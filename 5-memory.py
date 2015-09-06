# implementation of card game - Memory

# http://www.codeskulptor.org/#user40_gJOQVsj1nn_10.py

import simplegui
import random

dock=range(8)
dock.extend(dock)

expose = [False for i in range(16)]
card_pos = [0,0]
card_faceup = [0,0,0]
state =0 
count =0 

# helper function to initialize globals
def new_game():
    global state, expose, count
    random.shuffle(dock)    
    expose = [False for i in range(16)]
    state =0 
    count =0
    label.set_text('Truns ='+str(count))
    frame.set_draw_handler(draw)
    #print dock

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global expose, card_pos, state, card_faceup
    global count
    card_pos = list(pos)
    #print card_pos
    card_select = (card_pos[0]/50)
    if expose[card_select] == False:
        expose[card_select] = True  
        if state == 0:
           state = 1      ## here state=1 means one card fare face up
           card_faceup[0]=card_select
        elif state == 1:
           state = 2      ## state ==2 means two cards are face up now
           card_faceup[1]=card_select
           count += 1
           label.set_text('Turns ='+str(count)) # print the counter
        else:
           if dock[card_faceup[0]] != dock[card_faceup[1]]:
               expose[card_faceup[0]] = False
               expose[card_faceup[1]] = False
           state = 1      ## state ==1 means odd cards are face up now
           card_faceup[0]=card_select

    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    numb_posit =15
    card_posit =25
    for i in range(16):
      text = str(dock[i])
      canvas.draw_text(text, (numb_posit, 70), 50, 'White')
      numb_posit += 50
      if expose[i]== False:
         canvas.draw_line([card_posit, 0], [card_posit, 100], 49, 'Green')
      card_posit += 50
    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric