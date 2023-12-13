from turtle import *
import time
win= Screen()
win.title("Tic Tac Toe")
win.bgcolor("#90c1ec")
t= Turtle()
t.speed(0)
t.hideturtle()
t.goto(0,100)

game =[
    [0 , 0 , 0],
    [0 , 0 , 0],
    [0 , 0 , 0]
]
def polygon(tr ,n ,lenght,width,color1="#544f54",color2="white"):
    tr.pendown()
    tr.begin_fill()
    tr.color(color1,color2)
    for i in range(n):
        tr.fd(lenght)
        tr.lt(90)
        tr.fd(width)
        tr.lt(90) 
    tr.end_fill()  

def border(lenght):
    t.pensize(7)
    t.pencolor("#544f54")
    for i in range(3):
        for j in range(3):
            polygon(t,2,lenght,lenght)
            t.fd(lenght)
        t.penup()
        t.rt(90)
        t.fd(lenght)
        t.rt(90)
        t.fd(lenght*3)
        t.lt(180)
        t.pendown()
    t.penup()
    t.goto(-270,0)
    t.pendown()
    polygon(t,2,190,100)


def draw_o():
    t.rt(90)
    t.fd(30)
    t.lt(90)
    t.pendown()
    t.width(6)
    t.color("#fe4753")
    t.circle(30)

def draw_x():
    t.pendown()
    t.width(6)
    t.color("#0969f1")
    t.lt(45)
    t.fd(50)
    t.bk(100)
    t.fd(50)
    t.lt(90)
    t.fd(50)
    t.bk(100)

def mid(x1 ,x2 ,y1 ,y2):
    xmid=(x1+x2)/2
    ymid=(y1+y2)/2
    t.goto(xmid,ymid)
    t.setheading(0)
#---------------------------------------------
p=Turtle()
p.speed(0)
p.hideturtle()
p.penup()
p.color("#0969f1")
p.goto(-170,35)

def x_Or_o(turn,i,j):

    if(turn %2==0):
            game[i][j]=2
            draw_o()
            p.clear()
            p.color("#0969f1")
            p.write("X turn",align="center",font = ('Courier', 35, 'bold'))

    else:
            game[i][j]=1
            draw_x()
            p.clear()
            p.color("#fe4753")
            p.write("O turn",align="center",font = ('Courier', 35, 'bold'))


# ----------------------------------------------------
# Pen (score)
pen = Turtle()
pen.speed(0)
pen.shape('circle')
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0, 240)
pen.write('Score(X): 0 Score(O): 0', align = 'center', font = ('Courier', 30, 'bold'))
# ----------------------------------------------------

score_x=0
score_o=0

# gameover
def over(score_x,score_o):
        pen.penup()
        pen.goto(-400,-100)
        pen.pensize(9)
        polygon(pen,2,1000,200,"#fbe167","#544f54")
        pen.penup()
        pen.home()
        pen.pendown()
        pen.color("white")
        pen.write("GAME OVER!",align="center",font = ('Courier', 50, 'bold'))
        pen.penup()
        pen.home()
        pen.goto(0,-90)
        if(score_x > score_o):
                pen.color("#0969f1")
                pen.write(" X WON!🥳",align="center",font = ('Courier', 60, 'bold'))
                
        elif (score_x < score_o):
                pen.color("#fe4753")
                pen.write(" O WON!🥳",align="center",font = ('Courier', 60, 'bold'))
        else:
                pen.color("green")
                pen.write(" TIE!🤨",align="center",font = ('Courier', 70, 'bold'))

# increase score 
def gameover(game):
    if game[0][0]>0 and game[0][0] == game[0][1] and game[0][1] == game[0][2]: return game[0][0]
    if game[1][0]>0 and game[1][0] == game[1][1] and game[1][1] == game[1][2]: return game[1][0]
    if game[2][0]>0 and game[2][0] == game[2][1] and game[2][1] == game[2][2]: return game[2][0]
    if game[0][0]>0 and game[0][0] == game[1][0] and game[1][0] == game[2][0]: return game[0][0]
    if game[0][1]>0 and game[0][1] == game[1][1] and game[1][1] == game[2][1]: return game[0][1]
    if game[0][2]>0 and game[0][2] == game[1][2] and game[1][2] == game[2][2]: return game[0][2]
    if game[0][0]>0 and game[0][0] == game[1][1] and game[1][1] == game[2][2]: return game[0][0]
    if game[2][0]>0 and game[2][0] == game[1][1] and game[1][1] == game[0][2]: return game[2][0]
    p = 0
    for i in range(3):
        for j in range(3):
            p += (1 if game[i][j] > 0 else 0)
    if p==9: return 3
    else: return 0
# update score
def update_score():
    pen.clear()
    pen.write('Score(X): {} Score(O): {}'.format(score_x, score_o), align='center', font = ('Courier', 30, 'bold'))
def stop():
        time.sleep(0.5)
        game.clear()
# -----------------------------------------------------
# position of a point
x1=0           
x2=101                    
x3=201         
x4=301          
            
y1=202
y2=102
y3=2
y4=-98
#--------------------------------
turn =0
def play(x,y):
    global turn
    global score_x
    global score_o
    turn+=1
    t.penup()

    if(x>=x1 and x<=x2 and y>=y2 and y<=y1 and game[0][0]==0):
        mid(x1 ,x2 ,y1 ,y2)
        x_Or_o(turn,0,0)
        
    elif(x>=x2 and x<=x3 and y>=y2 and y<=y1 and game[0][1]==0):
        mid(x2 ,x3 ,y1 ,y2)
        x_Or_o(turn,0,1)
        
    elif(x>=x3 and x<=x4 and y>=y2 and y<=y1 and game[0][2]==0):
        mid(x4 ,x3 ,y1 ,y2)
        x_Or_o(turn,0,2)
        
    elif(x>=x1 and x<=x2 and y>=y3 and y<=y2 and game[1][0]==0):
        mid(x1 ,x2 ,y3 ,y2)
        x_Or_o(turn,1,0)
        
    elif(x>=x2 and x<=x3 and y>=y3 and y<=y2 and game[1][1]==0):
        mid(x2 ,x3 ,y3 ,y2)
        x_Or_o(turn,1,1)
        
    elif(x>=x3 and x<=x4 and y>=y3 and y<=y2 and game[1][2]==0):
        mid(x4 ,x3 ,y3 ,y2)
        x_Or_o(turn,1,2)
        
    elif(x>=x1 and x<=x2 and y>=y4 and y<=y3 and game[2][0]==0):
        mid(x1 ,x2 ,y4 ,y3)
        x_Or_o(turn,2,0)
        
    elif(x>=x2 and x<=x3 and y>=y4 and y<=y3 and game[2][1]==0):
        mid(x2 ,x3 ,y4 ,y3)
        x_Or_o(turn,2,1)
        
    elif(x>=x3 and x<=x4 and y>=y4 and y<=y3 and game[2][2]==0):
        mid(x4 ,x3 ,y4 ,y3)
        x_Or_o(turn,2,2)
        
    # Decide the winner 
    res = gameover(game)
    if res==1:
        score_x+=1
        update_score()
        over(score_x,score_o)
        stop()
    elif res==2:
        score_o+=1
        update_score()
        over(score_x,score_o)   
        stop()
    elif turn==9:
         over(score_x,score_o)   
         stop()
         

# ************************
#def print_pos(x,y):
#     print(x,y)

#win.onclick(print_pos)
border(100)
p.write("X turn",align="center",font = ('Courier', 35, 'bold'))
win.onclick(play,1,True)

done()