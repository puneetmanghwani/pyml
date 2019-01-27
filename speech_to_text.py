#!/usr/bin/python3

import speech_recognition as sr
r = sr.Recognizer()


mic=sr.Microphone()

with mic as source:
		
	audio=r.listen(source)
	
print("you said", r.recognize_google(audio))

 
