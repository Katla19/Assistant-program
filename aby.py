import pyttsx3 #pip install pyttsx3 (For Speak)
import datetime 
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui (For Screenshot)
import psutil #pip install pustil
import pyjokes #pip install pyjokes
import random
import winreg as reg
import operator
import json
import wolframalpha
from urllib.request import urlopen
import requests
import time
import pywhatkit as kit

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("time")
    speak(Time)
def date():
    year = datetime.datetime.now().year
    month=datetime.datetime.now().month
    datetime_object = datetime.datetime.strptime(str(month), "%m")
    month_name = datetime_object.strftime("%B")
    date=datetime.datetime.now().day
    speak("today's date")
    date=str(date)+str(month_name)+str(year)
    speak(date)
def wishme():
    speak("Welcome")
    date()
    time_()
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    elif hour>=18 and hour<24:
        speak("good evening")
    else:
        speak("good night")
    speak("call pie whenever any help needed ..")

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=2)
        audio=r.listen(source)
    try:
        query=r.recognize_google(audio,language='en-US')
    except Exception as e:
        return("None")
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail 
    server.login('Your email', 'Your password')
    server.sendmail('Your email', to, content)
    server.close()
def screenshot():
    img = pyautogui.screenshot()
    img.save("path to save image")
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
def jokes():
    speak(pyjokes.get_joke())

def Introduction():
    speak("I am v a , Personal virtual assistant , "
    "I can help you in various regards , "
    "I can search for you on the Internet , "
    "I can also grab definitions for you from wikipedia , ")

def region(l):
        speak("what is the command")
        query = TakeCommand().lower()

        if 'time' in query:
            time_()
            return none
        elif 'date' in query:
            date()
            return none
        elif 'how are you' in query:
            speak("I am fine, Sir Thanks for asking")
            speak("How are you Sir?")
            aquery=TakeCommand().lower()
            if 'fine' in aquery or "good" in aquery: 
                speak("It's good to know that your fine")
            else:
                speak("I hope you get well soon.")
            return none
        elif 'wikipedia' in query:
            for i in range(3):
                speak("What should I search in wikipedia?")
                Search_term = TakeCommand().lower()
                if Search_term in "none":
                    time.sleep(2)
                else:
                    result = wikipedia.summary(Search_term, sentences=2)
                    speak("According to Wikipedia")
                    speak(result)
            return none
        
        elif 'youtube' in query:
            for i in range(3):
                speak("What should I search in youtube?")
                Search_term = TakeCommand().lower()
                if Search_term in "none":
                    time.sleep(2)
                else:
                    speak("Here we go to Youtube\n")
                    wb.open("https://www.youtube.com/results?search_query="+Search_term)
            return none
        elif 'search' in query:
            for i in range(3):
                speak("What should I search?")
                Search_term = TakeCommand().lower()
                if Search_term in "none":
                    time.sleep(2)
                else:
                    speak("Here we go to Youtube\n")
                    wb.open('https://www.google.com/search?q='+Search_term)
            return none
        elif "who am i" in query:
            speak("If you can talk, then definitely you are a human")
            return none
        elif "why you came to this world" in query:
            speak("it is a secret")
            return none
        elif 'word' in query:
            speak("opening MS Word")
            os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/word.exe")
            return none
        elif 'what is love' and 'tell me about love' in query:
            speak("It is 7th sense that destroy all other senses , "
            "And I think it is just a mere illusion , "
            "It is waste of time")
            return none
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled") 
            return none
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = TakeCommand()
                speak("Who is the Reciever?")
                reciept = input("Enter recieptant's name: ")
                to = (reciept)
                sendEmail(to,content)
                speak(content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Unable to send the email.")
            return none       
        elif 'log out' in query:
            os.system("shutdown -l")
            return none
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
            return none
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
            return none
        
        elif 'remember that' in query:
            speak("What should I remember ?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()
            return none

        elif 'do you remember anything' in query:
            remember =open('memory.txt', 'r')
            speak("You asked me to remeber that"+remember.read())
            return none
        
        
        elif "write a note" in query:
            speak("What should i write, sir")
            note = TakeCommand()
            file = open('note.txt', 'w')
            speak("Sir, Should i include date and time")
            dt = TakeCommand()
            if 'yes' in dt or 'sure' in dt:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak('done')
            else:
                file.write(note)
            return none
                
        elif "show note" in query:
            speak("Showing Notes")
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read()) 
            return none
        elif "weather" in query: 
			
			# Google Open weather website 
			# to get API of Open weather
            api_key = "open weather api"
            base_url = "http://api.openweathermap.org/data /2.5/weather?q="
            speak(" City name ")
            print("City name : ")
            city_name = TakeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()
            
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
                
            else:
                speak(" City Not Found ") 
            return none


        elif 'news' in query:
            
            try:

                jsonObj = urlopen('''news api link''')
                data = json.load(jsonObj)
                i = 1
                
                speak('here are some top news from the times of india')
                print('''=============== TOP HEADLINES ============'''+ '\n')
                
                for item in data['articles']:
                    
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
                    
            except Exception as e:
                print(str(e)) 
            return none

                
        
        elif 'take screenshot' in query:
            screenshot()
            speak("Done!")    
            return none
        elif 'cpu' in query:
            cpu()
            return none
        elif 'joke' in query:
            jokes()
            return none
        elif 'tell me about yourself' and 'who are you' in query:
            Introduction()
            return none
        elif 'tell me about mac' and 'creator' in query:
            Creator()
            return none
        
        #show location on map
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + "")
            return none

        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")
            return none
            
        elif "i love you" in query:
            speak("It's hard to understand, I am still trying to figure this out.")
            return none
        

        #calculation
        elif "calculate" in query:
            
            app_id = "wolfram alpha api"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer) 
            return none
        



        #General Questions
        elif "what is" in query or "who is" in query: 
			
			# Use the same API key 
			# that we have generated earlier
            client = wolframalpha.Client("wolfram alpha api")
            res = client.query(query)
            
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results") 
            return none




        #sleep-time
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much seconds you want me to stop listening commands")
            a = int(TakeCommand())
            time.sleep(a)
            print(a)
            return none

        #quit
        elif 'offline' in query:
            speak("going Offline")
            quit()
            return none
        elif 'none' in query:
            speak("it was not clear")
            region(l+1)
            return none
        query="0"
        print(l)

        if l>3:
            return none
        else:
            region(l+1)

def addregistry():
    pth = os.path.dirname(os.path.realpath("desktop"))
    s_name="pie.py"    
    address=os.path.join(pth,s_name)
    key = "HKEY_CURRENT_USER"
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"


    
if __name__ == '__main__':

    try:
        f = open("filename.txt")
        f.close()
    except IOError:
        addregistry()
    clear = lambda: os.system('cls') 
    clear()
    wishme()
    while True:
        r=sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=2)
            audio=r.listen(source)
        try:
            query=r.recognize_google(audio,language='en-US')   
            print(query)
            if 'ab' in query:
                region(0) 
                query="0"
            elif 'offline' in query:
                speak("going Offline")
                quit()
            else:
                continue
        except Exception as e:
            print("\n")
            continue
