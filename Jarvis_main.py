import subprocess
import pyautogui
import sys
import pyttsx3
import cv2
import json
import speech_recognition as sr  
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import ctypes
import time
import requests
import pywhatkit
import pyscreenshot
import time
import cricket
import weather
import stock
import connect
from plyer import notification
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from gui import Ui_MainWindow


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()



def startup():
    speak("Initializing Jarvis")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Caliberating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak("All drivers are up and running")
    speak("All systems have been activated")
    speak("Now I am online")
    strTime = datetime.datetime.now().strftime("%I:%M:%S")
    speak(f"Sir, the time is {strTime}")
        
    
    speak("I am Jarvis 1 point o. Online and ready sir. Please tell me how may I help you")

    



assname ="Jarvis 1 point o"

class MainThread(QThread):  
        def __init__(self):
            super(MainThread, self).__init__()

        def run(self):
            self.TaskExecution() 

        def takeCommand(self):
            
            r = sr.Recognizer()
            
            with sr.Microphone() as source:
                
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)

            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language ='en-in')
                print(f"User said: {query}\n")

            except Exception as e:
                print(e)
                print("Unable to Recognize your voice.")
                return "None"
            
            return query


        def TaskExecution(self):
            startup()
            
            while True:
                
                self.query = self.takeCommand().lower()
                
            
                if 'wikipedia' in self.query:
                    speak('Searching Wikipedia...')

                    speak("What you want to search")
                    
                    results = wikipedia.summary('Flower')
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                elif 'open youtube' in self.query:
                    speak("Here you go to Youtube\n")
                    webbrowser.open("https://www.youtube.com/")

                elif 'open google' in self.query:
                    speak("Here you go to Google\n")
                    webbrowser.open("https://www.google.com/")

                elif 'open edge' in self.query:
                    speak("Here you go to Microsoft Edge\n")
                    webbrowser.open("https://www.edge.com/")

                elif 'open stack' in self.query:
                    speak("Here you go to Stack Over flow.Happy coding")
                    webbrowser.open("https://www.stackoverflow.com/")

                

                elif 'the time' in self.query:
                    strTime = datetime.datetime.now().strftime("%I:%M:%p")
                    speak(f"Sir, the time is {strTime}")

                elif 'cricket' in self.query :
                    cricket.cricket()

                elif 'play on youtube' in self.query:
                    try:
                        speak("What you want to play on youtube?")
                        search = "None"
                        while True:
                            search = self.takeCommand()
                            if(search == "None"):
                                speak("Could not recognise your voice")
                                speak("Please try again")
                                continue
                            else:
                                break

                        print("Connecting to youtube...")
                        speak("Connecting to youtube")
                        speak("Playing on youtube")
                        pywhatkit.playonyt(search)
                    except Exception as e:
                        print("Can't connect to youtube")
                        speak("Can't connect to youtube")

                elif 'search' in self.query:
                    try:
                        speak("What you want to search?")
                        search = "None"
                        while True:
                            search = self.takeCommand()
                            if(search == "None"):
                                speak("Could not recognise your voice")
                                speak("Please try again")
                                continue
                            else:
                                break

                        print("Connecting...")
                        speak("Connecting to google")
                        speak("Searching on google")
                        pywhatkit.search(search)
                    except Exception as e:
                        print("Can't connect")
                        speak("Can't connect")

                elif 'whatsapp message' in self.query:
                    try:
                        speak("To whom you want to send message?")
                        person = "None"
                        while True:
                            person = self.takeCommand()
                            if(person == "None"):
                                speak("Could not recognise sender's name")
                                speak("Please speak sender's name again")
                            else:
                                break
                        print("Person name is " + person)
                        speak("What message you want to?")
                        m = "None"
                        while True:
                            m = self.takeCommand()
                            if(m == "None"):
                                speak("Could not recognise your message")
                                speak("Please speak say again")
                            else:
                                break
                        print("Your message is " + m)
                        time.sleep(2)
                        print("Sending...")
                        phone_numbers = {"mummy":"+919311130711"}
                        pywhatkit.sendwhatmsg_instantly(phone_numbers[person], m, 15, True, 4)
                    except Exception as e:
                        print("Not able to send message")
                        speak("Not able to send message")

                elif 'weather' in self.query :
                    try:
                        speak("Which city weather information you want?")
                        city = self.takeCommand()
                        print("Searching...")
                        weather.weather_report(city)
                    except Exception as e:
                        print("Not able to able to get data")
                        speak("Not able to get data")

                elif 'stocks' in self.query or 'stock' in self.query:
                    try:
                        speak("Which company stocks you want to know?")
                        company = self.takeCommand()
                        print("Searching...")
                        stock.stock()
                    except Exception as e:
                        print("Not able to able to get data")
                        speak("Not able to get data")                
                        
                elif 'connect to phone' in self.query:
                    speak("Connecting with your smartphone")
                    speak("Connection has been successfully established")
                    connect.connect_to_phone()

                elif 'screenshot' in self.query:
                    image = pyscreenshot.grab()
                    file_name = str(time.time()) +".png"
                    image.save(file_name)
                    speak("Screenshot has been taken")

                elif 'close' in self.query:
                    pyautogui.moveTo(1896,12,2,pyautogui.easeOutQuad)
                    pyautogui.click()
                    pyautogui.moveTo(1749,552,2,pyautogui.easeOutQuad)

                elif 'down' in self.query:
                    pyautogui.scroll(-250)
                
                elif 'up' in self.query:
                    pyautogui.scroll(250)

                elif 'pause' in self.query:
                    pyautogui.press('k')

                elif 'play' in self.query:
                    pyautogui.press('k')

                elif 'full screen' in self.query:
                    pyautogui.press('f')

                elif 'normal screen' in self.query:
                    pyautogui.press('esc')

                elif 'take command' in self.query:
                    pyautogui.press('/')
                    pyautogui.keyDown('ctrl')
                    pyautogui.keyDown('a')
                    pyautogui.keyUp('a')
                    pyautogui.keyUp('ctrl')
                    pyautogui.press('backspace')
                    speak("Sir, what do you want to search")
                    searchbox = self.takeCommand()
                    pyautogui.write(searchbox, interval = 0.25)
                    pyautogui.press('enter')

                elif 'how are you' in self.query:
                    speak("I am fine, Thank you")
                    speak("How are you, Sir")

                elif 'fine' in self.query or "good" in self.query:
                    speak("It's good to know that your fine")

                elif 'exit' in self.query:
                    speak("Thanks for giving me your time")
                    pyautogui.moveTo(1401,796,2,pyautogui.easeOutQuad)
                    pyautogui.click()

                elif "who made you" in self.query or "who created you" in self.query:
                    speak("I have been created by Nikhil.")
                    
                elif 'joke' in self.query:
                    speak(pyjokes.get_joke())
                    
                elif 'search' in self.query or 'play' in self.query:
                    
                    self.query = self.query.replace("search", "")
                    self.query = self.query.replace("play", "")		
                    webbrowser.open(self.query)

                elif "who i am" in self.query:
                    speak("If you talk then definitely your human.")

                elif 'powerpoint presentation' in self.query:
                    speak("opening Power Point presentation")
                    power = r"C:\\Users\\pc\Desktop\Desktop\\New folder\\Jarvis1.pptx"
                    os.startfile(power)

                elif "who are you" in self.query:
                    speak("I am your virtual assistant created by Nikhil")

                elif 'reason for you' in self.query:
                    speak("I was created as a Minor project by Mister Nikhil ")

                elif 'change background' in self.query:
                    ctypes.windll.user32.SystemParametersInfoW(20,
                                                            0,
                                                            "Location of wallpaper",
                                                            0)
                    speak("Background changed successfully")
                
                elif 'lock window' in self.query:
                        speak("locking the device")
                        ctypes.windll.user32.LockWorkStation()

                elif 'shutdown system' in self.query:
                        speak("Hold On a Sec ! Your system is on its way to shut down")
                        subprocess.call('shutdown / p /f')
                        
                elif 'empty recycle bin' in self.query:
                    winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                    speak("Recycle Bin Recycled")

                elif "don't listen" in self.query or "stop listening" in self.query:
                    speak("for how much time you want to stop jarvis from listening commands")
                    a = int(self.takeCommand())
                    time.sleep(a)
                    print(a)

                elif "where is" in self.query:
                    self.query = self.query.replace("where is", "")
                    location = self.query
                    speak("User asked to Locate")
                    speak(location)
                    webbrowser.open("https://www.google.com/maps/place/" + location)

                elif "tell me about" in self.query:
                    self.query = self.query.replace("tell me about", "")
                    topic = self.query
                    res = wikipedia.summary(topic, sentences=2)
                    pr = str(res)
                    ptr = pr[0 : 150]
                    ans = ptr + "."
                    notification.notify(
                    title = topic.capitalize().format(datetime.date.today()),
                    message = ans ,
                    app_icon = "C:/My Files/Github Project/Jarvis Assistant/info.ico",
                    timeout = 40
                    )
                    speak(ptr)
                    
                elif "camera" in self.query or "take a photo" in self.query:
                    ec.capture(0, "Jarvis Camera ", "img.jpg")
                    
                elif "restart" in self.query:
                    subprocess.call(["shutdown", "/r"])
                    
                elif "hibernate" in self.query or "sleep" in self.query:
                    speak("Hibernating")
                    subprocess.call("shutdown / h")

                elif "log off" in self.query or "sign out" in self.query:
                    speak("Make sure all the application are closed before sign-out")
                    time.sleep(5)
                    subprocess.call(["shutdown", "/l"])

                elif "write a note" in self.query:
                    speak("What should i write, sir")
                    note = self.takeCommand()
                    file = open('jarvis.txt', 'w')
                    speak("Sir, Should i include date and time")
                    snfm = self.takeCommand()
                    if 'yes' in snfm or 'sure' in snfm:
                        strTime = datetime.datetime.now().strftime("%x | %r")
                        file.write(strTime)
                        file.write(" :- ")
                        file.write(note)
                    else:
                        file.write(note)
                
                elif "note" in self.query:
                    speak("Showing Notes")
                    file = open("jarvis.txt", "r")
                    print(file.read())
                    speak(file.read(6))
                
                elif "wikipedia" in self.query:
                    webbrowser.open("http://www.wikipedia.com/")

                elif "Good Morning" in self.query:
                    speak("A warm" +self.query)
                    speak("How are you Mister")
                    speak(assname)

                elif "will you be my gf" in self.query or "will you be my bf" in self.query:
                    speak("I'm not sure about, may be you should give me some time")

                elif "how are you" in self.query:
                    speak("I'm fine, glad you me that")

                elif "i love you" in self.query:
                    speak("It's hard to understand")

                elif "what is" in self.query or "who is" in self.query:
                    
                    client = wolframalpha.Client("API_ID")
                    res = client.query(self.query)
                    
                    try:
                        print (next(res.results).text)
                        speak (next(res.results).text)
                    except StopIteration:
                        print ("No results")

startExecution = MainThread()


class Main(QMainWindow):
        def __init__(self):
            super().__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.pushButton.clicked.connect(self.startTask)
            self.ui.pushButton_2.clicked.connect(self.close)

        def __del__(self):
            sys.stdout = sys.__stdout__

        def startTask(self):
            self.ui.movie = QtGui.QMovie("C:/My Files/Github Project/Jarvis Assistant/images/live_wallpaper.gif")
            self.ui.label.setMovie(self.ui.movie)
            self.ui.movie.start()
            self.ui.movie = QtGui.QMovie("C:/My Files/Github Project/Jarvis Assistant/images/initiating.gif")
            self.ui.label_2.setMovie(self.ui.movie)
            self.ui.movie.start()
            timer = QTimer(self)
            timer.timeout.connect(self.showTime)
            timer.start(1000)
            startExecution.start()

        def showTime(self):
            current_time = QTime.currentTime()
            current_date = QDate.currentDate()
            label_time = current_time.toString('hh:mm:ss')
            label_date = current_date.toString(Qt.ISODate)
            self.ui.textBrowser.setText(label_date)
            self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())



