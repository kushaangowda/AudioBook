import pyttsx3
import PyPDF2
from os import system, name
from time import sleep

engine = pyttsx3.init()

voices = engine.getProperty('voices')
male_voice = voices[0].id
female_voice = voices[1].id

def clear(): 
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

def playAudioBook(name):
    book = open(name,'rb')

    pdf_reader = PyPDF2.PdfFileReader(book)

    num_pages = pdf_reader.numPages

    print('Playing Audiobook')
    engine.say('Playing Audiobook Now.')
    engine.runAndWait() 

    sleep(1)

    for num in range(0,num_pages):
        page = pdf_reader.getPage(num)
        data= page.extractText()
        engine.say(data)
        engine.runAndWait()  

    sleep(1)

    print('Audiobook has ended')
    engine.say('Audiobook has ended')
    engine.runAndWait() 

def runMain():
    c = 1
    while c == 1:
        print('Choose one among the following: ')
        print('1: change voice to male')
        print('2: change voice to female')
        print('3: play audiobook')
        print('q: to quit')
        a = input()

        if a == '1':
            changeVoice('male')
        elif a == '2':
            changeVoice('female')
        elif a == '3':
            playAudioBook('sample.pdf')
        elif a == 'q' or a == 'Q':
            c = 0
            print('Ending Application')
        else:
            print('Invalid Input')
        sleep(1)
        clear()

runMain()