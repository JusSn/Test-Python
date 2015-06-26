# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

secret_number = 0
limit = 7
guesses = 0

# helper function to start and restart the game
def new_game(num):
    print "-------------------------\nNew Game | Range: 0 -", num
    
    # initialize global variables used in your code here
    global secret_number
    global limit
    global guesses
    
    guesses = 0
    
    if num == 100:
        limit = 7
    elif num == 1000:
        limit = 10
        
    secret_number = random.randrange(0,num,1)

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    new_game(100)
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    new_game(1000)

def input_guess(guess):
    # main game logic goes here	
    global guesses
    
    #add to number of guesses
    guesses += 1 
    
    #convert input to int
    guessint = int(guess) 
    
    #prints last guess
    print "\nGuess was " + guess 
    
    #Comparison if/else block
    if guessint > secret_number:
        print "The secret number is lower.", limit - guesses, "guesses remaining."
        
    elif guessint == secret_number:
        print "Correct!"
        
        if limit == 10:
            new_game(1000)
        else:
            new_game(100)
            
    else: 
        print "The secret number is higher.", limit - guesses, "guesses remaining."
    
    #decides if game is over
    if guesses >= limit:
        print "\nGame Over! The number was",secret_number
        
        if limit == 10:
            new_game(1000)
        else:
            new_game(100)
    
# create frame
frame = simplegui.create_frame("Guess The Number!",100,400)

# register event handlers for control elements and start frame
frame.add_input("Input",input_guess,150)
frame.add_button("Range: 0 - 100",range100,150)
frame.add_button("Range: 0 - 1000",range1000,150)
frame.start()

# call new_game 
new_game(100)

# always remember to check your completed program against the grading rubric
