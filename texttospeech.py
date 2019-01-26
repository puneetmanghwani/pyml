#!/usr/bin/python3
'''
import pyttsx3
engine=pyttsx3.init()
engine.say('this is this is this is this is this is this is this is this is this is this is this is this is this is this is this is this is this is this is this is this is this is this is this is this is ')
engine.runAndWait()
'''


from gtts import gTTS
import os
tts=gTTS(text='good morning',lang='en')
tts.save("good.mp3")

os.system("vlc good.mp3")
