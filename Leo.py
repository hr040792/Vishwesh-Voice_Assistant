import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import site
import random

sound = pyttsx3.init('sapi5')
voices = sound.getProperty('voices')
sound.setProperty('voice', voices[1].id)


def speak(audio):
    sound.say(audio)
    sound.runAndWait()


def wish():    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning, Have a nice day!")
        speak("Good Morning, Have a nice day!")
    elif hour>=12 and hour<18:
        print("Good Afternoon!")   
        speak("Good Afternoon!")   
    else:
        print("Good Evening!")  
        speak("Good Evening!")  
        
    print("I am Leo How may I help you!")       
    speak("I am Leo How may I help you!")       

def takeCommand():
    tc = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n")
        print("Hearing____")
        tc.pause_threshold = 1
        audio = tc.listen(source)

    try:
        print("\n")
        print("Recognizing____")    
        query = tc.recognize_google(audio, language='en-in')
        print("\n")
        print(f"User said: {query}\n")
        speak(f"You said {query}\n")
        print(f"You said {query}\n")

    except Exception as e:  
        print("\n")
        print("Can you please recall once again...") 
        speak("Can you please recall once again")
        
        return "None"
    return query






if __name__=="__main__" :
    wish()
    
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching in wikipedia wait a moment')
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)
            speak("Thankyou for using")
            

        
        elif'calculate' in query:
            print("Ofcourse, Provide your equation")
            speak("Ofcourse, Provide your equation")
            print('Calculating.....................?')
            speak('Calculating')
            equation = takeCommand().lower()
            try:
                result = eval(equation)
                print(f"Answer of {equation} is {result}")
                speak(f"Answer of {equation} is {result}")
            except Exception as e:
                print("I couldn't understand.")
                speak("I couldn't understand.")
            
            
        
        elif 'time'in  query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Vishwesh,The current time is {strTime}")
        
        elif'hello'in query:
            speak("Hello!")
        elif'what is your name'in query:
            speak("My name is Leo")
        elif'thank you'in query:
            speak("Mention not.")
        elif'who is your developer'in query:
            speak("Vishwesh kumar sinha")
        
        
        
        elif'play music'in query:
            music_dir='C:\\Users\\hr040\\Music\\song'
            songs =os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            random.shuffle(songs)
        elif 'play video'in query:
            video_dir='C:\\Users\\hr040\\Videos\\Video'
            videopath=os.listdir(video_dir)
            print(videopath)
            os.startfile(os.path.join(video_dir,videopath[0]))
        
        
        elif 'open dev'in query:
            devpath="C:\\Program Files (x86)\\Embarcadero\\Dev-Cpp\\devcpp.exe"
            os.startfile(devpath)
        elif'open google chrome'in query:
            chromepath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)
        elif'open winrar'in query:
            rarpath="C:\\Program Files\\WinRAR\\WinRAR.exe"
            os.startfile(rarpath)
        
        
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif'open google'in query:
            webbrowser.open("google.com")
        elif'open facebook'in query:
            webbrowser.open("facebook.com")
        elif'open yahoo' in query:
            webbrowser.open("yahoo.com")
        elif'open instagram'in query:
            webbrowser.open("instagram.com")
        elif'whatsapp'in query:
            webbrowser.open("whatsappweb.com")
        elif'open netflix'in query:
            webbrowser.open("netflix.com")
        elif'open hotstar'in query:
            webbrowser.open("hotstar.com")
        elif'open amazon'in query:
            webbrowser.open("amazon.com")
        elif'open Flipkart'in query:
            webbrowser.open("flipkart.com")
        elif'play song on youtube'in query:
            webbrowser.open("https://www.youtube.com//watch?v=3SxE7So2ueU")
        elif'play codewithharry on youtube'in query:
            webbrowser.open("https://www.youtube.com/watch?v=7Dh73z3icd8&list=PLu0W_9lII9aiXlHcLx-mDH1Qul38wD3aR&index=1")
        elif 'open online coding'in query:
            webbrowser.open("https://ide.codingblocks.com/")
                
        
        
        elif'shutdown' in query:
            speak("Thankyou for using me Good Bye")
            quit()
            
