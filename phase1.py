# import datetime 
# import os 
# import psutil # pip install psutil
# import pyautogui as gui # pip install pyautogui
# import pyttsx3 # pip install pyttsx3
# import requests 
# import shutil
# import smtplib as smtp # pip install smtplib
# import socket
# import speech_recognition as sr # pip install SpeechRecognition
# import sys
# import time
# import tkinter as tk 
# import webbrowser as wb #pip install webbrowser
# import wikipedia as wiki # pip install wikipedia

# #===========================================================================================

# #START TEXT TO SPEECH 
# engine = pyttsx3.init()


# #DEFINE VARIABLES
# rate = engine.getProperty('rate')
# voices = engine.getProperty('voices') 
# volume = engine.getProperty('volume')


# #INTIALIZE VARIABLES
# engine.setProperty('rate', 225)
# engine.setProperty('voices', voices[0].id)
# engine.setProperty('volume',1.0)


# #UPDATE VARIABLE
# engine.setProperty('voices', voices[1].id)

# #===========================================================================================

# def  check_connectivity():
# 	request = requests.get("https://www.google.com")
# 	response = request.status_code
# 	if response == 200:
# 		return True
# 	return False

# def check_cpu_usage():
# 	speak("Cyberkid will now scan your device. Please wait for the result.")
# 	# time.sleep(10)
# 	CPUusage = psutil.cpu_percent()
# 	speak('CPU is at'+ str(CPUusage))
# 	core = psutil.cpu_count()
# 	speak("your processors has "+ str(core)  +" cores running")
# 	battery = psutil.sensors_battery()
# 	if battery.power_plugged == False:
# 		speak("You are currently running on battery")
# 	else:
# 		speak("You are currently charging your device")
# 	batteryvalue = battery.percent
# 	speak("Battery is at"+str(batteryvalue) + "percent")
# 	user = psutil.users()
# 	speak("You are logged in as"+str(user[0][0]))
# 	return CPUusage < 80

# def check_disk_usage(disk):
#     du = shutil.disk_usage(disk)
#     free = du.free / du.total * 100
#     return free > 20

# def check_localhost():
#     localhost = socket.gethostbyname('localhost')
#     if localhost == '127.0.0.1':
#         return True
#     return False

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# def time():
#     Time = datetime.datetime.now().strftime("%I:%M:%S")
#     speak("the current time is")
#     speak(Time)

# def check_memory():
# 	memory = psutil.virtual_memory()
# 	memoryvalue = memory.percent
# 	speak("Memory usage is at "+str(memoryvalue)+" percent")
# 	return memoryvalue < 80

# def welcomehome():
#     hour = datetime.datetime.now().hour
#     if hour >= 4 and hour<10:
#         part = "Good Morning"
#     elif hour >=10 and hour<16:
#         part = "Good Afternoon"
#     elif hour >= 16 and hour<22:
#         part = "Good Evening"
#     else:
#         part = "Good Night"
#     speak(part + "Sir")
#     speak("I am glad to have you here")

# #===========================================================================================

# # time()
# # check_disk_usage("/")
# # check_cpu_usage()
# # check_localhost()
# # check_connectivity()
# # check_memory()
# welcomehome()
# time()

# if check_disk_usage("/"):
# 	speak("Disk storage is good")
# 	print("Disk storage is good")
# else:
# 	speak("you're running out of disk space")
# 	print("you're running out of disk space")

# if check_cpu_usage():
# 	speak("CPU is healthy")
# 	print("CPU is healthy")
# else:
# 	speak("CPU is overloaded")
# 	print("CPU is overloaded")

# if check_memory():
# 	speak("Primary Memory is good")
# 	print("Primary Memory is good")
# else:
# 	speak("Memory usage is high")
# 	print("Memory usage is high")

# if check_localhost() and check_connectivity():
# 	speak("Loopback and Network Connectivity is good")
# 	print("Loopback and Network Connectivity is good")
# else: 
# 	speak("Network connectivity checks failed")
# 	print("Network connectivity checks failed")

# print("DONE !")
# speak("I am online and ready")






import datetime
import os 
import psutil
import pyttsx3
import requests
import shutil 
import socket
import time 

import MiniProj_2

#------------------------------------------------------

