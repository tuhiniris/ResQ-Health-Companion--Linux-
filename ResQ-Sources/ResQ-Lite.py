import subprocess 
import datetime
import os 
import sys 
import time 
import random 
import speech_recognition as sr
#import face_recognition
#import cv2
import numpy as np
import pandas
from func_timeout import func_timeout, FunctionTimedOut
import pyttsx3
from gtts import gTTS 
import pyglet
#from pytube import YouTube
#from moviepy.editor import *
#from youtube_search import YoutubeSearch
#from playsound import playsound
import glob
import os, signal
import DanceRobot as resq_movement
import DatabaseMapper as userDAO

sys_check_for_my_wheel = 0
#resq_movement.scan()
#resq_movement.moveforward(1)
#resq_movement.movebackward(1)
#resq_movement.moveleftward(2)
#resq_movement.moverightward(2)

def process():	
	name = "vlc"
	try:
		# iterating through each instance of the process
		for line in os.popen("ps ax | grep " + name + " | grep -v grep"):
			fields = line.split() 
			
			# extracting Process ID from the output
			pid = fields[0]
			
			# terminating process
			os.kill(int(pid), signal.SIGKILL)
		print("Process Successfully terminated")		
	except:
		print("Error Encountered while running script")

def playsound(x):
	import pygame
	pygame.mixer.init()
	pygame.mixer.music.load(x)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue	

def startup():
	def progress(percent=0, width=30):
		hashes = width * percent // 100
		blanks = width - hashes
		print('\r[', hashes*'#', blanks*' ', ']', f' {percent:.0f}%', sep='',end='', flush=True)
	for i in range(101):
		progress(i)
		time.sleep(0.02)
	print("\nStarting Systems")
	time.sleep(2)
	os.system('clear')

def voicecommands():
	r = sr.Recognizer()
	m = sr.Microphone()
	os.system('clear')

	try:
		with m as source: r.adjust_for_ambient_noise(source)
		player2 = "/usr/bin/cvlc"
		try:    
			subprocess.call([player2, "/home/pi/Desktop/FYP_AT/Notify/blip.mp3"],timeout = 1)					
		except:
			#time.sleep(10)
			pass
		os.system('clear')   
		print("---ResQ,from Community Health Hub---")
		print("|READY|\n")
		print("|Version : 0.8b|\n")
		print("Developed By : Tuhinadri Banerjee & Aditya Kundu\n")
		print("Say Something")
		#time.sleep(1) --> THIS SLEEP ADJUSTING COLLEGE WIFI / JIOFI LATENCY
		with m as source: audio = r.listen(source)
		print("Got it! Now to recognize it...")
		try:
			value = r.recognize_google(audio)
			if str is bytes:
				print(u"You said {}".format(value).encode("utf-8"))
			else:
				print("You said {}".format(value))
				return(value)
		except sr.UnknownValueError:
			print("Oops! Didn't catch that")
			return("NaN")
		except sr.RequestError as e:
			print("Couldn't request results from Google Speech Recognition service; {0}".format(e))
			return("NaN")
	except KeyboardInterrupt:
		pass

