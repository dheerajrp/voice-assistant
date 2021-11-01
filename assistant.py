import datetime
import os
import webbrowser

import pyttsx3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    '''speaks the audio which is given as input'''
    engine.say(audio)
    engine.runAndWait()


def greet():
    '''to greet according the time of the day'''
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak('Good Morning Dheeraj!')
    elif 12 <= hour < 18:
        speak('Good Afternoon Dheeraj!')
    else:
        speak('Good Evening Dheeraj!')

    speak('I am Jarvis, your personal assistant. How may I help you?')


def listen():
    '''takes microphone input from user and returns string'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.operation_timeout = 5
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        return query
    except:
        speak('Say that again please')
        query = ''
        return query


if __name__ == '__main__':
    greet()
    while True:
        query = listen().lower()

        if 'search for' in query:
            speak('Searching in wikipedia...')
            # query = query.replace('wikipedia', '')
            # results = wikipedia.summary(query, sentences=1)
            speak(f'According to wikipedia, {wikipedia.summary(query, sentences=2)}')

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime('%H:%M')
            speak(f'The time is {strtime}')

        elif 'open pycharm' in query:
            path = r"C:\Program Files\JetBrains\PyCharm Community Edition 2021.2.3\bin\pycharm64.exe"
            os.startfile(path)

        elif 'thanks' in query:
            speak('No problem.')

        elif 'quit' or 'bye' in query:
            speak('see you next time!')
            exit()