#START TEXT TO SPEECH 
engine = pyttsx3.init()
class VoiceEngine:
	def __init__(self, gender):
		#DEFINE VOICE PROPERTIES
		rate = engine.getProperty('rate')
		voices = engine.getProperty('voices') 
		volume = engine.getProperty('volume')
		#INTIALIZE VOICE PROPERTIES
		engine.setProperty('rate', 200)
		engine.setProperty('volume',1.0)
		#UPDATE VOICE PROPERTIES
		if gender == "female":
			engine.setProperty('voice', voices[1].id)
		else:
			engine.setProperty('voice', voices[0].id)
	def speak(self, audio):
		#TEXT TO SPEECH
	    engine.say(audio)
	    engine.runAndWait()

eng1 = VoiceEngine("male")
eng1.speak("hi")
eng2 = VoiceEngine("female")
eng2.speak("hello")
eng1 = VoiceEngine("male")
eng1.speak("How are you Nirvana?")
eng2 = VoiceEngine("female")
eng2.speak("I am online and ready, what about you Cyberkid?")
eng1 = VoiceEngine("male")
eng1.speak("I am good, just waiting for a System report for the day. ")
eng2 = VoiceEngine("female")
eng2.speak("Sure boy, lemme do it for you.")
#-------------------------------------------------------

class SystemStats:
	def  check_connectivity(self):
		request = requests.get("https://www.google.com")
		response = request.status_code
		if response == 200:
			return True
		return False

	def check_cpu_usage(self):
		print("Cyberkid will now scan your device." + 
			"Please wait for the result...")
		for i in range(5): 
			print(".")
			time.sleep(1)
		CPUusage = psutil.cpu_percent()
		print("CPU usage: "+ str(CPUusage) + "%")
		core = psutil.cpu_count()
		print("Number of Cores: "+ str(core))
		battery = psutil.sensors_battery()
		if battery.power_plugged == False:
			print("Power Mode: Discharging")
		else:
			print("Power Mode: Charging")
		batteryvalue = battery.percent
		print("Battery Level: "+str(batteryvalue) + "%")
		user = psutil.users()
		print("User : "+str(user[0][0]))
		return CPUusage < 80
	def check_disk_usage(self, disk):
	    du = shutil.disk_usage(disk)
	    free = du.free / du.total * 100
	    return free > 20
	def check_localhost(self):
		localhost = socket.gethostbyname('localhost')
		if localhost == '127.0.0.1':
			return True
		return False
	def check_memory(self):
		memory = psutil.virtual_memory()
		memoryvalue = memory.percent
		print("Memory usage: "+str(memoryvalue)+"%")
		return memoryvalue < 80
	def time(self):
		Time = datetime.datetime.now().strftime("%I:%M:%S")
		Date = datetime.date.today()
		print("Date : " + str(Date) + " and Time : " + Time)

sysStat = SystemStats()
sysStat.time()
time.sleep(1)
res1 = sysStat.check_cpu_usage()
eng2.speak("CPU is good") if res1 else eng2.speak("High CPU usage")
print("CPU usage : Good") if res1 else print("CPU usage : High")
time.sleep(1)
res2 = sysStat.check_connectivity()
eng2.speak("Network is good") if res2 else eng2.speak("Bad Network")
print("Network : Good") if res2 else print("Network : Bad")
time.sleep(1)
res3 = sysStat.check_disk_usage("/")
eng2.speak("Disk storage looks good") if res3 else eng2.speak("Disk Storage is "
	+ "running out of space")
print("Disk Storage : Good") if res3 else print("Disk Storage : "
	+ "Out of space")
time.sleep(1)
res4 = sysStat.check_localhost()
eng2.speak("Localhost is working") if res4 else eng2.speak("Localhost failed")
print("Localhost : Working") if res4 else print("Localhost : Failed")
time.sleep(1)
res5 = sysStat.check_memory()
eng2.speak("Memory is available") if res5 else eng2.speak("Low Memory")
print("Memory : Available") if res5 else print("Memory : Low Memory")

#----------------------------------------------------------------------

eng1 = VoiceEngine("male")
eng1.speak("So can you update this in the database for me?")
eng2 = VoiceEngine("female")
eng2.speak("Why not? So which database would you like me to access Buddy?")
dBase = input("Enter your Database name or just say it :P I am listening...\n")
if dBase == "SQL": 
	eng2.speak("Logging into your SQL database.")
	app = MiniProj_2.StudentApp()
	app.mainloop()
	eng2.speak("Saving changes to your Database.")
else:
	eng2.speak("Database not found !")

#-------------------------------------------------------------------------