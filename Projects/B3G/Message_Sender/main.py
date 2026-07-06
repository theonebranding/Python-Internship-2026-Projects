from tkinter import *
import subprocess
import os
import sys

root = Tk()
root.title("Python Message Sender")
root.geometry("400x350")
root.resizable(False, False)

Label(
    root,
    text="PYTHON MESSAGE SENDER",
    font=("Arial",18,"bold"),
    fg="blue"
).pack(pady=20)

base_path = os.path.dirname(os.path.abspath(__file__))

def open_manual():
    subprocess.Popen([
        sys.executable,
        os.path.join(base_path, "manual_sms.py")
    ])

def open_excel():
    subprocess.Popen([
        sys.executable,
        os.path.join(base_path, "excel_sms.py")
    ])

Button(root, text="📱 Manual SMS", width=25, height=2,
       command=open_manual).pack(pady=10)

Button(root, text="📄 Excel SMS", width=25, height=2,
       command=open_excel).pack(pady=10)

Button(root, text="Exit", width=25, height=2,
       command=root.destroy).pack(pady=10)

root.mainloop()