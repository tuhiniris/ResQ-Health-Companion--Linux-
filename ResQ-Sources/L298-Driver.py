import RPi.GPIO as gpio
import time
import sys
import os
import tkinter as tk

def init():
	gpio.setmode(gpio.BCM)
	gpio.setup(17, gpio.OUT)
	gpio.setup(18, gpio.OUT)
	gpio.setup(23, gpio.OUT)
	gpio.setup(4, gpio.OUT)


def reverse(tf):
	
	gpio.output(17, True)
	gpio.output(23, False)
	gpio.output(18, True)
	gpio.output(4, False)
	time.sleep(tf)
	gpio.cleanup()
	

def forward(tf): #23 -> IN1,17->IN2 | 4 -> IN3,18->IN4
	
	gpio.output(17, False)
	gpio.output(23, True)	
	gpio.output(18, False)
	gpio.output(4, True)	
	time.sleep(tf)
	gpio.cleanup()
	

def turn_right(tf):
	gpio.output(17, True)
	gpio.output(23, False)	
	gpio.output(18, False)
	gpio.output(4, True)	
	time.sleep(tf)
	gpio.cleanup()

def turn_left(tf):
	
	gpio.output(17, False)
	gpio.output(23, True)	
	gpio.output(18, True)
	gpio.output(4, False)	
	time.sleep(tf)
	gpio.cleanup()

def stoppie(tf):
	gpio.output(17, False)
	gpio.output(23, False)	
	gpio.output(18, False)
	gpio.output(4, False)	
	time.sleep(tf)
	gpio.cleanup()	

def key_input(event):
	init()
	print ('Key:', event.char)
	key_press = event.char
	sleep_time = 0.02
	if key_press.lower() == 'w':
		forward(sleep_time)
	elif key_press.lower() =='s':
		reverse(sleep_time)
	elif key_press.lower() == 'a':
		turn_left(sleep_time+1)
	elif key_press.lower() == 'd':
		turn_right(sleep_time+1)
	else:
		stoppie(sleep_time)
	
running = False	
command = tk.Tk()

lbl=tk.Label(command, text="Drive", fg='black', font=("Arial", 20))
lbl.place(x=0, y=0)
command.title('ResQ')
command.geometry("400x40+10+10")
command.bind('<KeyPress>', key_input)
command.bind('<KeyRelease>', key_input)
os.system('clear')
command.mainloop()




