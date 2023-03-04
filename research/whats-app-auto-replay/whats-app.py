import pywhatkit as pwk
import pyautogui as spam
import time
import pip
import speech_recognition as sr
import webbrowser
import smtplib
import random
import wikipedia
import datetime
import wolframalpha
import os
import sys
import subprocess
import pyttsx3


engine = pyttsx3.init()

'''len(voices)-1'''
client = wolframalpha.Client(' IL 61820-7237, USA')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('shofee : ' + audio)
    engine.say(audio)
    engine.runAndWait()

speak('hi sir how are you?')

#iterating through the contact list
for index,name in contacts:
    try:
        click_search_name(heshikan)
    except:
        print("Unable to locate search bar or name")

    try:
        click_send_message(hello)
    except:
        print("Unable to locate message bar")

