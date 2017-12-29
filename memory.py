import simplegui
import random

list= [1,2,2,3,7,1,5,8,3,5,4,4,6,7,6,8]
list_turn=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
state=0
last_number=-1

def mouse_handler(position):
    
    global state
    global list_turn
    global last_number
    number=position[0]/50
    if state==0:
        state=1
        list_turn[number]=1
        last_number=number
        
    elif state==1:
        state=2
        list_turn[number]=1
        if list[last_number]==list[number]:
            list_turn[number]=2
            list_turn[last_number]=2
        
    else :
        count=0
        for i in list_turn:
            if i==1 :
                list_turn[count]=0
            count=count+1
        state=1
        list_turn[number]=1
        last_number=number


def button_handler():
    global state
    global list
    global list_turn
    list=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    list_turn=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    j=0 
    state=0
    for i in list:
        count=3
        while count>=2:
            count=0        
            rnumber=random.randrange(1,9)
            for k in list:
                if k==rnumber:
                    count=count+1
            if count<=1:
                list[j]=rnumber
                j=j+1
     
    
def draw_handler(canvas): 
    width=20
    cishu=0
    for i in list :
        if list_turn[cishu] == 1 or list_turn[cishu]==2:
            canvas.draw_text(str(i), (width, 60), 40, 'white')
            canvas.draw_line((width+30, 0), (width+30, 100), 1, 'orange')
        
        else :
            canvas.draw_line((width+30, 0), (width+30, 100), 1, 'orange')
        
        width+=50
        cishu+=1
    
    

frame = simplegui.create_frame("Memory", 800, 100)
frame.set_draw_handler(draw_handler)
button1 = frame.add_button('Reset', button_handler)
frame.set_mouseclick_handler(mouse_handler)


frame.start()