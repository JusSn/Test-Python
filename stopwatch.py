# template for "Stopwatch: The Game"
# http://www.codeskulptor.org/#user40_lzs9Jn3ekZ_0.py

import simplegui
# define global variables

deciseconds = 0
D = 0
points = 0
attempts = 0
time_format = "0:00.0"
score = "0/0"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global time_format
    global D
    A = str(t//600)
    
    #total time in seconds
    secs = (t//10)%60 
    if secs < 10:
        B = "0" + str(secs)
    else:
        B = str(secs)
        
    D = str(t%10)
    
    #convert to String
    time_format = A + ":" + B + "." + D
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    #need to update score
    global points
    global attempts
    
    if timer.is_running() == True:
        timer.stop()
        attempts += 1
        if D == "0":
            points += 1
    
    update_score()
        
def reset():
    #need to reset time and score
    global deciseconds
    global points
    global attempts
    
    #set to -1 because update function adds 1
    deciseconds = -1
    points = 0
    attempts = 0
    
    timer.stop()
    update_time()
    update_score()
    
# define event handler for timer with 0.1 sec interval
def update_time():
    global deciseconds
    
    deciseconds += 1
    
    #converts new time
    format(deciseconds)
