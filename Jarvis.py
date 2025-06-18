import speech_recognition as sr
import pyttsx3
import webbrowser
import socket
import time

def wait_for_internet(timeout=30):
    start = time.time()
    while time.time() - start < timeout:
        try:
            socket.create_connection(("www.google.com", 80), 2)
            return True
        except OSError:
            time.sleep(2)
    return False

# Wait for internet before continuing
wait_for_internet()

# Setup text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("Welcome master Devansh")
engine.runAndWait()

# Start assistant loop
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Just call me if you need anything...")
        try:
            audio = r.listen(source)
            speech = r.recognize_google(audio).lower()
        except sr.UnknownValueError:
            print("Could not understand you.")
            continue
        except sr.RequestError as e:
            print(f"API error: {e}")
            continue

    if speech == "jarvis":
        engine.say("Yes master Devansh")
        engine.runAndWait()
        with sr.Microphone() as source:
            print("What's your order?")
            audio = r.listen(source)
        try:
            task = r.recognize_google(audio).lower()
            match task:
                case "open google":
                    webbrowser.open("https://www.google.com")
                case "open youtube":
                    webbrowser.open("https://www.youtube.com")
                case _:
                    engine.say("Sorry, I can't do that yet.")
            engine.say("There you go sir")
            engine.runAndWait()
        except sr.UnknownValueError:
            print("Didn't catch that.")
        except sr.RequestError as e:
            print(f"API Error: {e}")
