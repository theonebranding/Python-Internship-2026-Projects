"""
Auto File Organizer
Watches a directory and automatically sorts files into categorized subfolders.
Usage:
    python organizer.py [--source PATH] [--watch] [--dry-run]
"""

import os
import shutil
import argparse
import logging
import time
from pathlib import Path
from datetime import datetime

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
    WATCHDOG_AVAILABLE = True
except ImportError:
    WATCHDOG_AVAILABLE = False

# ── Category rules ──────────────────────────────────────────────────────────
CATEGORIES = {
    "Images":     [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico", ".tiff", ".heic"],
    "Videos":     [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".m4v"],
    "Audio":      [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a", ".opus"],
    "Documents":  [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".odt", ".rtf", ".md"],
    "Code":       [".py", ".js", ".ts", ".html", ".css", ".cpp", ".c", ".java", ".go", ".rs", ".rb", ".php", ".sh", ".json", ".yaml", ".yml", ".toml", ".xml", ".sql"],
    "Archives":   [".zip", ".tar", ".gz", ".rar", ".7z", ".bz2", ".xz"],
    "Executables":[".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm", ".appimage"],
    "Fonts":      [".ttf", ".otf", ".woff", ".woff2", ".eot"],
    "Data":       [".csv", ".tsv", ".parquet", ".feather", ".sqlite", ".db", ".hdf5"],
}

# Build reverse lookup: extension → category
EXT_MAP = {}
for category, extensions in CATEGORIES.items():
    for ext in extensions:
        EXT_MAP[ext.lower()] = category

# ── Logging setup ────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("organizer.log", encoding="utf-8"),
    ],
)
log = logging.getLogger(__name__)


# ── Core organizer logic ─────────────────────────────────────────────────────
def get_category(file_path: Path) -> str:
    """Return the category folder name for a file."""
    return EXT_MAP.get(file_path.suffix.lower(), "Others")


def safe_destination(dest_dir: Path, filename: str) -> Path:
    """Return a non-colliding destination path (appends _1, _2 … if needed)."""
    dest = dest_dir / filename
    if not dest.exists():
        return dest
    stem, suffix = Path(filename).stem, Path(filename).suffix
    counter = 1
    while True:
        candidate = dest_dir / f"{stem}_{counter}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def move_file(src: Path, dest: Path, dry_run: bool = False) -> bool:
    """Move src → dest. Returns True on success."""
    try:
        if dry_run:
            log.info("[DRY RUN] Would move: %s  →  %s", src.name, dest)
            return True
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dest))
        log.info("Moved: %-40s  →  %s", src.name, dest.parent.name)
        return True
    except Exception as exc:
        log.error("Failed to move %s: %s", src, exc)
        return False


def organize_directory(source: Path, dry_run: bool = False) -> dict:
    """
    Scan source directory and move every non-directory file into the
    appropriate category subfolder. Returns a summary dict.
    """
    if not source.is_dir():
        raise NotADirectoryError(f"Source is not a directory: {source}")

    summary = {"moved": 0, "skipped": 0, "errors": 0}

    for item in list(source.iterdir()):
        # Skip directories, hidden files, and the log file itself
        if item.is_dir() or item.name.startswith(".") or item.name == "organizer.log":
            continue

        category = get_category(item)
        dest_dir = source / category
        dest = safe_destination(dest_dir, item.name)

        if move_file(item, dest, dry_run):
            summary["moved"] += 1
        else:
            summary["errors"] += 1

    log.info(
        "Done — moved: %d  |  errors: %d  |  dry-run: %s",
        summary["moved"], summary["errors"], dry_run,
    )
    return summary


# ── Watchdog event handler ───────────────────────────────────────────────────
class OrganizerHandler(file.py):
    """Handles new files created in the watched directory."""

    def __init__(self, source: Path, dry_run: bool = False):
        super().__init__()
        self.source = source
        self.dry_run = dry_run
        # Track recently processed files to avoid double-triggers
        self._seen: set[str] = set()

    def on_created(self, event):
        if event.is_directory:
            return
        src = Path(event.src_path)
        # Ignore files already inside a category subfolder
        if src.parent != self.source:
            return
        if src.name in self._seen:
            return
        # Brief pause so the file finishes writing before we move it
        time.sleep(0.5)
        if not src.exists():
            return
        self._seen.add(src.name)
        category = get_category(src)
        dest_dir = self.source / category
        dest = safe_destination(dest_dir, src.name)
        move_file(src, dest, self.dry_run)


# ── CLI entry point ──────────────────────────────────────────────────────────
def parse_args():
    parser = argparse.ArgumentParser(
        description="Auto File Organizer — sorts files into category subfolders.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python organizer.py                          # Organize ~/Downloads
  python organizer.py --source ~/Desktop       # Organize Desktop
  python organizer.py --watch                  # Organize + keep watching
  python organizer.py --dry-run                # Preview without moving files
        """,
    )
    parser.add_argument(
        "--source", "-s",
        type=Path,
        default=Path.home() / "Downloads",
        help="Directory to organize (default: ~/Downloads)",
    )
    parser.add_argument(
        "--watch", "-w",
        action="store_true",
        help="Keep running and organize new files as they appear",
    )
    parser.add_argument(
        "--dry-run", "-n",
        action="store_true",
        help="Show what would happen without actually moving files",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    source = args.source.expanduser().resolve()

    log.info("Source : %s", source)
    log.info("Dry-run: %s", args.dry_run)

    # Initial scan
    organize_directory(source, dry_run=args.dry_run)

    # Watch mode
    if args.watch:
        if not WATCHDOG_AVAILABLE:
            log.error("Install watchdog to use --watch:  pip install watchdog")
            return
        log.info("Watching for new files … (Ctrl+C to stop)")
        handler = OrganizerHandler(source, dry_run=args.dry_run)
        observer = Observer()
        observer.schedule(handler, str(source), recursive=False)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            log.info("Stopping watcher …")
            observer.stop()
        observer.join()


if __name__ == "__main__":
    main()
