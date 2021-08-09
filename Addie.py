import speech_recognition as sr
import pyttsx3
import os
import random
import pyaudio
import datetime
import wikipedia
import webbrowser
import smtplib
import urllib
import re
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import operator
from subprocess import call
import subprocess
import wolframalpha
import json
import requests
from datetime import date
import cv2
import winsound
import pyjokes

engine = pyttsx3.init()# module pyttsx3, pip install pyttsx3 #it can also be used sapi5
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)# voices id, there are 2 voices
# inbuild voice used from windows

########## speak function ##################
def speak(audio):#audio argument hai
    engine.say(audio)
    engine.runAndWait()


def wishMe():

    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    wishList = ["Hello", "Hi", "What's up", "Yo", "Hi There","Hey"]

    speak(random.choice(wishList))
    speak(", I am Addie. Please tell me how can i help you")
    takeCommand()
    # takenameCommand()
    # speak("Hi, I am Addie. What should i call you?")


def date():
    from datetime import date
    today = date.today()
    date1 = today.strftime("%m/%d/%Y")
    print("d1 =", date1)

    speak(f"Today's date is  {date1}")



def bye_greeting():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Bye Miss Paaruul. Happy to help you. Have a good day.")

    elif 12 <= hour < 18:
        speak("Bye Miss Paaruul. Happy to help you. Have a good afternoon.")

    else:
        speak("Bye Miss Paaruul. Happy to help you. Have a good Evening.")

# def takenameCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         # r.pause_threshold = 1
#         audio = r.listen(source, phrase_time_limit=5)
#         try:
#             print("Recognizing...")
#             query = r.recognize_google(audio, language='en-in')
#             speak(f"Hello {query}\n")
#             print(f"User said: {query}\n")
#         except Exception as e:
#             print("Say that again Please...")
#             speak("Say that again please...")
#             return "None"
#         return query


def takeCommand():
    # it takes microphone input from the user and returns string output'
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again Please...")
            speak("Say that again please...")
            return "None"
        return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('emailaddress', 'Password')#your email address
    server.sendmail('emailaddress', to, content)#email address you want to send the email
    server.close()


def get_operator_fn(op):
    return {
        '+': operator.add,  # 3 plus 4
        '-': operator.sub,  # 2 minus 3
        '*': operator.mul,  # 3 multiply 5
        '/': operator.__truediv__,  # 7 divide 3
        'divided': operator.__truediv__,
        'Mod': operator.mod,
        'mod': operator.mod,  # speak 7 mod 2
        '^': operator.xor,  # speak 7 caret 3
    }[op]


def eval_binary_expr(op1, oper, op2):
    op1, op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)


# def note(text):
#     date = datetime.datetime.now()
#     file_name = str(date).replace(":", "-") + "-note.txt"
#     with open(file_name, "w") as f:
#         f.write(text)
#     sublime = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Sublime_Text 3"
#     subprocess.Popen(["notepad.exe", file_name])


# note("tech with parul")


