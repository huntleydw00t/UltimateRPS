#Ultimate Rock, Paper, Scissors by HuntleyWeb
#Created By: Donald J. Huntley (HuntleyWeb Founder)
#Email: ops@huntleyweb.com
#Website: www.huntleyweb.com

#Notes
#Build 0.0.2
#Date: 06/08/2023



#Welcome to the Ultimate Rock Paper Scissors
#This program will be broken into many parts so advancements can be made
#Its a simple game with a simple goal, Win.
#There will be many addons and features which will improve upon the game
#Crazy Crazy Shit man


#Imported Libraries
import urpsPlay, urpsMenu
import time
import os
import platform
from classes import color


#Variables -->
menChoice = 0
keepRolling = True
whichOS = platform.system()
#Code -->
#Allow the main menu to keep going until we exit the game by typing "Q"
while keepRolling == True:
    if whichOS == 'Linux':
        os.system('clear')
    elif whichOS == 'Windows':
        os.system('cls')
    print (color.GREEN + color.UNDERLINE + "Welcome to Ultimate Rock Paper Scissors" + color.RESET)
    print("")
    print(color.CYAN + "MAIN MENU" + color.RESET)
    print("")
    print(color.MAGENTA + "1: Play Game")
    #print("2: Play Story")
    print("2: About Info")
    print("3: How to Play")
    print("Q: Quit Game" + color.RESET)
    print("")
    menChoice = input("Please Make a Selection: ")

    keepRolling = urpsMenu.menu_sel(menChoice)
    

    
    

