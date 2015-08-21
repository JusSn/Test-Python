# ___   ___   ___   ___               ___    
#|   | |     |   |   | \       |\ /| |       I do not own any images or sounds used in this application.
#|-+-  |-+-  |-+-|   + |       | + | |-+-    All assets property of respective owners
#|  \  |     |   |   | |       |   | |       StarFox (TM) property of Nintendo Co. or respective owner
#|   \ |___  |   |  _|_/       |   | |___   

# INSTRUCTIONS:
# Codeskulptor framework and code available at http://www.codeskulptor.org/#user40_W3isdGQ9yxaWBKl_0.py
# (0. Google Chrome is recommended)
# 1. Allow pop-ups
# 2. Click the play button in top left corner 
# 3. Maximize the new window
# 4. Controls explained on left-hand side of window. 
# 5. Enjoy!
# 6. If sound effects (explosion, thrust, and missile) do not work, please alert me!
#       Also see line 46 of code.
# 7. To turn off music after closing popup, hit the back-arrow on top left of CodeSkulptor.

# DISCLAIMERS
# Justin Fan
# Asteroid Attack 2 

# extension of Rice University Python course's RiceRocks concept
# original template by Scott Rixner et. al. of Rice University 
#   (their code is marked with --PROVIDED CODE--)

# Asteroid/environment particle art assets created by Kim Lathrop 
# may be freely re-used in non-commercial projects, please credit Kim

# All images and sounds property of their respective owners

# program template for Spaceship
import simplegui
import math
import random

# sound effect mp3s from starfox-online.net do not work unless cached in browser first for some reason.
# swapping commented sound objects may or may not fix it depending on the machine.
# URLs do not change either. Possibly something to do with the way these files are hosted on this specific website.

# slow_sound = simplegui.load_sound("http://f.starfox-online.net/sf64/sfx/arwingHyperLaserOneShot.mp3")
# ship_thrust_sound = simplegui.load_sound("http://f.starfox-online.net/sf64/sfx/flyToNextMission.mp3")
# explosion_sound = simplegui.load_sound("http://f.starfox-online.net/sf64/sfx/arwingHitGround.mp3")
# nobombs_sound = simplegui.load_sound("http://f.starfox-online.net/sf64/sfx/noDamageHit.mp3")
# brake_sound = simplegui.load_sound("http://f.starfox-online.net/sf64/sfx/brake.mp3")
# pause_sound = simplegui.load_sound("http://f.starfox-online.net/sf64/sfx/pause.mp3")
# unpause_sound = simplegui.load_sound("http://f.starfox-online.net/sf64/sfx/vsDeselect.mp3")
# freeze_sound = simplegui.load_sound("http://f.starfox-online.net/sf64/sfx/vsMenuMove.mp3")
# bomb_pick_sound = simplegui.load_sound("http://f.starfox-online.net/sf64/sfx/bombPickup.mp3")
# pew_up_sound = simplegui.load_sound("http://f.starfox-online.net/sf64/sfx/laserPickup.mp3")
# double_pick_sound = simplegui.load_sound("http://f.starfox-online.net/sf64/sfx/openTargeting.mp3")
# missile_sound = slow_sound
# charged_sound = simplegui.load_sound("http://f.starfox-online.net/sf64/sfx/arwingPulseLaser.mp3")
# charged_sound.set_volume(0.5)
# heat_sound = simplegui.load_sound("http://f.starfox-online.net/sf64/sfx/landmasterSingleShot.mp3")
# shield_up_sound = simplegui.load_sound("http://f.starfox-online.net/sf64/sfx/radioTransmissionStart.mp3")
# shield_down_sound = simplegui.load_sound("http://f.starfox-online.net/sf64/sfx/radioTransmissionEnd.mp3")
# -----------------------

explosion_1 = simplegui.load_sound("http://vocaroo.com/media_command.php?media=s0zERqNdlH21&command=download_mp3")
explosion_2 = simplegui.load_sound("http://vocaroo.com/media_command.php?media=s1CVUs7LBvQw&command=download_mp3")
explosion_charged = simplegui.load_sound("http://vocaroo.com/media_command.php?media=s1gVdkSQY28h&command=download_mp3")
explosion_ship = simplegui.load_sound("http://vocaroo.com/media_command.php?media=s1PUaQg7CfX0&command=download_mp3")

