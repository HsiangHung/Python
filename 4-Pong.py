# Implementation of classic arcade game Pong

#  http://www.codeskulptor.org/#user40_5D540oEGaR_7.py


import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]


direction = 'RIGHT'


right_score =0
left_score  =0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists

    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel[0] =  random.randrange(2, 10)
    ball_vel[1] = -random.randrange(2, 8)
       
    #print direction
    if (direction == 'LEFT'):
        ball_vel[0] = -ball_vel[0]

        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global right_score, left_score  # these are ints
    
    paddle1_pos = [      HALF_PAD_WIDTH,HEIGHT/2]
    paddle2_pos = [WIDTH-HALF_PAD_WIDTH,HEIGHT/2]
    paddle1_vel = [0, 0]
    paddle2_vel = [0, 0]
    right_score = 0
    left_score  = 0
    
    randomnumber = random.randrange(0,2)
    if (randomnumber >= 1): 
        direction = 'RIGHT'
    else:
        direction = 'LEFT'
        
    spawn_ball(direction)
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel
    global left_score, right_score
     
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    if (ball_pos[0] <= PAD_WIDTH+BALL_RADIUS):
        # meaning hit the right gutter
        if (ball_pos[1] < paddle1_pos[1]-PAD_HEIGHT/2):
            right_score = right_score + 1
            spawn_ball('RIGHT')
        elif (ball_pos[1] > paddle1_pos[1]+PAD_HEIGHT/2):
            right_score = right_score + 1
            spawn_ball('RIGHT')
        else:
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] =  ball_vel[0]+0.1*ball_vel[0]
       
            
    elif (ball_pos[0] >= WIDTH-PAD_WIDTH-BALL_RADIUS):
        # meaning hit the left gutter
        if (ball_pos[1] < paddle2_pos[1]-PAD_HEIGHT/2):
            left_score = left_score + 1
            spawn_ball('LEFT')
        elif (ball_pos[1] > paddle2_pos[1]+PAD_HEIGHT/2):
            left_score = left_score + 1
            spawn_ball('LEFT')
        else:
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] =  ball_vel[0]+0.1*ball_vel[0]
 

        
    ball_pos[1] += ball_vel[1]
    if (ball_pos[1] <= BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    elif (ball_pos[1] >= HEIGHT-BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
                    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

    
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1] += paddle1_vel[1]
    if (paddle1_pos[1] <= PAD_HEIGHT/2):
        paddle1_pos[1] = PAD_HEIGHT/2
        paddle1_vel[1] =0
    elif (paddle1_pos[1] >= HEIGHT-PAD_HEIGHT/2):
        paddle1_pos[1] = HEIGHT-PAD_HEIGHT/2
        paddle1_vel[1] =0
        
    paddle2_pos[1] += paddle2_vel[1]
    if (paddle2_pos[1] <= PAD_HEIGHT/2):
        paddle2_pos[1] = PAD_HEIGHT/2
        paddle2_vel[1] =0
    elif (paddle2_pos[1] >= HEIGHT-PAD_HEIGHT/2):
        paddle2_pos[1] = HEIGHT-PAD_HEIGHT/2
        paddle2_vel[1] =0

    
    # draw paddles
    canvas.draw_line([WIDTH-PAD_WIDTH/2, paddle2_pos[1]+PAD_HEIGHT/2],[WIDTH-PAD_WIDTH/2, paddle2_pos[1]-PAD_HEIGHT/2], PAD_WIDTH, "White")
    canvas.draw_line([PAD_WIDTH/2, paddle1_pos[1]+PAD_HEIGHT/2],[PAD_WIDTH/2, paddle1_pos[1]-PAD_HEIGHT/2], PAD_WIDTH, "White")
        
        
    # determine whether paddle and ball collide    
  
    
    
    # draw scores
    canvas.draw_text(str(left_score), [150,80],45, 'Green')
    canvas.draw_text(str(right_score), [450,80], 45, 'Green')
    
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    acc = 2
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1] += acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel[1] += acc

        
   
def keyup(key):
    global paddle1_vel, paddle2_vel

    acc = 2
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1] -= acc
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1] -= acc
        
def reset_handler():
    new_game()
        
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.add_button('Restart', reset_handler,100)


# start frame
new_game()
frame.start()

