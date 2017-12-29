import simplegui

frame_Width=500
frame_length=300
Ball_position = [250,150]
Ball_velocity = [3,1]
Ball_radius=13
score=[0,0]
bm=-10
bound_position1=[(0,frame_length/2-33), (0,frame_length/2+33)]
bound_position2=[(frame_Width,frame_length/2-33), (frame_Width,frame_length/2+33)]

def timer_handler11():
    global bound_position1
    bound_position1=[(0,bound_position1[0][1]+bm),(0,bound_position1[1][1]+bm)]
def timer_handler12():
    global bound_position1
    bound_position1=[(0,bound_position1[0][1]-bm),(0,bound_position1[1][1]-bm)]
    
def timer_handler21():
    global bound_position2
    bound_position2=[(frame_Width,bound_position2[0][1]+bm),(frame_Width,bound_position2[1][1]+bm)]
def timer_handler22():
    global bound_position2
    bound_position2=[(frame_Width,bound_position2[0][1]-bm),(frame_Width,bound_position2[1][1]-bm)]

def key_handler1(key):
    if key==simplegui.KEY_MAP['w']:
         timer11.start()
    elif key==simplegui.KEY_MAP['s']:
          timer12.start()
    elif key==simplegui.KEY_MAP['up']:
           timer21.start()
    elif key==simplegui.KEY_MAP['down']:
          timer22.start()
            
def key_handler2(key):
    if key==simplegui.KEY_MAP['w']:
         timer11.stop()
    elif key==simplegui.KEY_MAP['s']:
          timer12.stop()
    elif key==simplegui.KEY_MAP['up']:
           timer21.stop()
    elif key==simplegui.KEY_MAP['down']:
          timer22.stop()     
            
def draw_handler(canvas):
    global Ball_position
    global Ball_velocity
    if Ball_position[0]+Ball_velocity[0]>=frame_Width :
            if Ball_position[1]+Ball_velocity[1]<=bound_position2[1][1] and Ball_position[1]+Ball_velocity[1]>=bound_position2[0][1] :
                Ball_velocity[0] = -Ball_velocity[0]
                Ball_velocity[0]=1.1*Ball_velocity[0]
                Ball_velocity[1]=1.1*Ball_velocity[1]
            else:
                score[0]=score[0]+1
                Ball_position=[250,150]   
                Ball_velocity=[3,1]
    if Ball_position[0]+Ball_velocity[0]<=0 :
            if Ball_position[1]+Ball_velocity[1]<=bound_position1[1][1] and Ball_position[1]+Ball_velocity[1]>=bound_position1[0][1] :
                Ball_velocity[0] = -Ball_velocity[0]
                Ball_velocity[0]=1.1*Ball_velocity[0]
                Ball_velocity[1]=1.1*Ball_velocity[1]
            else:
                score[0]=score[0]+1
                Ball_position=[250,150]
                Ball_velocity=[3,1]
        
    if Ball_position[1]+Ball_velocity[1]>=frame_length or Ball_position[1]+Ball_velocity[1]<=0:
        Ball_velocity[1] = -Ball_velocity[1]  
                
    Ball_position[0]=Ball_position[0]+Ball_velocity[0]
    Ball_position[1]=Ball_position[1]+Ball_velocity[1]
    canvas.draw_circle((Ball_position[0],Ball_position[1]), Ball_radius, 10, 'White','white')
    canvas.draw_line((frame_Width/2,0), (frame_Width/2,frame_length), 2, 'white')
    canvas.draw_line((0,0), (0,frame_length), 2, 'white')
    canvas.draw_line((frame_Width,0),(frame_Width,frame_length), 2, 'white')
    canvas.draw_line(bound_position1[0],bound_position1[1], 20, 'white')
    canvas.draw_line(bound_position2[0],bound_position2[1], 20, 'white')
    score1=str(score[0])
    score2=str(score[1])
    canvas.draw_text( score1, (frame_Width/4,70), 50, 'white')
    canvas.draw_text( score2, (3*frame_Width/4,70), 50, 'white')
    
frame = simplegui.create_frame('Pong', 500, 300)
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(key_handler1)
frame.set_keyup_handler(key_handler2)
timer11 = simplegui.create_timer(70, timer_handler11)
timer12 = simplegui.create_timer(70, timer_handler12)
timer21 = simplegui.create_timer(70, timer_handler21)
timer22 = simplegui.create_timer(70, timer_handler22)

frame.start()