ship_thrust_sound = simplegui.load_sound("http://vocaroo.com/media_command.php?media=s0YJ21ddhw9F&command=download_mp3")
nobombs_sound = simplegui.load_sound("http://vocaroo.com/media_command.php?media=s0s3ItaqU4sq&command=download_mp3")

brake_sound = simplegui.load_sound("http://vocaroo.com/media_command.php?media=s0vG53TcQjtf&command=download_mp3")
pause_sound = simplegui.load_sound("http://vocaroo.com/media_command.php?media=s0xRy9iIyaNH&command=download_mp3")
unpause_sound = simplegui.load_sound("http://vocaroo.com/media_command.php?media=s0tlh7KOqj2T&command=download_mp3")

freeze_sound = simplegui.load_sound("http://vocaroo.com/media_command.php?media=s0prqcAmKavg&command=download_mp3")
bomb_pick_sound = simplegui.load_sound("http://vocaroo.com/media_command.php?media=s0EvnDJM1QDX&command=download_mp3")

pew_up_sound = simplegui.load_sound("http://vocaroo.com/media_command.php?media=s0Yw1gxiDmPh&command=download_mp3")
double_pick_sound = simplegui.load_sound("http://vocaroo.com/media_command.php?media=s0GUGLJAQXLj&command=download_mp3")

a_miss_sound = simplegui.load_sound("http://vocaroo.com/media_command.php?media=s0i92pvN1fzA&command=download_mp3")
b_miss_sound = simplegui.load_sound("http://vocaroo.com/media_command.php?media=s0i92pvN1fzA&command=download_mp3")

a_charged_sound = simplegui.load_sound("http://vocaroo.com/media_command.php?media=s0PoMVGDccFJ&command=download_mp3")
b_charged_sound = simplegui.load_sound("http://vocaroo.com/media_command.php?media=s0PoMVGDccFJ&command=download_mp3")
a_charged_sound.set_volume(0.5)
b_charged_sound.set_volume(0.5)

heat_sound = simplegui.load_sound("http://vocaroo.com/media_command.php?media=s06NPDSmaE85&command=download_mp3")

shield_up_sound = simplegui.load_sound("http://vocaroo.com/media_command.php?media=s0woIgOOw6YD&command=download_mp3")
shield_down_sound = simplegui.load_sound("http://vocaroo.com/media_command.php?media=s0YYcW2MNZKj&command=download_mp3")


# globals for user interface
WIDTH = 800
HEIGHT = 600
edge1 = 50
edge2 = 630
s1 = 30
s2 = 40
tab = 45
top_edge = 215

speed = {1:25, 2:6, 3:2.5, 4:1.3333}
acc = 0.08 # rotation acceleration

hi = 0
hi_acc = 0

music = True
graphics = False # turn off background and animation for better performance?
v2 = True # denotes version 2 of the game with powerups

left = False
right = False
forw = True

persist = 36 # frames * 2 to show of missile explosion (affects when it is removed after detonating) 
title = "ASTEROID ATTACK"
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

a = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris1_brown.png")
b = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_brown.png")
c = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris3_brown.png")
d = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris4_brown.png")
e = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris1_blue.png")
f = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")
g = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris3_blue.png")
h = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris4_blue.png")
g = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris_blend.png")
debris_image = random.choice([a, b, c, d, e, f, g])

nebula_info = ImageInfo([700, 500], [WIDTH, HEIGHT])
ylw = simplegui.load_image("http://7-themes.com/data_images/out/47/6932033-space-background-25628.jpg")
prp = simplegui.load_image("http://static.tumblr.com/bc660a9f1f3c2acfd47dda4834b9ce63/qdfhp89/s9an3665b/tumblr_static_pink_nebula_space_lights-wide1.jpg")
blk = simplegui.load_image("http://7-themes.com/data_images/out/75/7027542-space-backgrounds-wallpaper.jpg")
red = simplegui.load_image("http://p1.pichost.me/i/24/1473632.jpg")
grn = simplegui.load_image("http://imagesci.com/img/2013/12/earth-space-background-2456-hd-wallpapers.jpg")
blu = simplegui.load_image("http://images4.alphacoders.com/106/106826.jpg")

order = [grn, blu, blk, ylw, prp, red]

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://i.imgur.com/ivkLPG8.png")

