import pyttsx3
import PyPDF2
from os import system, name
from time import sleep
from Settings import Settings 
import os
# import keyboard

# Getting list of all pdfs from current directory #
#---------------------------------------------------#
allFiles = os.listdir('.') 

audioBooks = []

for file in allFiles:
    if file[-4:] == '.pdf':
        fileObject = {
            "name":file,
            "pgno": 0,
            "lineno":0
        }
        audioBooks.append(fileObject)
#---------------------------------------------------#

engine = pyttsx3.init()

def clearCMD(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

def playAudioBook(abook, index):
    skip = 0

    book = open(abook['name'],'rb')

    pdf_reader = PyPDF2.PdfFileReader(book)

    num_pages = pdf_reader.numPages

    print('Playing Audiobook')
    engine.say('Playing Audiobook Now.')
    engine.runAndWait() 

    sleep(1)

    for num in range(abook['pgno'],num_pages):
        # if keyboard.read_key() == "p":
        #     print("Paused")
        #     skip = 1
        #     audioBooks[index]['pgno'] = num
        #     break
        # else:
        page = pdf_reader.getPage(num)
        data= page.extractText()
        engine.say(data)
        engine.runAndWait()  

    sleep(1)
    if skip == 0:
        print('Audiobook has ended')
        engine.say('Audiobook has ended')
        engine.runAndWait() 

def chooseAudioBooks():
    c = 1
    while c == 1:
        clearCMD()
        i = 0

        print('AudioBook', end='\n\n')
        print('Choose a book: ')
        print('q: Return to Home Screen')
        for book in audioBooks:
            print(str(i)+': '+book['name']+', last stopped at Pgno = '+str(book['pgno']))
            i = i+1

        print('Enter the S.no of book')
        a = input()

        if a.isnumeric():
            a = int(a)
            if a<i:
                playAudioBook(audioBooks[a],a)
            else:
                print('Invalid S.no')
        elif a == 'q' or a == 'Q':
            c = 0
            continue
        else:
            print('Invalid S.no')

        sleep(1)
