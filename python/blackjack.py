# Mini-project #6 - Blackjack
# http://www.codeskulptor.org/#user40_kBIhDxtfk2_42.py

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
msg = ""
msg2 = ""

score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, rank, suit):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.rank + "|" + self.suit

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []
        self.soft = False
        self.num = 0

    def __str__(self):
        output = ""
        for x in self.hand:
            output = output + " " + str(x)
            
        return output
        
    def add_card(self, card):
        self.num += 1
        self.hand.append(card)
       

    def get_value(self):
        total = 0
        for x in self.hand:
            rank = x.get_rank()
            value = VALUES[rank]
            if rank == 'A':
                if total + 11 < 21:
                    total = total + 11
                    self.soft = True
                else:
                    total = total + 1
            else:
                if (total + value > 21):
                    if (self.soft == True):
                        total = total - 10 + value
                        self.soft = False
                        
                    else: total = total + value
                else:
                    total = total + value
                    
        return total
    
    def is_BJ(self):
        if self.get_value() == 21:
            if self.num == 2:
                msg = "Blackjack!"
        
                   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        index = 0;
        for x in self.hand:
            x.draw(canvas, [index * 80 + 10, pos])
            index += 1
        
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(rank, suit))
                
        self.num = 52

    def shuffle(self):
        random.shuffle(self.cards)


    def deal_card(self):
        self.num -= 1
        return self.cards.pop(0)
    
    def __str__(self):
        output = ""
        for x in self.cards:
            output = output + " " + str(x)
            
        return output

#define event handlers for buttons
def deal():
    global msg, msg2, in_play, game_deck, player_hand, dealer_hand
    msg = ""
    msg2 = ""
    
    dealer_hand = Hand()
    player_hand = Hand()
    
    if game_deck.num < 4:
        game_deck = Deck()

    game_deck.shuffle()
    
    player_hand.add_card(game_deck.deal_card())
    dealer_hand.add_card(game_deck.deal_card())
    player_hand.add_card(game_deck.deal_card())
    dealer_hand.add_card(game_deck.deal_card())
    
    msg = "NEW GAME"
    print "\n" + msg
    
    print "Player: " + str(player_hand) + " (" + str(player_hand.get_value()) + ")"
    print "Dealer: " + str(dealer_hand) + " (" + str(dealer_hand.get_value()) + ")"
    
    in_play = True

def hit():
    global in_play, player_hand, msg, msg2, game_deck
    msg = ""
    if game_deck.num < 2:
        game_deck = Deck()
        game_deck.shuffle()
    
    
    if in_play == True:
        newCard = game_deck.deal_card()
        
        player_hand.add_card(newCard)
        cur_value = player_hand.get_value()
        
        outcome = "Hit: " + str(player_hand) + " (" + str(cur_value) + ")"

        if cur_value > 21:
            msg = "You have busted!"
            msg2 = "Dealer wins!"
            print msg
            print msg2
            in_play = False
    
    else:
        pass
    
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global dealer_hand, in_play, outcome, msg, msg2
    msg = ""
    
    if in_play == True:
        while dealer_hand.get_value() < 17:
            newCard = game_deck.deal_card()
            dealer_hand.add_card(newCard)
            outcome = "Dealer dealt " + str(newCard) + " (" + str(dealer_hand.get_value()) + ")"
            
            
        outcome = "Dealer has: " + str(dealer_hand) + " (" + str(dealer_hand.get_value()) + ")"
            
        if dealer_hand.get_value() > 21:
            msg = "The dealer busted!"
            msg2 = "Player wins!"
            print msg
            print msg2
            
        else:
            if dealer_hand.get_value() >= player_hand.get_value():
                msg2 = "Dealer wins!"
                print msg2
            else:
                player_hand.is_BJ()
                msg2 = "Player Wins!"
                print msg2
                
        in_play = False        
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    dealer_hand.draw(canvas, 10)
    player_hand.draw(canvas, 300)
    
    canvas.draw_text(str(player_hand.get_value()), [11, 290], 40, "White", "sans-serif")
    canvas.draw_text(msg, [11, 180], 30, "White")
    canvas.draw_text(msg2, [11, 240], 30, "White")
    
    if in_play == True:
        canvas.draw_image(card_back, [CARD_CENTER[0],CARD_CENTER[1]], CARD_SIZE, [10 + CARD_CENTER[0], 10 + CARD_CENTER[1]], CARD_SIZE)
       
    else:
        canvas.draw_text(str(dealer_hand.get_value()), [11, 145], 40, "White", "sans-serif")
        


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
game_deck = Deck()
deal()
frame.start()



# remember to review the gradic rubric