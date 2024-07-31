import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
recognizer= sr.Recognizer()
engine=pyttsx3.init()
newsapi="b05caccc0d654582983dd85d0e2a0f09"


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        musiclibrary.music[song]
        link=musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=b05caccc0d654582983dd85d0e2a0f09")
        if r.status_code == 200:
            data = r.json()
            headlines = [article['title'] for article in data['articles']]
            for i, headline in enumerate(headlines, 1):
                speak(f"{i}. {headline}")
    else:
        #let open openai
        pass

if __name__=="__main__":
    speak("Initializing Jarvis......")

    # listen for the wake word "Jarvis"
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
        print("recognition....")
        
        try:
            with sr.Microphone() as source:
                print("listening")
                audio = r.listen(source, timeout=3,phrase_time_limit=3)

        # recognize speech using Sphinx
            print("Google thinks you said " + r.recognize_google(audio))
            word=r.recognize_google(audio)
            if (word.lower()=="jarvis"):
                speak("ya")


                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis active....")
                    audio = r.listen(source)
            
                    command= word=r.recognize_google(audio)
                    processcommand(command)


        except Exception as e:
            print(" error; {0}".format(e))


