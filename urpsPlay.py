from random import randint
import time
import os, platform
import sys
import urpsDisplay, urpsInsult
from classes import color

def main_game(gameChoice):
    #This will be our selections for the game actions.  As time progresses more moves will be added to the game
    playTable = ["Rock", "Paper", "Scissors"]
    
    #We will start by giving the computer one of the above three choices randomly
    compHand = playTable[randint(0,2)]
    compHand = compHand.lower()

    #We will create a loop and it will run while player's value is equal to false.
    #I will cleanup the functionality of this later for smoother play
    humPlayer = False
    #gChoice = gameChoice

    #We will also keep score of these games with a score board. (In the future there will be a round duration selection and more)
    playScore = 0
    compScore = 0

    whichOS = platform.system()

    #Lets make this shit work muahahahaha
    #We will begin with a while loop that runs while player variable is equal to false
    while humPlayer == False:
        #This is a selection for insulting or not instulting
        if gameChoice == "1":
            # will print the score board here
            urpsDisplay.score_board(playScore, compScore)

            #Let's begin by asking the player for a choice of what move to make this will also set the humPlayer to True
            humPlayer = input("Rock, Paper or Scissors?")
            humPlayer = humPlayer.lower()

            #Tie Scenario
            if humPlayer == compHand:
                if compHand == "rock":
                    print ("Player: ", "\N{right-facing fist}", ": Computer: ", "\N{left-facing fist}")
                elif compHand == "paper":
                    print ("Player: ", "\N{Raised back of hand}", ": Computer: ", "\N{Raised back of hand}")
                else:
                    print ("Player: ", "\N{victory hand}", ": Computer: ", "\N{victory hand}")
                print(color.GREEN + "Tie! Good Round" + color.RESET)

                #Let's add a point to both players
                playScore = playScore + 1
                compScore = compScore + 1
                humPlayer = False

            #Let's see what happens when our hero chooses Rock
            elif humPlayer == "rock":
                if compHand == "paper":
                    print ("Player: ", "\N{right-facing fist}", ": Computer: ", "\N{Raised back of hand}")
                    print(color.RED + "You Failed! " + color.RESET, compHand, color.RED + " Covers " + color.RESET, humPlayer)
                    compScore = compScore + 1

                else:
                    print("Player: ", "\N{right-facing fist}", ": Computer: ", "\N{victory hand}")
                    print(color.GREEN + "You Win!!!! " + color.RESET, humPlayer, color.GREEN + " smashes " + color.RESET, compHand)
                    playScore = playScore + 1
                humPlayer = False

            elif humPlayer == "paper":
                if compHand == "scissors":
                    print("Player: ", "\N{Raised back of hand}", ": Computer: ", "\N{victory hand}")
                    print(color.RED + "You Failed!! " + color.RESET, compHand, color.RED + " Cut's " + color.RESET, humPlayer)
                    
                    compScore = compScore + 1

                else:
                    print("Player: ", "\N{Raised back of hand}", ": Computer: ", "\N{left-facing fist}")
                    print(color.GREEN + "You Win!! " + color.RESET, humPlayer, color.GREEN + " Covers " + color.RESET, compHand)
                    playScore = playScore + 1

                humPlayer = False

            elif humPlayer == "scissors":
                if compHand == "rock":
                    print("Player: ", "\N{victory hand}", ": Computer: ", "\N{left-facing fist}")
                    print(color.RED + "You Failed!!! " + color.RESET, compHand, color.RED + " Crushes " + color.RESET, humPlayer)
                    
                    compScore = compScore + 1

                else:
                    print("Player: ", "\N{victory hand}", ": Computer: ", "\N{Raised back of hand}")
                    print(color.GREEN + "You Win!!! " + color.RESET, humPlayer, color.GREEN + " Cuts " + color.RESET, compHand)
                    playScore = playScore + 1
                humPlayer = False
        
            elif humPlayer == "quit":
                humPlayer = True

                #Whoops don't know what that was
            else:
                print("Whoa Boy!!! That is not one of your choices!!")
                humPlayer = False
            
        else:
            #Insult Side
            # will print the score board here
            urpsDisplay.score_board(playScore, compScore)

            #Let's begin by asking the player for a choice of what move to make this will also set the humPlayer to True
            humPlayer = input("Rock, Paper or Scissors?")
            humPlayer = humPlayer.lower()

            #Tie Scenario
            if humPlayer == compHand:
                if compHand == "rock":
                    print ("Player: ", "\N{right-facing fist}", ": Computer: ", "\N{left-facing fist}")
                elif compHand == "paper":
                    print ("Player: ", "\N{Raised back of hand}", ": Computer: ", "\N{Raised back of hand}")
                else:
                    print ("Player: ", "\N{victory hand}", ": Computer: ", "\N{victory hand}")
                print(color.GREEN + "Tie! Good Round" + color.RESET)

                #Let's add a point to both players
                playScore = playScore + 1
                compScore = compScore + 1
                humPlayer = False

            #Let's see what happens when our hero chooses Rock
            elif humPlayer == "rock":
                if compHand == "paper":
                    print ("Player: ", "\N{right-facing fist}", ": Computer: ", "\N{Raised back of hand}")
                    print(color.RED + "You Failed! " + color.RESET, compHand, color.RED + " Covers " + color.RESET, humPlayer)
                    print(color.YELLOW + "Judge: ", urpsInsult.judge_insult() + color.RESET)
                    compScore = compScore + 1

                else:
                    print("Player: ", "\N{right-facing fist}", ": Computer: ", "\N{victory hand}")
                    print(color.GREEN + "You Win!!!! " + color.RESET, humPlayer, color.GREEN + " smashes " + color.RESET, compHand)
                    playScore = playScore + 1
                humPlayer = False

            elif humPlayer == "paper":
                if compHand == "scissors":
                    print("Player: ", "\N{Raised back of hand}", ": Computer: ", "\N{victory hand}")
                    print(color.RED + "You Failed!! " + color.RESET, compHand, color.RED + " Cut's " + color.RESET, humPlayer)
                    print(color.YELLOW + "Judge: ", urpsInsult.judge_insult() + color.RESET)
                    compScore = compScore + 1

                else:
                    print("Player: ", "\N{Raised back of hand}", ": Computer: ", "\N{left-facing fist}")
                    print(color.GREEN + "You Win!! " + color.RESET, humPlayer, color.GREEN + " Covers " + color.RESET, compHand)
                    playScore = playScore + 1
                humPlayer = False
            elif humPlayer == "scissors":
                if compHand == "rock":
                    print("Player: ", "\N{victory hand}", ": Computer: ", "\N{left-facing fist}")
                    print(color.RED + "You Failed!!! " + color.RESET, compHand, color.RED + " Crushes " + color.RESET, humPlayer)
                    print(color.YELLOW + "Judge: ", urpsInsult.judge_insult() + color.RESET)
                    compScore = compScore + 1

                else:
                    print("Player: ", "\N{victory hand}", ": Computer: ", "\N{Raised back of hand}")
                    print(color.GREEN + "You Win!!! " + color.RESET, humPlayer, color.GREEN + " Cuts " + color.RESET, compHand)
                    playScore = playScore + 1
                humPlayer = False
        
            elif humPlayer == "quit":
                humPlayer = True

                #Whoops don't know what that was
            else:
                print("Whoa Boy!!! That is not one of your choices!!")
                humPlayer = False

            

        #humPlayer = False
        time.sleep(2)

        if whichOS == 'Linux':
            os.system('clear')
        elif whichOS == 'Windows':
            os.system('cls')
        

        compHand = playTable[randint(0,2)]
        compHand = compHand.lower()
            