# def eval_binary_expr(op1, oper, op2):
#     op1, op2 = int(op1), int(op2)
#     return get_operator_fn(oper)(op1, op2)


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()
        # logic for executing task based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'find location' in query:
            speak("which location you want to search?")
            query = takeCommand()
            r2 = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                location = r2.listen(source, phrase_time_limit=4)
                get_location = r2.recognize_google(location)
                print(get_location)
                url = 'https://google.nl/maps/place' + get_location + '/&amp;'
                webbrowser.get().open(url)
                speak("Here is the location of " + get_location)
        elif 'who are you' in query or 'what can you do' in query:
            speak('I am Addie version 1 point O, your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow, predict time,take a photo,search wikipedia, predict weather'
                  'in different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'search' in query:
            speak("What do you want to search?")
            print("What do you want to search?")
            query = takeCommand()
            url = 'http://google.com/search?q=' + query
            webbrowser.get().open(url)
            speak("Here is what i found for " + query)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play song' in query:
            speak("Which song would you like to play?")
            print("Which song would you like to play?")
            query = takeCommand()
            url = 'http://www.youtube.com/results'
            song = urllib.parse.urlencode({"search_query": query})
            print(song)

            result = urllib.request.urlopen(url + "?search_query=" + song)
            # print(result.read().decode())

            search_results = re.findall(r'\"url\":\"\/watch\?v=(.{11})', result.read().decode())
            print(search_results)

            url2 = "http://www.youtube.com/watch?v=" + search_results[0]
            webbrowser.open_new(url2)

        elif 'play music' in query:
            music_dir = 'C:\\Users\\parul\\Music\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, The time is  {strTime}")

        # elif 'the date' in query:
        #    date()

        elif "weather" in query:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                celsius_not_float = current_temperature - 273.15
                celsius = "{:.2f}".format(celsius_not_float)
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
                print(" Temperature in celsius unit = " +
                      str(celsius))
                speak(" Temperature in celsius unit is " +
                      str(celsius))

            else:
                speak(" City Not Found ")

        elif 'open code' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.3.1\\bin\\pycharm64.exe"#your own computer path
            os.startfile(codePath)

        elif 'email to parul' in query:
            try:
                speak("Whats should i say?")
                content = takeCommand()
                to = 'emailaddress  '
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry my friend ")

        elif 'decrease volume' in query:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))

            # Get current volume
            currentVolumeDb = volume.GetMasterVolumeLevel()
            volume.SetMasterVolumeLevel(currentVolumeDb - 6.0, None)
            speak("Volume Decreased!!")
            # NOTE: -6.0 dB = half volume !

        elif 'increase volume' in query:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))

            # Get current volume
            currentVolumeDb = volume.GetMasterVolumeLevel()
            volume.SetMasterVolumeLevel(currentVolumeDb + 6.0, None)
            speak("Volume Increased!!")
            # NOTE: +6.0 dB = half volume !

        elif 'mute volume' in query:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))

            # Get current volume
            currentVolumeDb = volume.GetMasterVolumeLevel()
            print(currentVolumeDb)
            volume.SetMasterVolumeLevel(-65.25, None)
            speak("Volume muted!!")
            # NOTE: +6.0 dB = half volume !

        elif 'full volume' in query:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))

            # Get current volume
            currentVolumeDb = volume.GetMasterVolumeLevel()
            volume.SetMasterVolumeLevel(0, None)
            speak("Volume full!!")
            # NOTE: +6.0 dB = half volume !

        elif 'open calculator' in query:
            call(["calc.exe"])

        elif 'calculate' in query:
            speak("Say what you want to calculate, example: 3 plus 3")
            calculate = takeCommand()
            answer = eval_binary_expr(*(calculate.split()))
            print(answer)
            speak("The Answer is ")
            speak(answer)
        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by Miss Paarul")
            print("I was built by Miss Paarul")

        elif 'geographical question' in query:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            print(answer)
            speak(answer)

        elif 'security camera' in query:
            cam = cv2.VideoCapture(0)
            while cam.isOpened():
                ret, frame1 = cam.read()
                ret, frame2 = cam.read()
                diff = cv2.absdiff(frame1, frame2)
                gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
                blur = cv2.GaussianBlur(gray, (5, 5), 0)
                _, thresh = cv2.threshold(blur, 20, 155, cv2.THRESH_BINARY)
                dilated = cv2.dilate(thresh, None, iterations=3)
                contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                # cv2.drawContours(frame1,contours, -1, (0,255,0), 2)
                for c in contours:
                    if cv2.contourArea(c) < 5000:
                        continue

                    x, y, w, h = cv2.boundingRect(c)
                    cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
                if cv2.waitKey(10) == ord('q'):
                    break
                cv2.imshow('Granny Cam', frame1)

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)


        elif "goodbye" in query or "okay bye" in query or "stop" in query or "thank you bye" in query or "bye" in query:
            bye_greeting()
            exit()

        elif "log off" in query or "sign out" in query:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        else:
            speak("Sorry, I do not understand. Please, can you repeat that again?")


