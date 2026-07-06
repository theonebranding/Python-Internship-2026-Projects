from deep_translator import GoogleTranslator
from gtts import gTTS
import os

print("\n\t\t*********TEXT TO SPEECH CONVERTER*********")
print("\t\t--------------------------------------------")
print("\t\t1.English")
print("\t\t2.Gujarati")
print("\t\t3.Hindi")
print("\t\t---------------------------------------------")

ch=input("Enter Your Choice:")

text=input("Enter Message to Convert into Speech:")

if ch=="1":
    translated_text=text
    language='en'
elif ch=="2":
    translated_text=GoogleTranslator(source='en',target='gu').translate(text)
    language='gu'
elif ch=="3":
    translated_text=GoogleTranslator(source='en',target='hi').translate(text)
    language='hi'
else:
    print("Please Enter Valid Choice!!!")
    exit()

print("\n\nThe Text You Entered is:",text)
print("\nThe Language You Selected is:",language)
print("\nThe Translated Text is:",translated_text)
s1=gTTS(text=translated_text,lang=language)
s1.save("speech.mp3")

print("Speech Converted Successfully!!!")
os.system("speech.mp3")