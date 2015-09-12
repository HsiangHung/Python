# Mini-project #6 - Blackjack
# http://www.codeskulptor.org/#user40_qY5U2lGJljCJVME_13.py

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
outcome = ""
score = 0

total_score =0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

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
        self.suit = []
        self.rank = []
        #pass	# create Hand object

    def __str__(self):
        card =""
        for i in range(len(self.rank)):
             card += str(self.suit[i]+self.rank[i])+' '  
        return card
        #pass	# return a string representation of a hand

    def add_card(self, card):
        self.suit += card.get_suit()
        self.rank += card.get_rank()
        #pass	# add a card object to a hand
        
    def get_posit_player(self,index):
        #print 'player:',self,index        
        self.xpos.append(50+index*100) 
        
    def get_posit_dealer(self,index):
        #print 'dealer:',self,index        
        self.xpos.append(50+index*100) 

    def get_value(self,score):
        #print self, self.rank[-1],'ok?'
        card_score = VALUES[self.rank[-1]]
        if (self.rank[-1] == 'A'):
            if (score < 11):
                card_score += 10
        return card_score
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        #pass	# compute the value of the hand, see Blackjack video
   
#    def draw(self, canvas, pos):
#        pass	# draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 

class Deck:
    def __init__(self):
        self.suit = []
        self.rank = [] 
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                self.suit.append(SUITS[i])
                self.rank.append(RANKS[j])    
        #print len(self.suit)
        #pass	# create a Deck object

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.suit)
        random.shuffle(self.rank)

    def deal_card(self):
        deal_suit = self.suit[-1]
        deal_rank = self.rank[-1]
        self.suit.pop()
        self.rank.pop()
        return deal_suit+deal_rank
        #pass	# deal a card object from the deck
    
    def __str__(self):
        card = ""
        for i in range(len(self.suit)):
            card += str(self.suit[i]+self.rank[i])+' '
        return card
        #pass	# return a string representing the deck

#define event handlers for buttons
def deal():
    #global draw
    global outcome, in_play
    global player, dealer
    global player_score, dealer_score
    global player_bust,  dealer_bust
    global total_score
    global deck
    global player_cardnum, dealer_cardnum

    if (in_play == True):
        total_score -= 1
    
    player = Hand()
    dealer = Hand()
    
    player_score =0
    dealer_score =0
    player_bust=0
    dealer_bust=0
    
    player_cardnum=-1
    dealer_cardnum=-1
    
    player.xpos = []
    player.ypos = 370
    dealer.xpos = []
    dealer.ypos = 170
    in_play = True
    
    deck = Deck()
    deck.shuffle()
    for i in range(2):
        player_cardnum += 1
        card = deck.deal_card()
        player.add_card(Card(card[0],card[1]))
        player_score += player.get_value(player_score)        
        player.get_posit_player(player_cardnum)
        #print card, player_score
        print player
        #print deck
        #print 
        # ----------------------------
        dealer_cardnum += 1
        card = deck.deal_card()
        dealer.add_card(Card(card[0],card[1]))
        dealer_score += dealer.get_value(player_score)
        dealer.get_posit_dealer(dealer_cardnum)
        #print card, dealer_score
        print dealer
        #print deck

      

def hit():
    global in_play
    global player_score, player_bust
    global deck, player
    global player_cardnum
    global total_score
    
    if (player_score <= 21):
        card = deck.deal_card()
        player.add_card(Card(card[0],card[1]))
        player_score += player.get_value(player_score)
        player_cardnum += 1
        player.get_posit_player(player_cardnum)
        print card, card[0],card[1],player_score
        print player
        print deck
        print 
        
    if (player_score >21):
        print "You have busted!"
        player_bust = 1
        in_play = False
        total_score -= 1
        
    #pass	# replace with your code below
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global in_play
    global deck, dealer
    global dealer_score, dealer_bust, dealer_cardnum
    global player_score, player_bust
    global total_score
    if (player_bust==1):
        print 'Player has busted'
    else:
        while (dealer_score <17):
            card = deck.deal_card()
            dealer.add_card(Card(card[0],card[1]))
            dealer_score += dealer.get_value(dealer_score)
            dealer_cardnum += 1
            dealer.get_posit_dealer(dealer_cardnum)
            print card, card[0],card[1],dealer_score
            print dealer
            print deck
            
        in_play =False
        if (dealer_score <= 21):
           if (dealer_score >= player_score):
             total_score -= 1
           else:
             total_score += 1
        elif (dealer_score >21):
            print 'Dealer has busted'
            dealer_bust = 1
            total_score += 1
    #pass	# replace with your code below
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global in_play, total_score
    for i in range(len(player.xpos)):
        card = Card(player.suit[i], player.rank[i])
        card.draw(canvas, [player.xpos[i], player.ypos])

    for i in range(len(dealer.xpos)):
        card = Card(dealer.suit[i], dealer.rank[i])
        card.draw(canvas, [dealer.xpos[i], dealer.ypos])  
        
    canvas.draw_text('Blackjack', [160,80],45, 'Blue')
    canvas.draw_text('Dealer', [100,140],35, 'Black')
    canvas.draw_text('Player', [100,340],35, 'Black')
    canvas.draw_text('Score:'+str(total_score), [400,120],35, 'Pink')
    
    if (in_play == False):
      if (player_bust ==1):
         canvas.draw_text('Player has busted! Dealer wins', [50,540],40, 'Yellow')
      elif (dealer_bust==1):
         canvas.draw_text('Dealer has busted! Player wins', [50,540],40, 'Yellow')
      else:
         if (dealer_score >= player_score):
           canvas.draw_text('Dealer wins!', [220,540],40, 'Yellow')  
         else:
           canvas.draw_text('Player wins', [220,540],40, 'Yellow')
      canvas.draw_text('New Deal?', [300,340],35, 'Black') 
    else:
      canvas.draw_text('Hit or Stand?', [300,340],35, 'Black')
      canvas.draw_image(card_back, (72/2, 96/2), CARD_SIZE, (86, 220), CARD_SIZE)
        
#    exit()


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)




# get things rolling
deal()
#print player, player_score
#print dealer, dealer_score
#print ' '
#print 'start a new game'
#print ' '
#hit()
#print
#print 'dealer side'
#print
#stand()
frame.start()


# remember to review the gradic rubric