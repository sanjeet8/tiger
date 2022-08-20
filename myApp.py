import datetime
import os
from PyDictionary import PyDictionary as pd
import keyboard
import pyautogui
import pywhatkit
import webbrowser
import cv2
import pyjokes
import numpy as np
from playsound import playsound
import speech_recognition as sr
import wikipedia
import pyttsx3
import PyPDF2
from time import sleep


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
   engine.say(audio)
   engine.runAndWait()


def takeCommand():
    # it takes microphone input fromthe user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognizing
        print(f"User Said: {query}\n")  # User query will be printed

    except Exception as e:
        print(e)
        print("Say that Again please...")
        # speak("Pardon Please...")
        return "None"  # None String will be return
    return query

def Reader():
    speak("ok, please Tell Me The name of book")
    name = takeCommand()
    if 'networking' in name:
        os.startfile('F:\\NOTES\\computer book\\Computer Networks - A Tanenbaum - 5th edition.pdf')
        book = open('F:\\NOTES\\computer book\\Computer Networks - A Tanenbaum - 5th edition.pdf')
        #pdfReader = PyPDF2.PdfFileReader(book)
        #page = pdfReader.getNumPages()
        #speak(f"Number of pages in this book are {page}")
        pageNum = int(input("Enter the page number"))
        #pages = pdfReader.getPage(pageNum)
        #text = pages.extractText()
        speak("In which language you want to listen?")
        lang = takeCommand()
        #speak(text)

def Music():
    query = takeCommand()
    query = query.replace("play","")
    #speak(f"ok sir, playing {query}")
    if ' Amplifier' in query:
        os.startfile('E:\\Audios\\My Music\\01-Amplifire.mp3')
    else:
        speak(f"Ok, opening {query} on youtube")
        pywhatkit.playonyt(query)

def anchor ():
    speak("ok, Roll Number...?")
    RollNo = takeCommand()
    if '1' in RollNo:
        RollNo = RollNo.replace("Roll Number","")
        speak(f"so our first guest is, Roll Number {RollNo}, Anand Kumar Tiwari")
        speak("he is going to represent something, so over to you Anand...")
    elif '2' in RollNo:
        RollNo = RollNo.replace("Roll Number","")
        speak(f"so our next guest is, Roll Number {RollNo}, Komal Kumari")
        speak("she is going to represent something, so over to you Komal...")
    elif '3' in RollNo:
        RollNo = RollNo.replace("Roll Number","")
        speak(f"so our next guest is, Roll Number {RollNo}, Sanjeet Kumar")
        speak("he is going to represent something, so over to you Sanjeet...")
    elif '4' in RollNo:
        RollNo = RollNo.replace("Roll Number","")
        speak(f"so our next guest is, Roll Number {RollNo}, tiger Prabhakar")
        speak("he is going to represent something, so over to you tiger...")
    elif '5' in RollNo:
        RollNo = RollNo.replace("Roll Number","")
        speak(f"so our next guest is, Roll Number {RollNo}, Sunil Kumar Tiwary")
        speak("he is going to represent something, so over to you Sir...")
    elif '6' in RollNo:
        RollNo = RollNo.replace("Roll Number","")
        speak(f"so our next guest is, Roll Number {RollNo}, Sanju Tiwary")
        speak("he is going to represent something, so over to you maam...")
    query = takeCommand()
    if 'thank you' in query:
        pass


