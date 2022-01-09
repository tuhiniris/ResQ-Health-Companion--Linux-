import subprocess 
import datetime
import os 
import sys 
import time 
import random 
import speech_recognition as sr
import face_recognition
import cv2
import numpy as np
import pandas
from func_timeout import func_timeout, FunctionTimedOut
import pyttsx3
from gtts import gTTS 
import pyglet
from pytube import YouTube
from moviepy.editor import *
from youtube_search import YoutubeSearch
from playsound import playsound
import glob

def startup():
	def progress(percent=0, width=30):
		hashes = width * percent // 100
		blanks = width - hashes
		print('\r[', hashes*'#', blanks*' ', ']', f' {percent:.0f}%', sep='',
			end='', flush=True)
	for i in range(101):
		progress(i)
		time.sleep(0.02)
	print("\nStarting Systems")
	time.sleep(2)
	googlespeaks("NineAI Home Assistant at your service")
	os.system('cls')           

def voicemode(command):    

	# Voice Triggers
	greet = ["hello","hi","hey","ok","morning","fine","hai","bhai"]
	cam = ["can you see me","camera","take a photo","picture","selfie"]
	m_activity = ["play music","song","songs","gaan","audio","music"]
	
	
	# Unknown Word Processing
	

	# Voice List
	#player = "/usr/bin/cvlc"
	player = "C:/Program Files/VideoLAN/VLC"
	voices = [
	"/voices/audio1.mp3",    
	"/voices/bored.mp3",
	"/voices/camerasmile.mp3",
	"/voices/canhelp.mp3",
	"/voices/comment1.mp3",
	"/voices/howyoudoin.mp3",
	"/voices/random talks/r1.mp3",
	"/voices/random talks/r2.mp3",
	"/voices/random talks/r3.mp3",
	"/voices/random talks/r4.mp3",
	"/voices/random talks/r5.mp3",
	"/voices/random talks/r6.mp3",
	"/voices/random talks/r7.mp3",
	"/voices/random talks/r8.mp3",
	
	# MUSIC
	"/voices/songs/Weero & Mitte - Our Dive (Radio Edit).mp3",
	"/voices/songs/Unknown Brain - Why Do I_ (feat. Bri Tolani) [NCS Release].mp3",
	"/voices/songs/Tobu - Return To The Wild [NCS Release].mp3",
	"/voices/songs/Sinner's Heist - Streetlight People (feat. Harley Bird) [NCS Release].mp3",
	"/voices/songs/Sekai - Running.mp3",
	"/voices/songs/RetroVision - Cake [NCS Release].mp3",
	"/voices/songs/Michael-White-ft.-Mylk---Venus--_NCS-Release_.mp3",
	"/voices/audio1.mp3"
	]
	
	# Process Controller
	timer = 0
	i = 3

	# Bot Logic
	if command in greet:
		i = 5
		timer = 5
	elif command == "Bye" or command == "bye":
		os.system('cls') 
		print("Goodbye !!")
		exit()
	elif command in cam:
		i = 2 
		timer = 5 
		scanner()            
	elif command in m_activity:
		musics = random.randint(14,20)
		i = musics
		timer = 100
	elif command == "NaN":
		quotes = random.choice([6,7,8,9,10,11,12,13])
		i = quotes
		timer = 10
		dino()
		os.system('cls')        
	elif command == "scan":
		scanner()
	elif command == "unknown words":
		os.system('cls')
		print("There are",len(unknown),"unknown words for this session.")
		print(unknown)  
		time.sleep(5)              
	elif command == "random":
		artists = ["avicii","syn cole music","post malone","ncs","nigel stanford music","linkin park","old town road","daft punk","illenium","sublab music"]
		newindex = random.randint(0,(len(artists)-1))        
		newcommand = artists[newindex]               
		googlespeaks("Playing Random Music by")
		print("Artist Selected",newcommand)
		googlespeaks(newcommand)
		youtubing(newcommand)
		os.system('cls')
		newcommand = ""
	elif command == "good morning":
		googlespeaks("Good Morning Sir. Playing Your Favourite Music Now.")
		for i in range(10):
			artists = ["avicii","syn cole music","post malone","nigel stanford music","linkin park","old town road","daft punk","illenium","sublab music"]
			newindex = random.randint(0,(len(artists)-1))        
			newcommand = artists[newindex]                         
			googlespeaks(newcommand)
			googlespeaks("Song") 
			googlespeaks(str(i+1))
			youtubing(newcommand)
			os.system('cls')
			newcommand = ""        
	
	elif command == "nigel stanford" or command == "Nigel Stanford":
		newcommand = "nigel stanford music" 
		googlespeaks(newcommand)
		for i in range(10):
			newcommand = "nigel stanford music"            
			googlespeaks("Song")
			googlespeaks(str(i+1))
			youtubing(newcommand)
			os.system('cls')
			newcommand = ""
		os.system('cls')
		newcommand = ""        
	
	elif command == "search":
		for i in range(10):
			googlespeaks("Song or Artist Name ?")
			searchkey = (voicecommands()+" Music")
			print(searchkey)
			time.sleep(5)
			googlespeaks(searchkey)
			youtubing(searchkey)
			os.system('cls')
			newcommand = ""
			searchkey = ""
		os.system('cls')
		newcommand = ""    
			
	
	elif command == "YouTube":        
		#googlespeaks("Good Morning Sir. Playing Your Favourite Music From YouTube.")
		artists = ["avicii","syn cole","post malone","nigel stanford music","linkin park","old town road","daft punk","illenium","sublab music"]
		for i in range(len(artists)):
			newcommand = artists[i]
			googlespeaks(newcommand)
			googlespeaks("Song") 
			googlespeaks(str(i+1))
			youtubing(newcommand)
			os.system('cls')
			newcommand = "" 
		os.system('cls')
		newcommand = "" 
		
	else:
		#stephen(command)#Offline
		google(command)#Online        
		new = random.choice([1,3,4])
		i = new
		timer = 10
		os.system('cls')
		if command not in unknown:
			print("Unknown Command -",command,"saved.")
			time.sleep(1.5)
			unknown.append(command) # Added Unknown Word to System Once       
		return
	
	# Intelli Playback System    
	try:    
		subprocess.call([player, voices[i]],timeout = timer)        
	except:
		pass
		os.system('cls') 
		print("|SYSTEM PASS|")
		time.sleep(0.5)
		os.system('cls')
		print("---NineAI Home Assistant---")
		print("|READY|\n")
		if len(unknown)>0:
			print("Currently Unknown Words")
			print(unknown)
			print("------")

