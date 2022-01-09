def playdbquote(x):
	import os
	os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
	import pygame
	pygame.mixer.init()
	pygame.mixer.music.load(x)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue

def dbquotes(unknowncommand):
	from gtts import gTTS
	import time
	text = unknowncommand
	v = gTTS(text=unknowncommand,lang="en-us",slow=False) 
	v.save("dbmessage.mp3")
	playdbquote("dbmessage.mp3") 
	time.sleep(0.5)
