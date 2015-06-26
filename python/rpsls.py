# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name == 'rock':
        number = 0
    elif name == 'Spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    elif name == 'scissors': 
        number = 4
    else:
        number = "Invalid input"
    return number

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return "Invalid number"
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    
def winner(play_numb,comp_number):
    if play_numb == comp_number:
        return "Player and Computer tie!"
    diff = (play_numb - comp_number) % 5
    if diff < 3:
        return "Player wins!"
    else:
        return "Computer wins!"
    
        
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    comp_number = random.randrange(0,5,1)
    play_numb = name_to_number(player_choice)
    if play_numb == "Invalid number":
        print play_numb
    else:
        print "Player chooses " + player_choice
        print "Computer chooses " + number_to_name(comp_number)
        print winner(play_numb,comp_number)
        print ""

    # print a blank line to separate consecutive games

    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()
    
    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


