from classes import color

def score_board(human, computer):
    print(color.GREEN + "Ultimate Rock, Paper, Scissors Ver: 0.0.2")
    print(color.CYAN + "____________________________________________________" + color.RESET)
    print(color.CYAN + "|" + color.RESET, color.BLUE + "   Player Score: " + color.RESET, human , color.CYAN + " | " + color.RESET, color.MAGENTA + "    Computer Score: " + color.RESET, computer, color.CYAN + "  |" + color.RESET)
    print(color.CYAN + "----------------------------------------------------" + color.RESET)
