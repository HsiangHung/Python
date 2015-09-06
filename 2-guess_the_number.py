# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

#  http://www.codeskulptor.org/#user40_r6pMie5ZG0_7.py


import simplegui
import random



# helper function to start and restart the game
def new_game(upper):
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randrange(0, upper)
    #print "secret number=",secret_number
    #print ""
    pass


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global n_max, n, upper
    print ""
    print "  ========================"
    print "-- start game in range of [0,100) --"
    n_max=7
    n=7
    upper=100
    print "You have",n, "times to guess"
    new_game(upper)
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global n_max, n, upper
    print ""
    print "  ========================"
    print "-- start game in range of [0,1000) --"
    n_max=10
    n=10
    upper=1000
    print "You have",n, "times to guess:"
    new_game(upper)    
    pass
    
def input_guess(guess):
    # main game logic goes here	
    global number, n_max, n, upper
    number = int(guess)
    n = n - 1
    output()
    
    if (number > secret_number):
        print "Lower"
    elif (number < secret_number):
        print "Higher"
    else: 
        print "Correct"

    
    
    if (n >= 1):
        print "Number of remaining guesses is", n
    elif (n == 0 ):
        print "This is the last chance!"
        if (number != secret_number):
           n = n_max
           print ""
           print " -- start new game ---"
           print "You have",n, "times to guess"
           new_game(upper)
            
        
    pass


def output():
    print ""
    print "Guess was", number


    
# create frame

frame = simplegui.create_frame('test', 150, 150)


# register event handlers for control elements and start frame


#frame.add_button('Print',output, 100)

frame.add_button('Range is [0,100)' , range100, 120)
frame.add_button('Range is [0,1000)', range1000, 120)

frame.add_input('Enter guess', input_guess, 80)



# call new_game 
#new_game(100)


# always remember to check your completed program against the grading rubric

