import speech_recognition as sr
import os
import pyttsx

from gtts import gTTS
from time import ctime

import webbrowser
import serial


class Agnes():
	def speak(self,string):
		print string
		tts =gTTS(text = string, lang = 'en')
		tts.save("audio.mp3")
		os.system("mpg321 audio.mp3") 

	def start(self):
		self.speak("hello! I am Agnes")

		test = True

		while test:
			data = self.record()
			test = self.agnes(data+"\n")

	def record(self):
		r = sr.Recognizer()

		with sr.Microphone() as source:
			print("Say something!")
			audio = r.listen(source)

		data = ""

		try:
			data = r.recognize_google(audio)
			#data = r.recognize_sphinx(audio) # no internet, but imprecise
			print "you said:"+ data

		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))

		return data

	def read_file(self,name):
		arq = open(name,'r')
		phrases = arq.readlines()

		arq.close()

		return phrases

	def arduino(self, letter):
		ser = serial.Serial('/dev/ttyUSB0', 9600)
		ser.write(letter)
		check = False
	
	def convert_list_to_string(self,list):
		string = ""
		i = 0

		for x in list:
			
			if(i == len(list)-1):
				string = string+str(x)
				break
			i = i +1
			string = string+str(x)+"+"

		return string

	def agnes(self,data):
		questions = self.read_file("questions.txt")
		responses = self.read_file("responses.txt")
		
		i = 0
		check = True

		for x in questions:
			
			if x == data.lower():
				self.speak(responses[i])
				check = False
				break
			
				
			i = i +1

		# says time
		if "what time is it" in data:
			self.speak(ctime())
			check = False

		# shows location
		if "where is" in data:
			data = data.split(" ")
			location = self.convert_list_to_string(data[2:])
			self.speak("Hold on, I will show you where " + location + " is.")
			#os.system("firefox-browser https://www.google.nl/maps/place/" + location + "/&amp;")
			controller = webbrowser.get('Firefox')
			controller.open('https://www.google.com.br/maps/place/'+location)
			check = False

		# exit the program
		if "goodbye" in data:
			self.speak("Bye")
			return False

		if "turn on" in data:
			self.arduino("a")


		if "turn off" in data:
			self.arduino("e")
			
		if check:
			self.speak("I did not understand, repeate please")

		return True
