import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr # pip install speechRecognition
import wikipedia # pip install wikipedia
import webbrowser
import os
import random
import smtplib
import random

# Set Number of Songs in Music Directory
no_of_songs = 0 # Change this value

# Add your emails list here (Use lowercase for names)
people = {"abc":"abc@gmail.com"}

#Set your email and Password for authentication (For Gmail Only)
youremail = "abc@gmail.com"
yourpassword = "abc123"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
#print(voices)

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour in range(0,12):
        speak("Good Morning!")
    elif hour in range(12,18):
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Python Bot, Please tell me what to do...")

def takeCommand():
    ''' It takes Microphone input from user'''
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said {query}\n")
        
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.starttls()
    server.loginttls(yourmail,yourpassword)
    server.sendmail(youremail,to,content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for executing task based on Query

        if 'wikipedia' in query:
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            #print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            music_dir = 'Music'
            songs = os.listdir(music_dir)
            index = random.randint(0,no_of_songs-1)
            os.startfile(os.path.join(music_dir,songs[index]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtime}")
            print(strTime)
        
        elif 'send email' in query:
            sent = False
            try:
                speak("What should I say?")
                content = takeCommand()
                for elem in people.keys():
                    if elem in content:
                        sendEmail(people[elem],content)
                        print("Mail Sent\n")
                        sent = True
                        break
                if not sent:
                    print("Contact not found ")
            except Exception as e:
                speak("Sorry, Can't Send your Email right now")
        
        elif 'exit' in query:
            print("Bye Bye")
            speak("Bye Bye")
            break
