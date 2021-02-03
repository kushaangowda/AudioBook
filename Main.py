from os import system, name
from time import sleep
from Settings import Settings
from AudioBook import chooseAudioBooks

def clearCMD(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def runMain():
    c = 1

    while c == 1:
        clearCMD()
        print('Home', end='\n\n')
        print('Choose one among the following: ')
        print('a: Choose audiobook')
        print('s: Settings')
        print('q: quit')
        a = input()
        
        if a == 'a' or a == 'A':
            chooseAudioBooks()
        elif a == 's' or a == 'S':
            Settings()
        elif a == 'q' or a == 'Q':
            c = 0
            print('Ending Application')
        else:
            print('Invalid Input')

        sleep(1)

runMain()