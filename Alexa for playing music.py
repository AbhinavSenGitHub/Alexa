#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import speech_recognition as sr
import pyttsx3
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source, timeout=10)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except sr.UnknownValueError:
        print('Sorry, I did not understand. Please repeat.')
        return "unknown"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "error"
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "error"

    return command

def run_alexa():
    command = take_command()
    print(command)

    if command == "unknown":
        talk("Sorry, I did not understand. Please repeat.")
    elif command == "error":
        talk("An unexpected error occurred. Please try again.")
    elif 'play' in command:
        song = command.replace('play', 'Playing')
        talk(f'Playing {song}')
        pywhatkit.playonyt(song)
    else:
        talk('Please say the command again.')

# Run the assistant
while True:
    run_alexa()