def whatsapp():
    speak("which person you want to send message")
    name = takeCommand()
    name = name.replace("tiger", "")
    name = name.replace("send message to", "")
    if 'bhyaa' in name:
        speak("Ok sir, what do you want to send?")
        msg = takeCommand()
        speak("Tell me the time of sending message")
        speak("Tell me the time in hour")
        hour = int(takeCommand())
        speak("Tell me the time in minute")
        min = int(takeCommand())
        pywhatkit.sendwhatmsg("+919708200551",msg,hour,min,20)
        speak(f"ok sir, sending whatsapp message to {name}...")
    elif 'papa' in name:
        speak("Ok sir, what do you want to send?")
        msg = takeCommand()
        speak("Tell me the time of sending message")
        speak("Tell me the time in hour")
        hour = int(takeCommand())
        speak("Tell me the time in minute")
        min = int(takeCommand())
        pywhatkit.sendwhatmsg("+918083535151",msg,hour,min,20)
        speak(f"ok sir, sending whatsapp message to {name}...")
    elif 'ansh' in name:
        speak("Ok, what do you want to send?")
        msg = takeCommand()
        speak("Tell me the time of sending message")
        speak("Tell me the time in hour")
        hour = int(takeCommand())
        speak("Tell me the time in minute")
        min = int(takeCommand())
        pywhatkit.sendwhatmsg("+919110919951",msg,hour,min,20)
        speak(f"ok sir, sending whatsapp message to {name}...")

def openApp():
    speak("ok,")

    if 'code' in query:
        speak("opening visual studio...")
        os.startfile("C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\Community\\Common7\\IDE\\devenv.exe")
    elif 'chrome' in query:
        speak("opening chrome...")
        os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
    elif 'wordpad' in query:
        speak("opening wordpad...")
        os.startfile("C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe")
    elif 'facebook' in query:
        speak("opening facebook...")
        webbrowser.open("https://www.facebook.com/")
    elif 'instagram' in query:
        speak("opening instagram...")
        webbrowser.open("https://www.instagram.com/")
    elif 'twitter' in query:
        speak("opening twitter...")
        webbrowser.open("https://www.twitter.com/")
    elif 'youtube' in query:
        speak("opening youtube...")
        webbrowser.open("https://www.youtube.com/")
    elif 'form' in query:
        speak("opening google form...")
        webbrowser.open("https://docs.google.com/forms/u/0/")
    elif 'map' in query:
        speak("opening google map...")
        webbrowser.open("https://www.google.co.in/maps/@25.6170256,85.116814,15z?hl=en&authuser=0")
    elif 'drive' in query:
        speak("opening google drive...")
        webbrowser.open("https://drive.google.com/drive/u/0/my-drive")
    elif 'meet' in query:
        speak("opening google meet...")
        webbrowser.open("https://meet.google.com/?hs=197&pli=1&authuser=0")
    elif 'gmail' in query:
        speak("topening gmail...")
        webbrowser.open("https://mail.google.com/mail/u/0/")

def closeApp():
    speak("ok, please wait")

    if 'chrome' in query:
        os.system("TASKKILL /f /im chrome.exe")

    elif 'code' in query:
        os.system("TASKKILL /f /im devenv.exe")

    elif 'wordpad' in query:
        os.system("TASKKILL /f /im wordpad.exe")



def Dict():
    speak("ok, dictionary activated")
    speak("what do you want to know")
    mean = takeCommand()
    speak("Ok, Please wait, i am searching")
    if'meaning' in mean:
        mean = mean.replace("what is the meaning of","")
        mean = mean.replace("tiger","")
        mean = mean.replace("of","")
        mean = mean.replace("the meaning of","")
        result = pd.meaning(mean)
        speak(f"The meaning of {mean} is {result}")

    elif 'synonym of' in mean:
        mean = mean.replace("what is the synonym of","")
        mean = mean.replace("tiger","")
        mean = mean.replace("of","")
        mean = mean.replace("synonym of","")
        result = pd.synonym(mean)
        speak(f"The synonym of {mean} is {result}")

    elif 'antonym of' in mean:
        mean = mean.replace("what is the antonym of","")
        mean = mean.replace("tiger","")
        mean = mean.replace("of","")
        mean = mean.replace("antonym of","")
        result = pd.antonym(mean)
        speak(f"The antonym of {mean} is {result}")



def youtubeAutomation():
    speak("what do you want?")
    command = takeCommand()

    if 'pause' in command:
        keyboard.press('space bar')
    elif 'restart' in command:
        keyboard.press('0')
    elif 'mute' in command:
        keyboard.press('m')
    elif 'skip' in command:
        keyboard.press('l')
    elif 'back' in command:
        keyboard.press('j')
    elif 'full screen' in command:
        keyboard.press('f')
    elif 'film mode' in command:
        keyboard.press('t')

