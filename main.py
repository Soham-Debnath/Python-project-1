import speech_recognition as sr
import webbrowser
import pyttsx3 
import musicLibrary
import requests

# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "21c82720174445c59003ff48fb48dfe3"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google...")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        speak("Opening Youtube...")
        webbrowser.open("https://www.youtube.com")
    elif "open twitter" in c.lower():
        speak("Opening twitter...")
        webbrowser.open("https://www.twitter.com")
    elif "open facebook" in c.lower():
        speak("Opening Facebook...")
        webbrowser.open("https://www.facebook.com")
    elif "open linkedin" in c.lower():
        speak("Opening Linkedin...")
        webbrowser.open("https://www.linkedin.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        speak("Playing "+song)
        link= musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        speak("Here are the top headlines from India")
        webbrowser.open("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")
        # need to work more on this
        # r = requests.get(f"http://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        # if r.status_code == 200:
           
        #     data = r.json()
            
        #     articles = data.get('articles',[])
            
            
        #     for article in articles:
        #         print(article['title'])
        #         # speak(article['title'])

if __name__ == "__main__":
    speak("initializing jarvis...")
    while True:

        #  Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=5,phrase_time_limit=3)

            word = r.recognize_google(audio)
            if(word.lower()== "jarvis"):
                speak("Yes, I'm listening...")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
           print("Error; {0}".format(e))