def voicemode(command):
	global sys_check_for_my_wheel
	import time,random,os,subprocess    
	
	time.sleep(1)
	# Voice Triggers
	greet = ["hello","hi","hey","hay","ok","morning","fine","hai","bhai","how are you"]
	important = ["should i take medicine","medicine","which medicine","when medicine"]
	#cam = ["can you see me","camera","take a photo","picture","selfie"] # In FULL VERSION RESQ
	m_activity = ["play music","song","songs","gaan","audio","music"]	# In FULL VERSION RESQ
	voices = ["idle2.mp3","idle1.mp3","readycall.mp3","bored.mp3","camerasmile.mp3","canhelp.mp3","comment1.mp3"]
	motion = ["go","forward","backward","move","patrol","scan","left","right","can"]
	# Unknown Word Processing	

	# Voice List
	player = "/usr/bin/cvlc"    
	
	# Process Controller
	timer = 0
	i = 0

	# Bot Logic
	if command in greet:
		resq_movement.nudgeyes()
		new = random.choice([0,1,2,3,4,5,6])
		i = new
		timer = 5
	
	elif command == "Bye" or command == "bye" or command == "goodbye" or command == "Goodbye":
		os.system('clear') 
		print("Goodbye !!")
		googlequotes("ResQ shuts down in 3 Seconds")
		resq_movement.nudgeno()
		exit()
	
	elif command == "good morning":
		os.system('clear')
		print("Good Morning Sir") 
		googlequotes("Good Morning")
		import time
		time.sleep(2)
	
	elif command in m_activity:
		try:
			import os
			import random 
			path="/home/pi/Desktop/ResQ-Sources/songs/"
			files=os.listdir(path)
			d=random.choice(files)
			print("Now Playing :",d)	
			import vlc
			p = vlc.MediaPlayer(path+d)
			from mutagen.mp3 import MP3
			audio = MP3(path+d)
			length = (audio.info.length)
			p.play()			
			time.sleep(length)
			process()
		except:
			import time
			time.sleep(10)
			pass			
	
	elif command == "relax":
		for jjx in range(5):
			try:
				import os
				import random 
				path="/home/pi/Desktop/ResQ-Sources/songs/"
				files=os.listdir(path)
				d=random.choice(files)
				print("Now Playing :",d)	
				import vlc
				p = vlc.MediaPlayer(path+d)
				from mutagen.mp3 import MP3
				audio = MP3(path+d)
				length = (audio.info.length)
				p.play()			
				time.sleep(length)
				process()
			except:
				import time
				time.sleep(10)
				pass	
	
	elif command in important: # Linker to SQLite Cloud
		internal_flag = 0 # Controller of Infinite Loop
		hashmap_for_users = {'zero':0,'one':1,'two':2,'three':3,0:0,1:1,2:2,3:3} # Home User Package
		
		googlequotes("What is your Family ID")			
		#userDAO.fetcher(2)
		while(internal_flag==0):
			userid = voicecommands() #Get ID NUMBER and Send to DAO
			try:
				if userid == "Tu" or userid == "tu" or userid == "too" or userid == "Too":
					userid = 2
				elif userid == "tree" or userid == "free":
					userid = 3	
				userid = int(userid)
				print("Your UserID is",userid)
				if userid in hashmap_for_users:
					scanned_id = hashmap_for_users.get(userid)
					resq_movement.nudgeyes()
					userDAO.fetcher(userid) #Passed Value of userid from hashmap
					internal_flag = 1
				else:
					resq_movement.nudgeno()
					googlequotes("Couldn't get you clearly, Try Again")	
						
			except:
				resq_movement.nudgeno()
				googlequotes("Error in Detection, Try Again")
				pass	
	
	elif command in motion: # Motion Control System
	#motion = ["go","forward","backward","move","patrol","scan","left","right"]	
		if(sys_check_for_my_wheel == 0):		
			googlequotes("Checking Engine")			
			resq_movement.moveforward(1)
			resq_movement.movebackward(1)
			resq_movement.moveleftward(2)
			resq_movement.moverightward(2)				
			googlequotes("Done Successfully")
			sys_check_for_my_wheel = 1
			# ------------------- END OF CHECKING WHEELS, LET'S CONTINUE
		if command == "can":
			command = "scan" #Mic Error Solution
		
		marker = 3
		'''
		try:
			duration = voicecommands()		
			if duration == "little":
				marker = 2
			elif duration == "long":
				marker = 4
		except:
			googlequotes("Some error occured, using default value")
			pass		
		'''
		if command == "forward":
			resq_movement.moveforward(marker)
		elif command == "backward":
			resq_movement.movebackward(marker)
		elif command == "left":
			resq_movement.moveleftward(marker)
		elif command == "right":
			resq_movement.moverightward(marker)
		if command == "scan" or command == "patrol":
			googlequotes("Give Way")
			resq_movement.scan()					
	
	else:
		google(command) #Online        
		new = random.choice([0,1,2])
		i = new
		timer = 10
		os.system('clear')
		if command not in unknown:
			print("Unknown Command -",command,"saved.")
			time.sleep(1.5)
			unknown.append(command) # Added Unknown Word to System Once       
		return
	
	# Kundu Playback System    
	try:    
		subprocess.call([player, voices[i]],timeout = timer)        
	except:
		import time
		#time.sleep(10) -> Debug Message Read Mode
		pass
		os.system('clear') 
		print("|SYSTEM PASS|")
		os.system('clear')
		print("---ResQ,from Community Health Hub---")
		print("|READY|\n")
		print("|Version : 0.8b|\n")
		if len(unknown)>0:
			print("Currently Unknown Words")
			print(unknown)
			print("------")

def googlequotes(unknowncommand):
	text = unknowncommand
	v = gTTS(text=unknowncommand,lang="en-uk",slow=False) 
	v.save("unknown.mp3")
	playsound("unknown.mp3") 
	time.sleep(0.2) #Default I keep 0.5 -> Reliable, 0.2 is faster

def google(unknowncommand): 
	text = unknowncommand
	v = gTTS(text=unknowncommand,lang="en-uk",slow=False) 
	v.save("unknown.mp3")
	q = gTTS(text="Sorry, ResQ Doesn't Know This.",lang="en-uk",slow=False)
	q.save("generic.mp3") 
	playsound("unknown.mp3") 
	time.sleep(0.1) #Default I keep 0.5 -> Reliable, 0.2 is faster
	playsound("generic.mp3")
	
unknown=[]
startup()



import vlc
p = vlc.MediaPlayer("readycall.mp3")
from mutagen.mp3 import MP3
audio = MP3("readycall.mp3")
length = (audio.info.length)
import time, sys, os
os.system("clear")
print("\n" + "ResQ is Ready".center(30, " "))
time.sleep(1)
p.play()			
time.sleep(length)
process()

while(True):
	import time
	os.system('clear')	
	time.sleep(0.3)
	command = voicecommands()
	if command!="nan":
		print("RECOGNISED DONE, PING NEXT STEP")
		voicemode(command.lower())   
	else:
		os.system('clear')
		command = voicecommands()	
