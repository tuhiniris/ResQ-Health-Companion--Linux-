import speech_recognition as sr
import pyttsx3,time
import DatabaseTools as dstvoice

r = sr.Recognizer()

def SpeakText(command):
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[2].id)
	engine.setProperty("rate", 120)
	engine.say(command)
	engine.runAndWait()

import sqlite3
connection = sqlite3.connect("resq_table.db")
cursor = connection.cursor()

#RULES

#instruction = voicing+" "+medicine+" "+timing+" "+time
#print(instruction)
#googlequotes(instruction)	

'''
command1 = """CREATE TABLE IF NOT EXISTS
resqmedicine(INDEX_ID INTEGER PRIMARY KEY AUTOINCREMENT,
USERNAME TEXT NOT NULL,
MEDICINE TEXT NOT NULL,
TIME INTEGER NOT NULL,
TYPE TEXT NOT NULL)"""

cursor.execute(command1)

'''

agent_id = {0:"'Admin'",1:"'Tuhinadri'",2:"'Aditya'",3:"'Walter'"} # Mapped By ResQ Admin

def fetcher(agent_id_num):
	try:
		global agent_id	
		# FETCHING MEDICINE RECORDS
		command2 = ("SELECT * FROM resqmedicine WHERE USERNAME = " +agent_id[agent_id_num])
		print(command2) #SQL Dynamic Query AND PASSED FROM VOICE

		cursor.execute(command2)
		results = cursor.fetchall()
		print(results)
		result_length = len(results)-1
		username = results[result_length][1]
		medicine = results[result_length][2]
		timenumber = str(results[result_length][3])
		timehour = results[result_length][4]
		time = timenumber+timehour

		#POST PROCESSING
		resultvoice = ("Hello "+username+". Your Next Medicine is "+medicine+". Please take it at "+time+".")
		print(resultvoice)
		#SpeakText(resultvoice)
		dstvoice.dbquotes(resultvoice)
		connection.commit()
	except:
		SpeakText("No Records Found!")
		pass

def newentrysuccess(text):
	SpeakText(text)

#fetcher(3)
