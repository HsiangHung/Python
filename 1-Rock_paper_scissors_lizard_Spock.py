# Rock-paper-scissors-lizard-Spock template

# http://www.codeskulptor.org/#user40_3fx2fdK0LU_3.py


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random


# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    pass
 
    if (name=='rock'):
       number=0
    elif (name=='Spock'):
       number=1
    elif (name=='paper'):
       number=2
    elif (name=='lizard'):
       number=3
    else:
       number=4
   
    return number

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    pass

    if (number==0):
       name='rock'
    elif (number==1):
       name='Spock'
    elif (number==2):
       name='paper'
    elif (number==3):
       name='lizard'
    else:
       name='scissors'
   
    return name
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    pass
    
    # print a blank line to separate consecutive games
    print 
    
    # print out the message for the player's choice
    print 'Player chooses',player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number=name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number=random.randrange(0,5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice=number_to_name(comp_number)

    # print out the message for computer's choice
    print 'Computer chooses',comp_choice
    
    # compute difference of comp_number and player_number modulo five
    difference = (player_number - comp_number) % 5
    
    if (difference <= -3 ):
        difference = differene % 5
    elif (difference >=3 ):
        difference = difference -5
    else: 
        difference = difference
   

    # use if/elif/else to determine winner, print winner message
    if (difference > 0):
      print 'Player wins!'
    elif (difference < 0):
      print 'Computer wins!'
    else:
      print 'Player and computer tie!'
    
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric



