from http import client
import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary
import requests 
from openai import OpenAI
from gtts import gTTS
import pygame

recogniser = sr.Recognizer()
engine = pyttsx3.init()
newsapi="yo dont even think imma give u my api "


def speak(text):
    engine.say(text)
    engine.runAndWait()

#def speak(text):
  #  tts=gTTS(text=text, lang='en')
   # tts.save("temp.mp3")
    
    #pygame.mixer.init()
    #pygame.mixer.music.load("temp.mp3")
    #pygame.mixer.music.play()

    #while pygame.mixer.music.get_busy():
     #   pygame.time.Clock().tick(10)

def aiprocess(command):
    client = OpenAI(
        api_key="im not gonna give u m api key bleh"
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant, called Jarvis skilled in general tasks like Alexa and Google Assistant."},
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    if c is None:
        return

    command = c.lower().strip()
    if "google" in command and ("open" in command or "launch" in command or "go to" in command):
        webbrowser.open("https://www.google.com")
    elif "youtube" in command and ("open" in command or "launch" in command or "go to" in command):
        webbrowser.open("https://www.youtube.com")
    elif "instagram" in command and ("open" in command or "launch" in command or "go to" in command):
        webbrowser.open("https://www.instagram.com")
    elif "github" in command and ("open" in command or "launch" in command or "go to" in command):
        webbrowser.open("https://github.com/aceholland")
    elif "chatgpt" in command and ("open" in command or "launch" in command or "go to" in command):
        webbrowser.open("https://chat.openai.com/")
    elif "gemini" in command and ("open" in command or "launch" in command or "go to" in command):
        webbrowser.open("https://gemini.com/")
    elif "gmail" in command and ("open" in command or "launch" in command or "go to" in command):
        webbrowser.open("https://mail.google.com/")
    elif "whatsapp" in command and ("open" in command or "launch" in command or "go to" in command):
        webbrowser.open("https://web.whatsapp.com/")
    elif c.lower().startswith("play"):
        song=c.lower().split(" " )[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=newsapi")
        if r.status_code==200:
            data=r.json()
            articles=data.get('articles', [])
            for article in articles:
                speak(article['title'])

    else :
        #let open ai handle the request 
        output =aiprocess(c)
        speak(output)





if __name__ == "__main__":
    speak("Initializing Jarvis")
    while True:
        try:
            print("Recognizing...")
            with sr.Microphone() as source:
                print("Listening")
                recogniser.adjust_for_ambient_noise(source, duration=0.5)
                audio = recogniser.listen(source, timeout=5, phrase_time_limit=5)

            word = recogniser.recognize_google(audio, language="en-in")
            print("You said:", word)

            if "jarvis" in word.lower():
                speak("Yes")
                with sr.Microphone() as source:
                    print("Jarvis activated")
                    recogniser.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recogniser.listen(source, timeout=8, phrase_time_limit=8)
                command = recogniser.recognize_google(audio, language="en-in")
                print("Command:", command)
                processCommand(command)

        except sr.UnknownValueError:
            print("No speech detected or the speech was unclear.")
        except sr.RequestError as e:
            print(f"Google speech recognition request failed: {e}")
        except Exception as e:
            print(f"Speech error: {e}")
            