# missile image
missile_info = ImageInfo([20,5], [40, 10], 3)
shot_image = simplegui.load_image("http://i.imgur.com/sWQdHsI.png")
missile_image = shot_image
charged_image = simplegui.load_image("http://i.imgur.com/uNFyThJ.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
brown = "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blend.png"
blue = "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png"
blend = "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blend.png"
asteroid_image = simplegui.load_image(blend)
asteroid_frozen = simplegui.load_image(blue)

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")
explosion_blue2 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_blue2.png")
explosion_blue = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_blue.png")
explosion_orange = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_orange.png")

soundtrack = simplegui.load_sound("http://zeldapower.com/downloads/mp3/ssbb2/Star_Fox_Assault_-_Star_Wolf_Theme.mp3")
soundtrack.set_volume(.15)

def top(sep = 30, mult = 1):
    return top_edge + sep * mult

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
        if shielded > 0 and self.alive:
            canvas. draw_circle(self.pos_2, 47, 3, "yellow")

    def update(self):
        
        if self.alive:
            self.angle = self.angle + self.angle_vel
            if self.thrust == True:                
                self.image_center[0] = 135
                ship_thrust_sound.play()
                if forw == True:
                    self.vel[0] += 0.2 * math.cos(self.angle)
                    self.vel[1] += 0.2 * math.sin(self.angle)
                else:
                    self.vel[0] -= 0.2 * math.cos(self.angle)
                    self.vel[1] -= 0.2 * math.sin(self.angle)
                
            else:
                self.image_center[0] = 45
                ship_thrust_sound.pause()
                ship_thrust_sound.rewind()
        else:
            self.exploded += 1
            self.image = explosion_blue2
            self.image_center = [(self.exploded / 4) * 128 + 64, explosion_info.get_center()[1]]
            self.image_size = explosion_info.get_size()
            ship_thrust_sound.pause()
            ship_thrust_sound.rewind()
            
        self.vel[0] *= 0.98
        self.vel[1] *= 0.98
        
        self.pos_2 = [(self.pos[0] % (WIDTH + 75)) - 45, (self.pos[1] % (HEIGHT + 75)) - 45]
        
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
       
    def shoot(self):
        
        # can't shoot while dead!
        if self.alive == True:
            global a_missile_sound, b_missile_sound, missile_image, hi, hi_acc, accu, shots, heat
            
            if heat <= 6:
                # allows new missiles to make sound on spawn

                if pew == 4:
                    a_missile_sound = a_charged_sound
                    b_missile_sound = b_charged_sound
                    missile_image = charged_image

                if self.side or doubles:

                    missile_pos = [0, 0]
                    missile_vel = [0, 0]

                    missile_pos[0] = self.pos_2[0] + 20 * math.cos(self.angle) + 10 * math.cos(self.angle - math.pi / 2)
                    missile_pos[1] = self.pos_2[1] + 20 * math.sin(self.angle) + 10 * math.sin(self.angle - math.pi / 2)

                    missile_vel[0] = (12 + pew * 3) * math.cos(self.angle)  # need separate velocity list for each missile
                    missile_vel[1] = (12 + pew * 3) * math.sin(self.angle)  # even if identical because if not, 
                                                                            # affecting one will affect all (single list passed by ref)
                    a_missile = Sprite(missile_image, missile_info, a_missile_sound, missile_pos, missile_vel, self.angle, 0)
                    Missiles.add(a_missile)

                if not self.side or doubles:

                    b_missile_pos = [0, 0] 
                    b_missile_vel = [0, 0]

                    b_missile_pos[0] = self.pos_2[0] + 20 * math.cos(self.angle) + 10 * math.cos(self.angle + math.pi / 2)
                    b_missile_pos[1] = self.pos_2[1] + 20 * math.sin(self.angle) + 10 * math.sin(self.angle + math.pi / 2)

                    b_missile_vel[0] = (12 + pew * 3) * math.cos(self.angle)
                    b_missile_vel[1] = (12 + pew * 3) * math.sin(self.angle)

                    b_missile = Sprite(missile_image, missile_info, b_missile_sound, b_missile_pos, b_missile_vel, self.angle, 0)
                    Missiles.add(b_missile)

                if self.side:
                    a_missile_sound.rewind()
                    a_missile_sound.play()
                    self.side = False
                else:
                    b_missile_sound.rewind()
                    b_missile_sound.play()
                    self.side = True

                heat += 1
                shots += 1

            else:
                #weapon overheat
                heat_sound.rewind()
                heat_sound.play()

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
        self.hit_pos = [0, 0]
        
        self.combo = 0
               
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
    def update(self):
        global Rocks, persist, slow, nebula_image, doubles, shielded, dead_missile
        global score, level, accu, state, hi, hi_acc, combo, pew
        
        # recalculate distance to ship
        self.dist = dist(self.pos, my_ship.pos_2)

        if self.radius == 40: # rocks
            
            if self.exploded > 0:
                self.image = random.choice([explosion_image, explosion_blue, explosion_orange])
                self.image_center = [(self.exploded / 2) * 128 + 64, explosion_info.get_center()[1]]
                self.exploded += 1
                self.vel = [0, 0]
                if self.exploded > 48:
                    Rocks.items.remove(self)
            
            # compare rock to every projectile currently in game
            for n in Missiles.items:    
                if n.exploded > persist:
                        Missiles.items.remove(n)
                        dead_missile.items.remove(n)# remove projectile after explosion animation completes
                else:
                    
                    # compare rock distance to missile n
                    self.miss_dist = dist(self.pos, n.pos)

                    if self.miss_dist < self.radius: # it's a hit!
                        Rocks.items.remove(self)
                        score += 1
                        n.combo += 1
                        if n.exploded == 0:
                            n.hit_pos[0] = n.pos[0]
                            n.hit_pos[1] = n.pos[1]
                            dead_missile.add(n) # record location of hit
                            
                        if pew >= 4:
                            explosion_sound = explosion_charged
                        else:
                            explosion_sound = random.choice([explosion_1, explosion_2])
                        explosion_sound.rewind()
                        explosion_sound.play()
                       
                        # missile reaches stage 1 of exploding
                        n.exploded = 1 # resets the explosion if it hits additional rocks
                        n.image = random.choice([explosion_image, explosion_blue, explosion_orange])
                        n.image_center = [64, explosion_info.get_center()[1]]
                        n.image_size = explosion_info.get_size()
                        n.vel[0] = n.vel[0] / slow
                        n.vel[1] = n.vel[1] / slow
                        n.angle_vel = 0
                        
                        # remove rock immediately so that it doesn't eat extra shots
                                
                        break # cease iterating through missiles for this rock that was just destroyed
                        
            if len(Rocks) == 0: # no rocks left on screen
                level_up()
                        
            # determine if rock has left screen
            out_of_bounds = self.pos[0] > WIDTH + 100 or self.pos[0] < -100 or self.pos[1] > HEIGHT + 100 or self.pos[1] < -100
            
            # rock OOB or contacts ship
            if my_ship.alive and self.exploded == 0:
                if self.dist < self.radius + 15:
                    if not shielded > 0:
                        my_ship.alive = False
                    else:
                        self.exploded += 1
                        explosion_sound = random.choice([explosion_1, explosion_2])
                        explosion_sound.rewind()
                        explosion_sound.play()

                elif out_of_bounds:
                    my_ship.alive = False

                if not my_ship.alive:
                    explosion_ship.rewind()
                    explosion_ship.play()
       
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
            
# //////////////////////Asteroid Attack 2/////////////////////
            
class Power:
    def __init__(self, color):
        self.color = color
        self.age = 0
        self.dist = 1000
        self.radius = 20
        
        x = random.randrange(50, WIDTH - 50)
        y = random.randrange(50, HEIGHT - 50)
        
        self.pos = [x, y]
        self.gone = False
        self.picked = False
        
    def update(self):
        
        global bombs, Rocks, slow, pew, doubles, shielded

        if state == 2:
            self.gone = True

        self.dist = dist(my_ship.pos_2, self.pos)
        if self.dist < self.radius + 27:
            self.gone = True
            self.picked = True
            
        if self.gone == True:
            self.pos = [1000, 1000]
            
            if self.picked == True:
                if self.color == "red":
                    bomb_pick_sound.rewind()
                    bomb_pick_sound.play()
                    bombs += 1
                    
                elif self.color == "blue":
                    freeze_sound.rewind()
                    freeze_sound.play()
                    for x in Rocks.items:
                        x.image = asteroid_frozen
                        x.vel[0] *= 0.1
                        x.vel[1] *= 0.1
                        x.angle_vel = 0

                elif self.color == "lime":
                    if pew < 4:
                        pew += 1
                        slow = speed[pew]
                    pew_up_sound.rewind()
                    pew_up_sound.play()

                elif self.color == "cyan":
                    double_pick_sound.rewind()
                    double_pick_sound.play()

                    doubles = 1

                elif self.color == "yellow":
                    shield_up_sound.rewind()
                    shield_up_sound.play()

                    shielded = 1
                        
                self.picked = False
            
    def draw(self, canvas):
        canvas.draw_circle(self.pos, self.radius, 3, "White", self.color)

def level_up():
    global level, doubles, shielded, pew, slow
    global nebula_image, Rocks

    level += 1

    if v2 == True: # if powerups are enabled
        if doubles == 1:
            doubles = 2
        elif doubles == 2:
            doubles = 0

        if shielded == 1:
            shielded = 2
        elif shielded == 2:
            shield_down_sound.rewind()
            shield_down_sound.play()
            shielded = 0
        SpawnPowerup(level) # chance to spawn powerup

        if level % 8 == 0: # shot power increase every 10 levels
            if pew < 4:
                pew += 1
                slow = speed[pew]
                pew_up_sound.rewind()
                pew_up_sound.play()

    if graphics:
        nebula_image = order[(level - 1) % 24 / 4]

    for z in range(0, level / 2): # number of rocks in next level
        spawn_rock()

def spawn_rock():
    global Rocks
        # spawn all rocks a set distance offscreen in random location
    y = random.randint(-40, HEIGHT + 41)
    x = random.randint(-40, WIDTH + 41)
    loc = [1000, 1000]

    valid = False
    while not valid: # prevents asteroids from spawning too close to ship
        pos = random.choice([[-40, y], [WIDTH + 40, y], [x, -40], [x, HEIGHT + 40]])
        if dist(my_ship.pos_2, pos) > 200:
            loc = pos
            valid = True

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

def SpawnPowerup(o_level):
    # random chance to regenerate each level
    # gameplay bonus lasts for rest of round and next level
    # moves offscreen if round passes without it being picked up
    # check powerup for age and move if age > 2 or something
    global powerup
    
    chance = random.choice(range(0, 10))
    if chance <= 4:
        color = random.choice(["red","lime","cyan","yellow","blue"])
        if pew >= 4 and color == "lime":
            color = "cyan"
        powerup = Power(color)

def Bomb():
    global bombs 
    
    if bombs > 0:
        bombs -= 1
        explosion_1.rewind()
        explosion_1.play()
        explosion_2.rewind()
        explosion_2.play()
        for x in Rocks.items:
            x.exploded += 1
    else:
        nobombs_sound.rewind()
        nobombs_sound.play()
    

# create keypress handler
def KeyDown(key):
    global left, right  # keeps track of keys to process conflicting presses. 
                        # can change direction without releasing key #1
                        # and continue in previous direction if key #1 is still pressed
                        # when key #2 is released
    global music, state, forw, bombs
    
    if key == simplegui.KEY_MAP["left"]:
        my_ship.angle_vel = -acc
        left = True
        
    elif key == simplegui.KEY_MAP["right"]:
        my_ship.angle_vel = acc
        right = True
        
    elif key == simplegui.KEY_MAP["up"]:
        my_ship.thrust = True
        forw = True

    elif key == simplegui.KEY_MAP["down"]:
        my_ship.thrust = True
        forw = False
        
    elif key == simplegui.KEY_MAP["space"]:
        if state == 0:
            state = 1
            if v2:
                bombs = 1
        elif state == 1:
            my_ship.shoot()
            
    elif key == simplegui.KEY_MAP["b"]:
        if state == 1:
            Bomb()
        
    elif key == simplegui.KEY_MAP["r"]:
        reset()
    
    elif key == simplegui.KEY_MAP["p"]:
        if state == 1:
            soundtrack.pause()
            pause_sound.rewind()
            pause_sound.play()
            state = 3
            
        elif state == 3:
            soundtrack.play()
            unpause_sound.rewind()
            unpause_sound.play()
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
            
    elif key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        my_ship.thrust = False

def OnClick(pos):
    global graphics, v2

    if state == 0:
        if WIDTH - 80 < pos[0] and pos[0] < WIDTH - 50:
            if HEIGHT - 80 < pos[1] and pos[1] < HEIGHT - 50:
                if not graphics:
                    graphics = True
                else:
                    graphics = False
            elif HEIGHT - 120 < pos[1] and pos[1] < HEIGHT - 90:
                if not v2:
                    v2 = True
                else:
                    v2 = False
def center_text(frame, canvas, text, y, point, color = "white", face = "sans-serif"):
    pixels = frame.get_canvas_textwidth(text, point, face)
    canvas.draw_text(text, [WIDTH / 2 - pixels / 2, y], point, color, face)

# create draw handler
def draw(canvas): 
    global time, heat
    soundtrack.play()
    
    # animate background
    time -= 1
    if time % 40 == 0: # weapon cooldown rate
        if heat > 0:
            heat -= 1

    if graphics:
        # ------------------PROVIDED CODE---------------------------------------------------------------
        wtime = (time / 4) % WIDTH
        center = debris_info.get_center()
        size = debris_info.get_size()
        canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
        canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
        canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
        
        # END ------------------PROVIDED CODE--------------------------------------------------------------- END

    my_ship.draw(canvas)
    if state > 0 and state < 4: # in-game states
    # draw ship and sprites
        Rocks.draw(canvas) # custom draw method will iterate through list of asteroids
        Missiles.draw(canvas) # same for projectiles
        
        combo_colors = ["silver", "teal", "lime", "cyan", "fuchsia", "red", "orange", "yellow"]
        if dead_missile:
            for item in dead_missile.items:
                combo_text = "+" + str(item.combo)
                canvas.draw_text(combo_text, item.hit_pos, item.combo * 15, combo_colors[item.combo % 8], "sans-serif") 
            
        if powerup:
            powerup.draw(canvas)
            powerup.update()
        
        if not state == 3: # not paused
            # update ship and sprites
            Rocks.update()
            Missiles.update()
            my_ship.update()
            
        else:
            center_text(frame, canvas, "PAUSED", 200, 100, "White", "sans-serif")
        
        # HUD updates
        canvas.draw_text("level " + str(level), [50, 80], 40, "White", "sans-serif")
        canvas.draw_text(str(int(score)), [50, HEIGHT - 90], 40, "White", "sans-serif")
        canvas.draw_text(str(accu) + "%", [50, HEIGHT - 50], 40, "White", "sans-serif")
        

        if v2: # powerups enabled
            canvas.draw_text(str(bombs), [WIDTH - 75, 80], 40, "Red", "sans-serif")

            if doubles > 0:
                pew_color = "cyan"
            else:
                pew_color = "lime"
            canvas.draw_text(str(pew), [WIDTH - 115, HEIGHT - 50], 40, pew_color, "sans-serif")

        for x in range(0, heat):
            if x < 2:
                color = "lime"
            elif x < 4:
                color = "yellow"
            elif x < 6:
                color = "orange"
            elif x == 6:
                color = "red"
            LL = [WIDTH - 75, HEIGHT - 50 - x * 30]
            UL = [WIDTH - 75, HEIGHT - 75 - x * 30]
            UR = [WIDTH - 50, HEIGHT - 75 - x * 30]
            LR = [WIDTH - 50, HEIGHT - 50 - x * 30]

            canvas.draw_polygon([LL, UL, UR, LR], 1, color, color)
        
        if state == 2: # Game Over state
            center_text(frame, canvas, msg, 300, 100)
            
    elif state == 0: # Main Menu
    
        center_text(frame, canvas, "2", 155, 150, "cyan", "serif")
        center_text(frame, canvas, title, 125, 50)
        center_text(frame, canvas, instructs, 215, 30)
        center_text(frame, canvas, "Hit SPACE to begin!", 400, 30)
        
        canvas.draw_text("best: " + str(int(hi)) + " @ " + str(hi_acc) + "%", [50, HEIGHT - 50], 25, "White", "sans-serif")

        canvas.draw_text("fire    SPACE", [edge1, top_edge], 20, "White", "monospace")
        canvas.draw_text("bomb    B", [edge1, top(s1)], 20, "White", "monospace")
        canvas.draw_text("turn    RIGHT", [edge1, top(s1, 2)], 20, "White", "monospace")
        canvas.draw_text("        LEFT", [edge1, top(s1, 3)], 20, "White", "monospace")
        canvas.draw_text("move    UP", [edge1, top(s1, 4)], 20, "White", "monospace")
        canvas.draw_text("        DOWN", [edge1, top(s1, 5)], 20, "White", "monospace")
        canvas.draw_text("pause   P", [edge1, top(s1, 6)], 20, "White", "monospace")
        canvas.draw_text("music   M", [edge1, top(s1, 7)], 20, "White", "monospace")
        canvas.draw_text("reset   R", [edge1, top(s1, 8)], 20, "White", "monospace")

        LL = [WIDTH - 80, HEIGHT - 50]
        UL = [WIDTH - 80, HEIGHT - 80]
        UR = [WIDTH - 50, HEIGHT - 80]
        LR = [WIDTH - 50, HEIGHT - 50]
        if graphics:
            canvas.draw_polygon([LL, UL, UR, LR], 6, "White", "Cyan")
        else:
            canvas.draw_polygon([LL, UL, UR, LR], 6, "White", "Gray")
        c = 1
        LL = [WIDTH - 80, HEIGHT - 50 - c * 40]
        UL = [WIDTH - 80, HEIGHT - 80 - c * 40]
        UR = [WIDTH - 50, HEIGHT - 80 - c * 40]
        LR = [WIDTH - 50, HEIGHT - 50 - c * 40]
        if v2:
            canvas.draw_polygon([LL, UL, UR, LR], 6, "White", "Cyan")

            canvas.draw_circle([edge2, top_edge - 7], 13, 3, "White", "red")
            canvas.draw_text("+bomb", [edge2 + tab, top_edge], 20, "White", "monospace")
            canvas.draw_circle([edge2, top(s2) - 7], 13, 3, "White", "lime")
            canvas.draw_text("+power", [edge2 + tab, top(s2)], 20, "White", "monospace")
            canvas.draw_circle([edge2, top(s2, 2) - 7], 13, 3, "White", "cyan")
            canvas.draw_text("double", [edge2 + tab, top(s2, 2)], 20, "White", "monospace")
            canvas.draw_circle([edge2, top(s2, 3) - 7], 13, 3, "White", "blue")
            canvas.draw_text("freeze", [edge2 + tab, top(s2, 3)], 20, "White", "monospace")
            canvas.draw_circle([edge2, top(s2, 4) - 7], 13, 3, "White", "yellow")
            canvas.draw_text("shield", [edge2 + tab, top(s2, 4)], 20, "White", "monospace")
        else:
            canvas.draw_polygon([LL, UL, UR, LR], 6, "White", "Gray")
        canvas.draw_text("GRAPHICS", [WIDTH - 280, HEIGHT - 50], 30, "White", "sans-serif")
        canvas.draw_text("POWERUPS", [WIDTH - 280, HEIGHT - 90], 30, "White", "sans-serif")
        
       
def reset():
    global my_ship, Missiles, Rocks, debris_image, nebula_image, state, a_missile_sound, b_missile_sound, missile_image, dead_missile
    global bombs, level, shots, accu, score, pew, slow, heat, doubles, shielded, powerup, time
    
    explosion_ship.pause()
    explosion_ship.rewind()

    state = 0
    soundtrack.play()
        
    debris_image = random.choice([a, b, c, d, e, f, g])
    
    # nebs = random.choice([ylw, prp, blk, red, grn, blu]) # switch background image
    nebula_image = grn
    
    score = 0
    level = 1
    shots = 0
    accu = 0
    time = 0
    heat = 0
    pew = 1
    slow = speed[pew]
    combo = 0
    bombs = 0
    doubles = 0
    shielded = 0

    powerup = None
    
    a_missile_sound = a_miss_sound
    b_missile_sound = b_miss_sound
    missile_image = shot_image
    
    # reset ship
    my_ship = Ship([WIDTH / 2 + 45, HEIGHT / 2 + 45], [0, 0], 0, ship_image, ship_info)
    my_ship.thrust = False
    
    Missiles = Multiples(30) # limit to prevent slowdowns
    dead_missile = Multiples(30) # missiles that manage to hit recorded here
    Rocks = Multiples() # will be limited by player ability
    
    # spawn first rock
    spawn_rock()
    
# initialize frame
frame = simplegui.create_frame("Asteroid Attack", WIDTH, HEIGHT)
ButReset = frame.add_button("reset", reset, 100)

# initialize ship and two sprites
reset()

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(KeyDown)
frame.set_keyup_handler(KeyUp)
frame.set_mouseclick_handler(OnClick)

# get things rolling
frame.start()