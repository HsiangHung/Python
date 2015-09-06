# template for "Stopwatch: The Game"
#  http://www.codeskulptor.org/#user40_olWM9UHG79_3.py


import simplegui


# define global variables

time=0

message = str(time)
ratio = '0/0'

width  =300
height =200

position = [width/2-75,height/2+20]

interval=100

success =0 
counter =0

sec =0 
tenthsec =0


print 'only as t = 5.0x, you will earn a successful stop'


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    global message
    global ratio, counter, success
    global sec, tenthsec
    A  =   time /600
    BC = (time/10) % 60
    B  = BC /10
    C  = BC % 10
    D  = (time - 600*A -10*BC)
    
    sec = C % 5
    tenthsec =D
    
    message = str(A)+':'+str(B)+str(C)+'.'+str(D)
    ratio = str(success)+'/'+str(counter)


     
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start_handler():
    global control
    timer.start()
    control = 1

    
def stop_handler():
    global control
    global counter, success
    global sec, tenthsec  

    timer.stop()
    
    if (control == 1):
      control =0 
      counter = counter+1
#      min  =   time /600
#      sec  =   ((time/10) % 60) % 10
#      tenthsec  = (time - 600*min -10*(time/10) % 60)
    
      if (sec==0 and tenthsec==0) :
         #print tenthsec
         success = success+1
      else:
         pass        
    
    format(time)
    frame.set_draw_handler(draw)

    
    
    
def reset_handler():
    global time, counter, success
    timer.stop()
    time = 0 
    counter =0 
    success =0 
    format(time)
    


# define event handler for timer with 0.1 sec interval

def timer_handler():
    global time
    time = time +1
    format(time)
    #print time
    

# define draw handler

def draw(canvas):
    canvas.draw_text(message, position, 60, 'White')
    canvas.draw_text(ratio, [width-70,40], 35, 'Green')
    
#def count_handler(canvas):
    
    
    
# create frame

frame = simplegui.create_frame('stopwatch',width,height)

format(time)
# register event handlers

frame.add_button('Start', start_handler,100)
frame.add_button('Stop', stop_handler,100)
frame.add_button('Reset', reset_handler,100)


frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, timer_handler)


# start frame

frame.start()


# Please remember to review the grading rubric

