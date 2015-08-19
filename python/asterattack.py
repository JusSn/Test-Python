# ___   ___   ___   ___               ___  
#|   | |     |   |   | \       |\ /| |     
#|-+-  |-+-  |-+-|   + |       | + | |-+-  
#|  \  |     |   |   | |       |   | |     
#|   \ |___  |   |  _|_/       |   | |___   

# INSTRUCTIONS:
# Codeskulptor framework and code available at http://www.codeskulptor.org/#user40_JZNWEOOPiACQFXU_0.py
# 
# (0. Google Chrome is recommended)
# 1. Allow pop-ups
# 2. Click the play button in top left corner 
# 3. Maximize the new window
# 4. Controls explained on left-hand side of window. 
# 5. Enjoy!
# 6. If sound effects (explosion, thrust, and missile) do not work, please alert me!
# 7. To turn off music after closing popup, hit the back-arrow on top left of CodeSkulptor.

# DISCLAIMERS
# Justin Fan
# Asteroid Attack

# extension of Rice University Python course's RiceRocks concept
# original template by Scott Rixner et. al. of Rice University 
#   (their code is marked with --PROVIDED CODE--)

# Asteroid/environment particle art assets created by Kim Lathrop 
# may be freely re-used in non-commercial projects, please credit Kim

# All images and sounds property of their respective owners

# need to do:
# doubleshot powerup
# freeze rocks powerup (color change?)
# invicibility powerup (touch damage?)
# bomb (on pickup, or store for later use?)

# barrel roll (dodge asteroid on key press?)

# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT =600
score = 0.0
accu = 0.00
hi = 0
hi_acc = 0
shots = 0
perc = 100
level = 1
time = 0

acc = 0.08 # rotation acceleration

music = True

msg = ""
left = False
right = False

state = 0 # title screen state

persist = 35
slow = 25

title = "ASTEROID ATTACK"
hi_score = "high score: " + str(hi)
instructs = "No rock shall pass!"
msg = "GAME OVER"

# ------------------PROVIDED CODE---------------------------------------------------------------

class ImageInfo:
    def __init__(self, center, size, radius = 0):
        self.center = center
        self.size = size
        self.radius = radius

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])

# END ------------------PROVIDED CODE--------------------------------------------------------------- END

a = "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris1_brown.png"
b = "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_brown.png"
c = "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris3_brown.png"
d = "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris4_brown.png"
e = "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris1_blue.png"
f = "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png"
g = "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris3_blue.png"
h = "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris4_blue.png"
g = "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris_blend.png"
debs = random.choice([a, b, c, d, e, f, g])
debris_image = simplegui.load_image(debs)

nebula_info = ImageInfo([700, 500], [WIDTH, HEIGHT])
ylw = "http://7-themes.com/data_images/out/47/6932033-space-background-25628.jpg"
prp = "http://static.tumblr.com/bc660a9f1f3c2acfd47dda4834b9ce63/qdfhp89/s9an3665b/tumblr_static_pink_nebula_space_lights-wide1.jpg"
blk = "http://7-themes.com/data_images/out/75/7027542-space-backgrounds-wallpaper.jpg"
red = "http://p1.pichost.me/i/24/1473632.jpg"
grn = "http://imagesci.com/img/2013/12/earth-space-background-2456-hd-wallpapers.jpg"
blu = "http://images4.alphacoders.com/106/106826.jpg"

order = [grn, blu, blk, ylw, prp, red]

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://i.imgur.com/ivkLPG8.png")

