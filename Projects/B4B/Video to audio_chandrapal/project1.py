#import moviepy.editor
from moviepy import *
from tkinter.filedialog import *

vid=askopenfilename()
video = VideoFileClip(vid)
#video=moviepy.editor.VideoFileClip(vid)

audio=video.audio
audio.write_audiofile("demo.mp3")

print("---end---")