import pyttsx3
from os import system, name
from time import sleep

engine = pyttsx3.init()

voices = engine.getProperty('voices')
male_voice = voices[0].id
female_voice = voices[1].id

initialSpeed = engine.getProperty('rate')

initialVolume = engine.getProperty('volume')

def clearCMD(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def changeVoice(gender):
    if gender == 'male':
        engine.setProperty('voice', male_voice)
    else:
        engine.setProperty('voice', female_voice)
    print('Voice changed to '+gender+' successfully')
    engine.say('Voice changed to '+gender+' successfully')
    engine.runAndWait()

def changeRate(val):
    engine.setProperty('rate', initialSpeed*val)
    print('The quick brown fox jumped over the lazy dog.')
    engine.say('The quick brown fox jumped over the lazy dog.')
    engine.runAndWait()

def changeVolume(val):
    engine.setProperty('volume', initialVolume*val)
    print('The quick brown fox jumped over the lazy dog.')
    engine.say('The quick brown fox jumped over the lazy dog.')
    engine.runAndWait()

def Settings():
    c = 1
    while c == 1:
        clearCMD()
        print('Settings', end='\n\n')
        print('Choose an option:')
        print('q: Return to Home Screen')
        print('s: change voice')
        print('r: change speech rate')
        print('v: change volume')

        a = input()

        if a == 's' or a == 'S':
            print('\n1: change voice to male')
            print('2: change voice to female')
            val = input()
            if val == '1':
                changeVoice('male')
                continue
            elif val == '2':
                changeVoice('female')
                continue
            else:
                print('Invalid Option')
        elif a == 'r' or a == 'R':
            print('\nEnter rate (for example, if you want 2X speed, enter 2): ',end='')
            val = input()
            if val.isnumeric():
                val = int(val)
                changeRate(val)
            else:
                print('Invalid Rate value')
        elif a == 'v' or a == 'V':
            print('\nEnter Volume in % (0-100): ',end='')
            val = input()
            if val.isnumeric():
                val = int(val)/100
                changeVolume(val)
            else:
                print('Invalid Volume % value')
        elif a == 'q' or a == 'Q':
            c = 0
            continue
        else:
            print('Invalid option')

        sleep(1)