# missile image
missile_info = ImageInfo([20,5], [40, 10], 3)
missile_image = simplegui.load_image("http://i.imgur.com/sWQdHsI.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
brown = "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blend.png"
blue = "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png"
blend = "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blend.png"
asteroid_image = simplegui.load_image(blend)

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

soundtrack = simplegui.load_sound("http://zeldapower.com/downloads/mp3/ssbb2/Star_Fox_Assault_-_Star_Wolf_Theme.mp3")
soundtrack.set_volume(.15)

ship_thrust_sound = simplegui.load_sound("http://www.starfox-online.net/files/file/811-boostmp3/?do=download&csrfKey=e7c7e9032f13c14b56628f39d765c66d")
explosion_sound = simplegui.load_sound("http://www.starfox-online.net/files/file/814-arwinghitgroundmp3/?do=download&csrfKey=e7c7e9032f13c14b56628f39d765c66d")
missile_sound = simplegui.load_sound("http://f.starfox-online.net/sf64/sfx/arwingHyperLaserOneShot.mp3")

# ------------------PROVIDED CODE---------------------------------------------------------------

# helper functions to handle transformations
def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
# END ------------------PROVIDED CODE--------------------------------------------------------------- END
        
        self.alive = True
        self.pos_2 = [pos[0] - 45, pos[1] - 45]
        self.side = True
        
        self.exploded = 0
        
    def draw(self,canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos_2, self.image_size, self.angle)

    def update(self):
        
        if self.alive == True:
            self.angle = self.angle + self.angle_vel
            if self.thrust == True:
                ship_thrust_sound.set_volume(1)
                self.vel[0] += 0.2 * math.cos(self.angle)
                self.vel[1] += 0.2 * math.sin(self.angle)
                self.image_center[0] = 135
                ship_thrust_sound.play()
                
            else:
                self.image_center[0] = 45
                ship_thrust_sound.pause()
                ship_thrust_sound.rewind()
        else:
            self.exploded += 1
            self.image = explosion_image
            self.image_center = [(self.exploded / 2) * 128 + 64, explosion_info.get_center()[1]]
            self.image_size = explosion_info.get_size()
            ship_thrust_sound.pause()
            
        self.vel[0] *= 0.98
        self.vel[1] *= 0.98
        
        self.pos_2 = [(self.pos[0] % (WIDTH + 75)) - 45, (self.pos[1] % (HEIGHT + 75)) - 45]
        
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
       
    def shoot(self):
        
        # can't shoot while dead!
        if self.alive == True:
            global missile_sound, hi, hi_acc, accu
            
            # allows new missiles to make sound on spawn
            missile_sound.set_volume(1)

            missile_pos = [0, 0]
            bmissile_pos = [0, 0]
            missile_vel = [0, 0]
            
            if self.side: # left side
                # multiple of trig(angle) will displace in direction of ship vector
                # multiple of trig(angle +/- pi/2) will displace perpendicularly
                missile_pos[0] = self.pos_2[0] + 20 * math.cos(self.angle) + 10 * math.cos(self.angle - math.pi / 2)
                missile_pos[1] = self.pos_2[1] + 20 * math.sin(self.angle) + 10 * math.sin(self.angle - math.pi / 2)
                self.side = False
            else:
                missile_pos[0] = self.pos_2[0] + 20 * math.cos(self.angle) + 10 * math.cos(self.angle + math.pi / 2)
                missile_pos[1] = self.pos_2[1] + 20 * math.sin(self.angle) + 10 * math.sin(self.angle + math.pi / 2)
                self.side = True 
            
            missile_vel[0] = 15 * math.cos(self.angle)
            missile_vel[1] = 15 * math.sin(self.angle)

            a_missile = Sprite(missile_image, missile_info, missile_sound, missile_pos, missile_vel, self.angle, 0)
            # b_missile = Sprite(missile_image, missile_info, missile_sound, bmissile_pos, missile_vel, self.angle, 0)
            # add to list to be updated
            Missiles.add(a_missile)
            # Missiles.add(b_missile)

# Sprite class
class Sprite:
    # ------------------PROVIDED CODE---------------------------------------------------------------
    
    def __init__(self, image, info, sound = None, pos = [WIDTH / 3, HEIGHT / 3], vel = [1, 1], ang = 0, ang_vel = 0):
        self.pos = [pos[0],pos[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.age = 0 # will be used in later build
        
    # END ------------------PROVIDED CODE--------------------------------------------------------------- END
        
        # distance between object and ship
        self.dist = dist(self.pos, my_ship.pos_2)
        
        # distance between object and a projectile
        self.miss_dist = 1000
        
        # object velocity
        self.vel = vel
        
        # object sound effect
        self.sound = sound
        
        # current stage of explodiness
        self.exploded = 0
        
        # play sound effect if available
        if sound:
            sound.rewind()
            sound.play()
               
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
    def update(self):
        global score, accu, level, Rocks, persist, slow, state, hi, hi_acc, nebula_image
        
        # recalculate distance to ship
        self.dist = dist(self.pos, my_ship.pos_2)

        if self.sound == None: # rocks don't have sound effects
            
            # compare rock to every projectile currently in game
            for n in Missiles.items:    
                if n.exploded > persist:
                        Missiles.items.remove(n) # remove projectile after explosion animation completes
                else:
                    
                    # compare rock distance to missile n
                    self.miss_dist = dist(self.pos, n.pos)

                    if self.miss_dist < self.radius: # it's a hit!
                        score += 1
                        explosion_sound.rewind()
                        explosion_sound.play()
                       
                        # missile reaches stage 1 of exploding
                        n.exploded = 1
                        n.image = explosion_image
                        n.image_center = [64, explosion_info.get_center()[1]]
                        n.image_size = explosion_info.get_size()
                        n.vel[0] = n.vel[0] / slow
                        n.vel[1] = n.vel[1] / slow
                        n.angle_vel = 0
                        
                        # remove rock immediately so that it doesn't eat extra shots
                        Rocks.items.remove(self) 
                        
                        if len(Rocks) == 0: # no rocks left on screen
                            level += 1
                            nebula_image = simplegui.load_image(order[(level - 1) % 24 / 4])
                            # if slow > 1.33: # for powerups in a later build
                                # slow *= .75
                            for z in range(0, level / 2): # number of rocks in next level
                                
                                # spawn all rocks a set distance offscreen in random location
                                y = random.randint(-45, HEIGHT + 46)
                                x = random.randint(-45, WIDTH + 46)
                                loc = random.choice([[-90, y], [WIDTH + 90, y], [x, -90], [x, HEIGHT + 90]])
                                vel = [0, 0] # initialize velocity list
 
                                # Spin
                                angle_vel = random.randint(-10, 10) * .01

                                # set horizontal direction towards middle of screen
                                if loc[0] < WIDTH / 2:
                                    vel[0] = random.randint(5, 15) * 0.1
                                else:
                                    vel[0] = random.randint(5, 15) * -0.1

                                # set vertical direction towards middle of screen
                                if loc[1] < HEIGHT / 2:
                                    vel[1] = random.randint(5, 15) * 0.1
                                else:
                                    vel[1] = random.randint(5, 15) * -0.1
                                
                                # create rock and add to list    
                                a_rock = Sprite(asteroid_image, asteroid_info, None, loc, vel, 0, angle_vel)
                                Rocks.add(a_rock)
                                
                        break # cease iterating through missiles for this rock that was just destroyed
                        
            # determine if rock has left screen
            out_of_bounds = self.pos[0] > WIDTH + 100 or self.pos[0] < -100 or self.pos[1] > HEIGHT + 100 or self.pos[1] < -100
            
            # rock OOB or contacts ship
            if (self.dist < self.radius + 15 or out_of_bounds) and my_ship.alive == True:
                my_ship.alive = False
                
                explosion_sound.rewind()
                explosion_sound.play()
   
                state = 2
                soundtrack.pause()
        
        if shots == 0:
            accu = 0.00;
        else:
            accu = score * 10000.0 // shots / 100.00
        if score > hi:
            hi = score
            hi_acc = accu
        elif score == hi:
            if hi_acc < accu:
                hi_acc = accu
        
        # updates object position
        self.angle += self.angle_vel
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        # update exploding object animations
        if self.exploded > 0:
            self.image_center = [(self.exploded / 2) * 128 + 64, explosion_info.get_center()[1]]
            self.exploded += 1

# container class for object lists. update will iterate through these for missile and rock
class Multiples:
    def __init__(self, maxi = 100):
        self.MAX = maxi
        self.items = []
        
    def __len__(self):
        return len(self.items)
        
    def update(self):
        for x in self.items:
            x.update()
            
    def draw(self, canvas):
        for x in self.items:
            x.draw(canvas)
    
    def add(self, item):
        if len(self.items) >= self.MAX:
            self.items.pop(0)
            
        self.items.append(item)
    
    def maxi(self, maxi):
        self.MAX = maxi
    
    def remove(self, ind = 0):
        if len(self.items) > 0:
            self.items.pop(ind)
            
def SpawnPowerup(): # later build
    pass

# create keypress handler
def KeyDown(key):
    global left, right  # keeps track of keys to process conflicting presses. 
                        # can change direction without releasing key #1
                        # and continue in previous direction if key #1 is still pressed
                        # when key #2 is released
    global instructs, music, state, shots
    
    if key == simplegui.KEY_MAP["left"]:
        my_ship.angle_vel = -acc
        left = True
        
    elif key == simplegui.KEY_MAP["right"]:
        my_ship.angle_vel = acc
        right = True
        
    elif key == simplegui.KEY_MAP["up"]:
        my_ship.thrust = True
        
    elif key == simplegui.KEY_MAP["space"]:
        if state == 0:
            state = 1
        elif state == 1:
            shots += 1
            my_ship.shoot()
        
    elif key == simplegui.KEY_MAP["r"]:
        reset()
    
    elif key == simplegui.KEY_MAP["p"]:
        if state == 1:
            state = 3
        elif state == 3:
            state = 1
       
    elif key == simplegui.KEY_MAP["m"]:
        if music == True:
            soundtrack.set_volume(0) # mute music
            music = False
        else:
            soundtrack.set_volume(.15)
            music = True

# create key release handler
def KeyUp(key):
    global left, right
    
    if key == simplegui.KEY_MAP["left"]:
        left = False
        if right == False:
            my_ship.angle_vel = 0
        else:
            my_ship.angle_vel = acc
    
    elif key == simplegui.KEY_MAP["right"]:
        right = False
        if left == False:
            my_ship.angle_vel = 0
        else:
            my_ship.angle_vel = -acc
            
    elif key == simplegui.KEY_MAP["up"]:
        my_ship.thrust = False

# create draw handler
def draw(canvas): 
    global time, my_ship
    
    # animiate background
    time -= 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    
    my_ship.draw(canvas)
    if state > 0 and state < 4:
    # draw ship and sprites
        Rocks.draw(canvas) # custom draw method will iterate through list of asteroids
        Missiles.draw(canvas) # same for projectiles
        
        if not state == 3:
            # update ship and sprites
            Rocks.update()
            Missiles.update()
            my_ship.update()
            
        else:
            canvas.draw_text("PAUSED", [HEIGHT / 2 - 105, 200], 100, "White", "sans-serif")
        
        # HUD updates
        canvas.draw_text("level " + str(level), [50, 80], 40, "White", "sans-serif")
        canvas.draw_text(str(int(score)), [50, HEIGHT - 90], 40, "White", "sans-serif")
        canvas.draw_text(str(accu) + "%", [50, HEIGHT - 50], 40, "White", "sans-serif") 
        
        if state == 2:
            canvas.draw_text(msg, [HEIGHT / 2 - 200, 300], 100, "White", "sans-serif")
        
    elif state == 0:
        canvas.draw_text("high score: " + str(int(hi)) + " @ " + str(hi_acc) + "%", [50, HEIGHT - 50], 30, "White", "sans-serif")
        canvas.draw_text(title, [WIDTH / 2 - 235, 150], 50, "White", "sans-serif")
        canvas.draw_text(instructs, [WIDTH / 2 - 130, 215], 30, "White", "sans-serif")
        canvas.draw_text("Hit SPACE to begin!", [WIDTH / 2 - 135, 400], 30, "White", "sans-serif")
        canvas.draw_text("fire    SPACE", [50, 215], 20, "White", "monospace")
        canvas.draw_text("turn    RIGHT", [50, 245], 20, "White", "monospace")
        canvas.draw_text("        LEFT", [50, 268], 20, "White", "monospace")
        canvas.draw_text("pause   P", [50, 328], 20, "White", "monospace")
        canvas.draw_text("music   M", [50, 358], 20, "White", "monospace")
        canvas.draw_text("move    UP", [50, 298], 20, "White", "monospace")
        canvas.draw_text("reset   R", [50, 388], 20, "White", "monospace")
       
 
    
def reset():
    global my_ship, score, Missiles, Rocks, level, music, debris_image, nebula_image, state, shots, accu
    
    state = 0
    
    if music == True:
        soundtrack.rewind()
        soundtrack.play()
        
    debs = random.choice([a, b, c, d, e, f, g]) # switch debris background
    debris_image = simplegui.load_image(debs)
    
    # nebs = random.choice([ylw, prp, blk, red, grn, blu]) # switch background image
    nebula_image = simplegui.load_image(grn)
    
    score = 0
    level = 1
    shots = 0
    accu = 0
    
    # reset ship
    my_ship = Ship([WIDTH / 2 + 45, HEIGHT / 2 + 45], [0, 0], 0, ship_image, ship_info)
    
    Missiles = Multiples(30) # limit to prevent slowdowns
    Rocks = Multiples() # will be limited by player ability
    
    # spawn first rock
    y = random.randrange(-45, 646)
    x = random.randrange(-45, 846)
    loc = random.choice([[-45, y], [WIDTH + 45, y], [x, -45], [x, HEIGHT + 45]])
    vel = [0, 0]

    # spin
    angle_vel = random.randint(-10, 10) * .01

    # Horizontal direction
    if loc[0] < WIDTH / 2:
        vel[0] = random.randint(5, 15) * 0.1
    else:
        vel[0] = random.randint(5, 15) * -0.1

            # Vertical Direction
    if loc[1] < HEIGHT / 2:
        vel[1] = random.randint(5, 15) * 0.1
    else:
        vel[1] = random.randint(5, 15) * -0.1

    a_rock = Sprite(asteroid_image, asteroid_info, None, loc, vel, 0, angle_vel)
    Rocks.add(a_rock)
    
# initialize frame
frame = simplegui.create_frame("Asteroid Attack", WIDTH, HEIGHT)
ButReset = frame.add_button("reset", reset, 100)
tut = ["Left/Right to turn", "Up to thrust", "Space to shoot", "R to reset", "P to un/pause", "M to mute/unmute music"]
for x in tut:
    frame.add_label(x, 300)

# initialize ship and two sprites
reset ()
# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(KeyDown)
frame.set_keyup_handler(KeyUp)

# get things rolling
frame.start()

