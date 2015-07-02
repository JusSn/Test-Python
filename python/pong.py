http://www.codeskulptor.org/#user40_72rVJSV4uk_79.py

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
UP = True

xBall = [WIDTH / 2, HEIGHT / 2]
vBall = [0,0]

x1 = HEIGHT / 2
x2 = HEIGHT / 2

v1 = 0
v2 = 0

score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global xBall, vBall
    global LEFT, UP
    
    xBall[0] = WIDTH / 2
    xBall[1] = HEIGHT / 2
    UP = True
    
    #direction is 1 or 0; 1 for left, 0 for right
    if direction == 0:
        LEFT = True
    else:
        LEFT  = False
    
    #seems like velocity numbers given in spec were quite exaggerated
    vBall[0] = random.randrange(3,8)
    vBall[1] = 0.1 * random.randrange(5,30)

# define event handlers
def new_game():
    global x1, x2, v1, v2
    global score1, score2  # these are ints
    global LEFT, UP
    global buttontext
    
    score1 = 0
    score2 = 0
    
    x1 = HEIGHT / 2
    x2 = HEIGHT / 2
    
    #random number 0 or 1 to decide left/right
    spawn_ball(random.randrange(0,2))

def draw(canvas):
    global score1, score2, x1, x2, xBall, vBall, LEFT, UP
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if LEFT == True:
        xBall[0] -= vBall[0]
        if xBall[0] < BALL_RADIUS + PAD_WIDTH:
            LEFT = False
            
            #increase horizontal velocity per bounce off paddle
            vBall[0] = 1.1 * vBall[0]
            vBall[1] = 1.1 * vBall[1]
            #random vertical velocity after hitting pad to make things interesting
            vBall[1] = 0.1 * random.randrange(0,30)
            
    else:
        xBall[0] += vBall[0]
        if xBall[0] > WIDTH - BALL_RADIUS - PAD_WIDTH:
            LEFT = True
            vBall[0] = 1.1 * vBall[0]
            vBall[1] = 1.1 * vBall[1]
            
            vBall[1] = 0.1 * random.randrange(0,30)
    
    if UP == True:
        xBall[1] -= vBall[1]
        if xBall[1] < BALL_RADIUS:
            UP = False
    else:
        xBall[1] += vBall[1]
        if xBall[1] > HEIGHT - BALL_RADIUS:
            UP = True
    
    # draw scores
    canvas.draw_text(str(score1), [220,75], 50, "Cyan")
    canvas.draw_text(str(score2), [350,75], 50, "Red")
    
    # draw ball
    canvas.draw_circle(xBall, BALL_RADIUS, 1, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    if v1 < 0:
        if x1 > HALF_PAD_HEIGHT:
            x1 += v1
    else:
        if x1 < HEIGHT - HALF_PAD_HEIGHT:
            x1 += v1
            
    if v2 < 0:
        if x2 > HALF_PAD_HEIGHT:
            x2 += v2
    else:
        if x2 < HEIGHT - HALF_PAD_HEIGHT:
            x2 += v2
    
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, x1 - HALF_PAD_HEIGHT], [HALF_PAD_WIDTH, x1 + HALF_PAD_HEIGHT], PAD_WIDTH, "Cyan")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, x2 - HALF_PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH, x2 + HALF_PAD_HEIGHT], PAD_WIDTH, "Red")
    
    # determine whether paddle and ball collide    
    if xBall[0] < BALL_RADIUS + PAD_WIDTH:
        if (xBall[1] > x1 + HALF_PAD_HEIGHT + 10) or (xBall[1] < x1 - HALF_PAD_HEIGHT - 10):
            score2 += 1
            spawn_ball(1)
    
    if xBall[0] > WIDTH - (PAD_WIDTH + BALL_RADIUS):
        if (xBall[1] > x2 + HALF_PAD_HEIGHT + 10) or (xBall[1] < x2 - HALF_PAD_HEIGHT - 10):
            score1 += 1
            spawn_ball(0)
    
def keydown(key):
    global v1, v2
    
    if chr(key) == 'W':
        v1 = -10
    if chr(key) == 'S':
        v1 = 10
    
    if key == simplegui.KEY_MAP["up"]:
        v2 = -10
    if key == simplegui.KEY_MAP["down"]:
        v2 = 10
   
def keyup(key):
    global v1, v2
    
    if chr(key) in 'WS':
        v1 = 0
    
    if key == simplegui.KEY_MAP["up"]:
        v2 = 0
        
    if key == simplegui.KEY_MAP["down"]:
        v2 = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.add_label('Don\'t forget to maximize the window.\nHit "restart" to begin!')
frame.add_button("restart", new_game, 100)

# start frame
frame.start()
