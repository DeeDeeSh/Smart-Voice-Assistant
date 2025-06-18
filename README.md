# 🧠 Jarvis - Voice Activated Assistant

Jarvis is a simple voice-controlled assistant built with Python. It listens for the keyword **"Jarvis"** and responds to basic voice commands like opening Google or YouTube. Designed as a beginner-friendly voice automation project.

---

## 🎯 Features

- ✅ Wake word detection: `"Jarvis"`
- 🗣️ Voice feedback using `pyttsx3`
- 🌐 Command execution (e.g., open websites)
- 🔌 Waits for internet connection before starting
- 🧠 Handles errors like API failures or unrecognized speech
- 🎙️ Uses your system microphone

---

## 📦 Requirements

Install dependencies using:
pip install SpeechRecognition pyttsx3 pyaudio

⚠️ If pyaudio gives an error, on Windows you can use:
pip install pipwin
pipwin install pyaudio

🚀 How to Run
Clone the repository:
git clone https://github.com/yourusername/jarvis-assistant.git
cd jarvis-assistant

Run the assistant:
python jarvis.py

🎤 Voice Commands You Can Use
After saying "Jarvis", try saying:

🟢 "Open Google" → Opens Google in your default browser

🟢 "Open YouTube" → Opens YouTube in your browser

🔴 Anything else → You’ll get a polite “Sorry, I can't do that yet.”

🔧 How It Works
Uses speech_recognition to capture audio and recognize speech

Checks for internet connection before starting using socket

Responds with text-to-speech using pyttsx3

Executes web commands via the webbrowser module

💡 Future Improvements
🗓️ Add reminder & alarm functionality

🔍 Voice-based Google search

🎵 Play music via voice commands

🤖 Add offline recognition support (like Vosk or Whisper)

🪟 Create a GUI with Tkinter or PyQt

🛠️ Startup Automation (Optional)
To run Jarvis on startup:

Create a .bat file with the following content:
@echo off
cd /d "C:\Path\To\Your\jarvis-assistant"
python jarvis.py

Place the .bat file in:
C:\Users\<YourUsername>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

AUTHOR
Devansh Sharma
"Just a guy trying to build cool stuff"