def voicecommands():
	r = sr.Recognizer()
	m = sr.Microphone()
	os.system('cls')

	try:
		with m as source: r.adjust_for_ambient_noise(source)
		player2 = "/usr/bin/cvlc"
		try:    
			subprocess.call([player2, "/voices/random talks/blip.mp3"],timeout = 1)
					
		except:
			pass
		os.system('cls')   
		print("---Welcome to IEMA Smart Bot System---")
		print("|READY|\n")
		print("Say something!")
		
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

def camfy():
	video_capture = cv2.VideoCapture(0)

	# Load a sample picture and learn how to recognize it.
	obama_image = face_recognition.load_image_file("/face_recognition/examples/obama.jpg")
	obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

	# Load a second sample picture and learn how to recognize it.
	biden_image = face_recognition.load_image_file("/face_recognition/examples/biden.jpg")
	biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

	# Create arrays of known face encodings and their names
	known_face_encodings = [
		obama_face_encoding,
		biden_face_encoding
	]
	known_face_names = [
		"Barack Obama",
		"Joe Biden"
	]
	os.system('cls')
	face_locations = []
	face_encodings = []
	face_names = []
	process_this_frame = True

	while True:
		ret, frame = video_capture.read()
		small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
		rgb_small_frame = small_frame[:, :, ::-1]
		if process_this_frame:            
			face_locations = face_recognition.face_locations(rgb_small_frame)
			face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
			face_names = []
			for face_encoding in face_encodings:               
				matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
				name = "Guest"
				face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
				best_match_index = np.argmin(face_distances)
				if matches[best_match_index]:
					name = known_face_names[best_match_index]
				face_names.append(name)

		process_this_frame = not process_this_frame
		for (top, right, bottom, left), name in zip(face_locations, face_names):
			top *= 4
			right *= 4
			bottom *= 4
			left *= 4
			cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
			cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
			font = cv2.FONT_HERSHEY_DUPLEX
			cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
		cv2.imshow('Video', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	video_capture.release()
	cv2.destroyAllWindows()

def scanner():
	try:
		doitReturnValue = func_timeout(25, camfy)
	except FunctionTimedOut:
		print("Terminated Scanner")
	cv2.destroyAllWindows()

def stephen(unknowncommand):
	os.system('cls')
	print("Unknown Word Detected :",command)
	engine = pyttsx3.init() # object creation
	rate = engine.getProperty('rate')   # getting details of current speaking rate
	engine.setProperty('rate', 125)     # setting up new voice rate
	volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
	engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
	voices = engine.getProperty('voices')       #getting details of current voice  #changing index, changes voices. o for male
	engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female
	engine.say("Unknown Command Detected")
	time.sleep(1)
	engine.say("Stephen Haking will remember it")
	time.sleep(1)
	engine.say(unknowncommand)
	engine.runAndWait()
	engine.stop()
	engine.runAndWait()

def google(unknowncommand): 
	text = unknowncommand
	v = gTTS(text=unknowncommand,lang="en-GB",slow=False) 
	v.save("unknown.mp3")
	q = gTTS(text="Unknown Command Detected. We will remember it.",lang="en-uk",slow=False)
	q.save("generic.mp3") 
	playsound("unknown.mp3") 
	time.sleep(0.5)
	playsound("generic.mp3")

def googlespeaks(unknowncommand): 
	text = unknowncommand
	v = gTTS(text=unknowncommand,lang="en-GB",slow=False) 
	#v.save("unknown.mp3")
	v.save("C:/Users/MERN/Documents/GitHub/ResQ-Health-Companion/NineAI/voices/unknown.mp3")
	playsound("unknown.mp3") 
	time.sleep(0.5)
	os.remove("unknown.mp3")

def googlequotes(unknowncommand):
	text = unknowncommand
	v = gTTS(text=unknowncommand,lang="en-GB",slow=False) 
	v.save("C:/Users/MERN/Documents/GitHub/ResQ-Health-Companion/NineAI/voices/unknown.mp3")
	playsound("unknown.mp3") 
	time.sleep(0.5)
	os.remove("unknown.mp3")   

def dino():
	animation = pyglet.image.load_animation('simple.gif')
	animSprite = pyglet.sprite.Sprite(animation)
	w = animSprite.width
	h = animSprite.height
	window = pyglet.window.Window(width=w, height=h)
	r,g,b,alpha = 1.3,0.5,1.8,2.5
	pyglet.gl.glClearColor(r,g,b,alpha)

	@window.event
	def on_draw():
		window.cls()
		animSprite.draw()
		
	def close(event):
		window.close()
	try:	
		print("YES")
		pyglet.clock.schedule_once(close, 5.0)
		pyglet.app.run()
	except:
		print("Animation Loading Error")	

def youtubing(command):    
	#cleaner()
	searchkey = command
	results = YoutubeSearch(searchkey, max_results=20).to_dict()
	selection = random.randint(0,9)
	link = (results[selection].get("url_suffix")) 
	final = ("https://youtube.com"+link)
	print(final)
	youtube_link = final
	y = YouTube(youtube_link)
	t = y.streams.filter(only_audio=True).all()
	#t[0].download(output_path="/Music-Scraper")
	#list_of_files = glob.glob('/home/nine/Music-Scraper/*.mp4')
	t[0].download(output_path="C:/Users/MERN/Documents/GitHub/ResQ-Health-Companion/NineAI/voices")
	list_of_files = glob.glob("C:/Users/MERN/Documents/GitHub/ResQ-Health-Companion/NineAI/voices/*.mp4")
	latest_file = max(list_of_files, key=os.path.getctime)
	latest_file = latest_file.replace("voices\\","voices/",1)
	os.system('cls')
	print("---- Now Playing ----")
	#print(latest_file[20:][:-4])
	print(latest_file)
	#googlequotes("Now Playing")    
	#googlequotes(str(latest_file[25:][:-4]))
	playsound(latest_file)
	googlequotes("Song Has Ended")
	cleaner()
	

def cleaner():
	folder_path = "C:/Users/MERN/Documents/GitHub/ResQ-Health-Companion/NineAI/voices"
	for file_name in os.listdir(folder_path):
		if file_name.endswith('.mp4'):
			os.remove(folder_path +"/"+ file_name)

def quotesy():
	import csv
	with open('/home/nine/quotes/quotes/einstein.csv', 'r') as f:
	  file = csv.reader(f)
	  quotes = list(file)    
	chooser = random.randint(2,150)
	print(quotes[chooser][0])      
	googlequotes(quotes[chooser][0])   

unknown = []
#startup()


while(True):
	now = datetime.datetime.now()
	if now.hour >=0 and now.hour<=7 and now.minute >= 00:
		dino()
		print(now,"--I'm Sleeping--")
		quotesy()
		print("Take Rest")
		googlequotes("Sleep Well.")
		print("Count to Sleep...")
		for i in range(3600):
			print(3600-i)
			time.sleep(1)
		os.system('cls')
	elif now.hour==9 and now.minute<7 and now.minute>=5:
		dino()
		print("Good Morning, Time to Wake Up")    
		googlequotes("Good Morning, Time to Wake Up")
		time.sleep(100)
			   
	else:
		command = voicecommands();
		voicemode(command)
		
# Stephen is Offine Voice
# Google is Online Voices

# Voice Files Directory

'''
	"/voices/audio1.mp3",
	"/voices/bored.mp3",
	"/voices/camerasmile.mp3",
	"/voices/canhelp.mp3",
	"/voices/comment1.mp3",
	"/voices/howyoudoin.mp3",
	"/voices/random talks/r1.mp3",
	"/voices/random talks/r2.mp3",
	"/voices/random talks/r3.mp3",
	"/voices/random talks/r4.mp3",
	"/voices/random talks/r5.mp3",
	"/voices/random talks/r6.mp3",
	"/voices/random talks/r7.mp3",
	"/voices/random talks/r8.mp3"
	
	MUSIC
	
	"/voices/songs/Weero & Mitte - Our Dive (Radio Edit).mp3",
	"/voices/songs/Unknown Brain - Why Do I_ (feat. Bri Tolani) [NCS Release].mp3",
	"/voices/songs/Tobu - Return To The Wild [NCS Release].mp3",
	"/voices/songs/Sinner's Heist - Streetlight People (feat. Harley Bird) [NCS Release].mp3",
	"/voices/songs/Sekai - Running.mp3",
	"/voices/songs/RetroVision - Cake [NCS Release].mp3",
	"/voices/songs/Michael-White-ft.-Mylk---Venus--_NCS-Release_.mp3",
	"/voices/audio1.mp3"   
	
	
'''