def wishMe():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Hey Sanjeet, it's {strTime}")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good AfterNoon")
    else:
        speak("Good Evening")
    speak("I am tiger, How may i help you?...")


if __name__=="__main__" :
  wishMe()

  while True:
    query = takeCommand().lower()
    if 'tiger' in query:
    #logic for executing task based on query
     if 'wikipedia' in query:
         speak('Searching Wikipedia...')
         query = query.replace("wikipedia", "")
         results = wikipedia.summary(query, sentences = 3)
         speak("According to wikipedia...")
         print(results)
         speak(results)
     elif 'who' in query:
         speak('Searching Wikipedia...')
         query = query.replace("who", "")
         results = wikipedia.summary(query, sentences = 2)
         speak("According to wikipedia")
         print(results)
         speak(results)

     elif 'youtube' in query:
        speak("Ok, please wait ...")
        query = query.replace("tiger","")
        query = query.replace("youtube","")
        speak(f"Ok, opening {query} in youtube")
        pywhatkit.playonyt(query)
     elif 'news' in query:
        speak("Ok, please wait ...")
        speak("which news you want to play?")
        query = takeCommand()
        query = query.replace("tiger", "")
        query = query.replace("some","")
        speak(f"Ok, opening {query}")
        pywhatkit.playonyt(query)
     elif 'how' in query:
        speak("Ok sir, this is what i found in youtube ...")
        query = query.replace("tiger","")
        query = query.replace("youtube search","")
        web = 'https://www.youtube.com/results?search_query=' + query
        webbrowser.open(web)

     elif 'google' in query:
         speak("Ok sir, this is what i found in google ...")
         query = query.replace("tiger", "")
         query = query.replace("google search", "")
         pywhatkit.search(query)
     elif 'what' in query:
         speak("Ok sir, this is what i found in google ...")
         query = query.replace("tiger", "")
         query = query.replace("google search", "")
         pywhatkit.search(query)
     elif 'suggest' in query:
         speak("Ok sir, please wait ...")
         query = query.replace("tiger", "")
         query = query.replace("tiger suggest me some", "")
         query = query.replace("can you suggest me some", "")
         pywhatkit.search(query)

     elif 'website' in query:
         speak("Ok sir, opening ...")
         query = query.replace("tiger", "")
         query = query.replace("website", "")
         web1 = query.replace("open","")
         web2 = 'https://www.' + web1 + '.com'
         webbrowser.open(web2)

     elif 'read book' in query:
        Reader()


     elif 'play' in query:
        Music()

     elif 'open facebook' in query:
         openApp()

     elif 'open twitter' in query:
         openApp()

     elif 'open instagram' in query:
         openApp()

     elif 'open form' in query:
         openApp()

     elif 'open map' in query:
         openApp()

     elif 'open drive' in query:
         openApp()

     elif 'open gmail' in query:
         openApp()

     elif 'open youtube' in query:
         openApp()

     elif 'open code' in query:
         openApp()

     elif 'open wordpad' in query:
         openApp()

     elif 'open chrome' in query:
         openApp()

     elif 'send message' in query:
         whatsapp()

     elif 'close chrome' in query:
         closeApp()


     elif 'close code' in query:
         closeApp()


     elif 'anchoring' in query:
         speak("ok sir, thank you for giving me this wonderful opportunity, let me introduce myself first")
         wishMe()
         speak("so, this is my short introduction, so now we are going to start our webinar")
         anchor()
     elif 'next' in query:
         anchor()


     elif 'screenshot' in query:
        k = pyautogui.screenshot()
        k.save

     elif 'joke' in query:
         speak("ok, This is a very funny joke for you, hope you will enjoy..")
         speak(pyjokes.get_joke())

     elif 'video' in query:
        speak("Ok sir, Playing Video...")
        music_dir = 'E:\\Videos\\Others\\learning videos for kids'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[5]))

     elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

     elif 'open aap' in query:
        openApp()

     elif 'dictionary' in query:
         Dict()

     
     elif 'exit' in query:
      speak("Ok sir, thank you, have a nice day, bye...")
      exit()
      break