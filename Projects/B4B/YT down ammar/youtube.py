import yt_dlp

url = input("Enter YouTube Video URL: ")

try:
    options = {
        "outtmpl": 

link = YouTube("https://www.youtube.com/watch?v=QCIAGwQnJ4Y&list=PLKPf-MHoBx0APPS4kdCi6JAaxEJwZPFuJ&index=2")

video = link.streams.get_highest_resolution()

video.download("E:\WorkSpace\Epic Python Series\Audiobook")
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

    print("Video Downloaded Successfully!")

except Exception as e:
    print("Error:", e)