# implementation of card game - Memory
# http://www.codeskulptor.org/#user40_icO9DtNTFR_8.py

import simplegui
import random

value1 = -1
value2 = -1
turns = 0
# helper function to initialize globals
def new_game():
    global deck
    global face_up
    global state
    global turns
    
    turns = 0
    state = 0
    
    deck = range(0,8)
    deck.extend(deck)
    random.shuffle(deck)
    
    face_up = list([])
    
    for x in range(0,16):
        face_up.append(False)
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state
    global value1
    global value2
    global card1
    global card2
    global turns
    
    print state
    
    if state == 0:
        card1 = pos[0] / 50
        if face_up[card1] == False:
            face_up[card1] = True
            state = 1
            turns += 1
            label.set_text("Turns = " + str(turns))
          
    elif state == 1:
      
        card2 = pos[0] / 50
        if face_up[card2] == False:
            face_up[card2] = True
          
            state = 2
            turns += 1
            label.set_text("Turns = " + str(turns))
            
    elif state == 2:
        
        value1 = deck[card1]
        value2 = deck[card2]
        print str(value1) + "&" + str(value2)
        
        if value1 != value2:
            face_up[card1] = False
            face_up[card2] = False
        
        card1 = pos[0] / 50
        if face_up[card1] == False:
            face_up[card1] = True
            state = 1
            turns += 1
            label.set_text("Turns = " + str(turns))

def draw(canvas):
    y = 0
    for x in deck:
        if face_up[y] == False:
            canvas.draw_polygon([[50 * y + 3, 3], [50 * (y + 1) - 3, 3], [50 * (y + 1) - 3, 97], [50 * y + 3, 97]], 3, "white", "navy")
        else:
            canvas.draw_polygon([[50 * y + 3, 3], [50 * (y + 1) - 3, 3], [50 * (y + 1) - 3, 97], [50 * y + 3, 97]], 3, "white", "yellow")
            canvas.draw_text(str(x),[15 + 50 * y, 63],40,"teal","sans-serif") 
        y += 1
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turns))


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric