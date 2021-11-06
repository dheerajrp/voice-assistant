import datetime
import os
import random
import sys
import webbrowser

import pyttsx3
import pywhatkit as kit
import speech_recognition as sr
import wikipedia

from Decorators import decorate

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak_print(audio):
    '''speaks the audio which is given as input and prints it'''
    print(f'Jarvis: {audio}')
    engine.say(audio)
    engine.runAndWait()


@decorate
def greet():
    '''to greet according the time of the day'''
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak_print('Good Morning!')
    elif 12 <= hour < 18:
        speak_print('Good Afternoon!')
    else:
        speak_print('Good Evening!')

    speak_print('I am Jarvis, your personal assistant. How may I help you?')


def listen():
    '''takes microphone input from user and returns string'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            print(f'You: {query}')
            return query
        except:
            speak_print('Say that again please')
            query = ''
            return query


if __name__ == '__main__':
    greet()
    greet_words = ['hi', 'hai', 'hello', 'morning', 'afternoon', 'evening', 'good morning',
                   'good afternoon', 'good evening']
    while True:
        query = listen().lower()

        if 'wikipedia' in query:
            speak_print('Searching in wikipedia...')
            query = query.replace('wikipedia', '')
            speak_print(f'According to wikipedia, {wikipedia.summary(query, sentences=2)}')

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime('%H:%M')
            speak_print(f'The time is {strtime}')

        elif 'open pycharm' in query:
            path = r"C:\Program Files\JetBrains\PyCharm Community Edition 2021.2.3\bin\pycharm64.exe"
            os.startfile(path)

        elif 'your name' in query:
            speak_print('I am Jarvis, your personal assistant.')

        elif str(query) in greet_words:
            speak_print('Hello. How may I help you today?')

        elif 'developed' in query:
            speak_print('I am developed with love by Dheeraj.')

        elif 'thanks' in query:
            speak_print('No problem.')

        elif 'news' in query:
            webbrowser.open("https://timesofindia.indiatimes.com/home/headlines")
            speak_print('Here are some headlines from the Times of India,Happy reading')

        elif 'open youtube' in query:
            speak_print('opening youtube')
            webbrowser.open_new_tab('www.youtube.com')


        elif 'open command prompt' in query:
            speak_print('opening command prompt')
            os.system('start cmd')

        elif 'play any song' in query:
            speak_print('Do you have any specific song you want to hear?')
            song = listen()
            if song == 'yes' or 'yea':
                speak_print('Which song?')
                choice = listen()
                speak_print(f'playing {choice} from youtube..')
                kit.playonyt(choice)
                sys.exit()
            if song == 'no' or 'nope':
                genres = ['romantic', 'pop', 'classical', 'happy', 'calm', 'emotional', 'festive', 'jazz', 'blues',
                          'melody', 'lofi', 'opera', 'instrumental', 'senti']
                speak_print('Playing a song. Hold on...')
                random_genre = random.choice(genres)
                print(random_genre)
                kit.playonyt(random_genre)
                sys.exit()

        elif 'open my library' in query:
            speak_print('Opening your library..')
            lib_path = r'C:\Users\dheer\Desktop\ml_dl_books'
            content = os.listdir(lib_path)
            os.startfile(lib_path)
            sys.exit()

        elif 'exit' in query:
            speak_print('see you next time!Bye')
            sys.exit()

        else:
            speak_print('I am not sure how to answer that.')
