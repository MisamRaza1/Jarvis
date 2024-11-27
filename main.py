import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import google.generativeai as genai
from secrets import GoogleApi

recognizer = sr.Recognizer()
engine = pyttsx3.init()
API_KEY ="Your_Api_Key"


def speak(text,speed):
    engine = pyttsx3.init()
    engine.setProperty('rate', speed)  # Default rate is around 200, decrease this for slower speed
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = genai.configure(api_key=GoogleApi)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(command)
    speak(response.text,180)

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https:/google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https:/youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https:/linkedin.com")
    elif "open amazon" in c.lower():
        webbrowser.open("https:/amazon.in")
    elif "open facebook" in c.lower():
        webbrowser.open("https:/facebook.com")
    elif "open flipkart" in c.lower():
        webbrowser.open("https:/flipkart.com")
    elif "open jiocinema" in c.lower():
        webbrowser.open("https:/jiocinema.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}")
        if(r.status_code == 200):
            data = r.json()

            articles = data.get('articles',[])

            for article in articles:
                speak(article['title'],180)
    else:
         aiProcess(c)
        


if __name__ == "__main__":
    
    speak("Initializing Jarvis....",180)

    while(True):
        r = sr.Recognizer()

        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)
            word = r.recognize_google(audio)
            if(word.lower()=='jarvis'):
                speak("yes boss",180)

                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error;{0}".format(e))

            
