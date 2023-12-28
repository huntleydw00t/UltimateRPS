#Possible Imports
import os
import time
import urpsPlay
from classes import color
#Variables

#Code -->

def menu_sel(choice):
    
    if choice == "1":
        #Start the game by calling on the urpsPlay.main_game()
        #time.sleep(1)
        os.system('cls')
        theChoice = input("Insert Game Choice (1 - Normal Game, 2 - Insult Version): ")
        urpsPlay.main_game(theChoice)
        return True
    #elif choice == "2":
        #This will come but a lot more development needed.
        #print("Coming Soon to a digital device near you")
        #print("")
        #input("Press Enter to return to the main menu")
        #return True
    elif choice == "2":
        #Simple about menu
        os.system('cls')
        print(color.GREEN + "Ultimate Rock, Paper, Scissors" + color.RESET)
        print(color.RED + "==============================" + color.RESET)
        print("")
        print(color.YELLOW + "Created by: " + color.RESET, color.BLUE + "  Donald J. Huntley" + color.RESET)
        print(color.YELLOW + "Company: " + color.RESET, color.BLUE + "     HuntleyWeb Technologies" + color.RESET)
        print(color.YELLOW + "Email: " + color.RESET, color.BLUE + "       ops@huntleyweb.com")
        print(color.YELLOW + "Date Created: " + color.RESET, color.BLUE + "6/8/2023" + color.RESET)
        print(color.YELLOW + "Version: " + color.RESET, color.BLUE + "     0.0.2" + color.RESET)
        print("")
        input(color.GREEN + "Press Enter to return to main menu" + color.RESET)
        return True
    elif choice == "3":
        #Give instructions on playing game (Well Duh)
        os.system("cls")
        print(color.GREEN + color.UNDERLINE + "How to Play" + color.RESET)
        print(color. YELLOW + "In game you will be given 3 Choices you must Spell out your Choices (ex. Rock or Paper) then hit enter")
        print("The game will translate that and show you the outcome of the round")
        print("If you wish to quit at anytime you may type 'Quit' " + color.RESET)
        print("")
        input(color.GREEN + "Press Enter to return to the main menu" + color.RESET)
        return True
    elif choice == "Q":
        #Simple quit command.  Lets clear the screen then say our goodbye
        #then we will return false to break the while loop in URPS.py
        os.system("cls")
        input("Rock on see you later.  Press Enter to quit.")
        return False

    #<-- Code