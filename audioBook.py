import pyttsx3
import PyPDF2
from os import system, name
from time import sleep
from Settings import Settings 
import os

# Getting list of all pdfs from current directory #
#---------------------------------------------------#
allFiles = os.listdir('.') 

audioBooks = []

for file in allFiles:
    if file[-4:] == '.pdf':
        audioBooks.append(file)
#---------------------------------------------------#

engine = pyttsx3.init()

def clearCMD(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

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

def chooseAudioBooks():
    c = 1
    while c == 1:
        clearCMD()
        i = 0

        print('AudioBook', end='\n\n')
        print('Choose a book: ')
        print('q: Return to Home Screen')
        for book in audioBooks:
            print(str(i)+': '+book)
            i = i+1

        print('Enter the S.no of book')
        a = input()

        if a.isnumeric():
            a = int(a)
            if a<i:
                playAudioBook(audioBooks[a])
            else:
                print('Invalid S.no')
        elif a == 'q' or a == 'Q':
            c = 0
            continue
        else:
            print('Invalid S.no')

        sleep(1)
