from tkinter import *
import time
import random
from winsound import *

tk = Tk()
canvas = Canvas(tk, width=900, height=600) 
tk.title("Aliens attack")
images = PhotoImage(file='img/startpage.gif')
b1 = PhotoImage(file='img/play.gif')
b2 = PhotoImage(file='img/how.gif')
b3 = PhotoImage(file='img/exit.gif')
b4 = PhotoImage(file='img/menu.gif')
b5 = PhotoImage(file='img/playagain.gif')
how = PhotoImage(file='img/howto.gif')
over = PhotoImage(file='img/gameover.gif')

canvas.pack()
class Start:
    def __init__(self,canvas):
        global bplay,bhow,bexit,start_game
        self.canvas = canvas
        bplay = Button(tk,image=b1,command=playgame)
        bhow = Button(tk,image=b2,command=howplay)
        bexit = Button(tk,image=b3,command=close)
        self.bplay = bplay
        self.bhow = bhow
        self.bexit = bexit
        self.x = 0
        self.y = 600
        start_game = canvas.create_image(self.x,self.y, anchor=SW,
                                             image=images)
        self.start_game = start_game
    def button(self):
        
        self.bplay.place(x=220,y=300)
        self.bhow.place(x=500,y=300)
        self.bexit.place(x=350,y=400)
class BG:
    def __init__(self,canvas):
        self.canvas = canvas
        self.images = PhotoImage(file='img/bg.gif')
        self.x = 0    
        self.y = 600
        self.vx = 3
        self.canvas_id = canvas.create_image(self.x, self.y, anchor=SW,
                                             image=self.images)
        
    def move(self):
        if start == 1:
            self.x -= self.vx
            self.canvas.move(self.canvas_id, -self.vx, 0)
        if self.x <= -1000:
            self.vx = 8
        elif self.x <= -8000:
            self.vx = 15
class ufo:
    def __init__(self, canvas):
        self.canvas = canvas
        self.images = PhotoImage(file='img/ufo.gif')
        self.x = 150
        self.y = 300   
        self.vx = 0
        self.vy = 0  
        self.canvas_id = canvas.create_image(self.x,self.y, anchor=SW,
                                             image=self.images)
    def move(self):
        global life,start
        self.canvas.move(self.canvas_id, self.vx, self.vy)
        if start == 1:
            self.y += self.vy
        if self.y >= 600:
            canvas.delete(self.canvas_id)
            end()
            start = 2
        elif self.y < 600 and self.y > 0:
            self.vy += 2
        elif self.y <= -100:
                canvas.delete(self.canvas_id)
                life = 0
                start = 2
                end()
class Alien:
        def __init__(self, canvas,speed=10):
            self.canvas = canvas
            self.speed = speed
            self.images = {'n1':PhotoImage(file='img/a1.gif'),
                           'n2':PhotoImage(file='img/a2.gif'),
                           'n3':PhotoImage(file='img/a3.gif'),
                           'n4':PhotoImage(file='img/a4.gif'),
                           'n5':PhotoImage(file='img/a5.gif'),
                           'n6':PhotoImage(file='img/a6.gif'),
                           'n7':PhotoImage(file='img/a7.gif')}
            self.char = random.choice(['n1','n2','n3','n4','n5','n6','n7'])
            self.position=random.choice([150,350,450])
            self.x = 1000 
            self.y = self.position   
            self.vx = 0
            self.vy = 0  
            self.canvas_id = canvas.create_image(self.x,self.y, anchor='center',
                                                 image=self.images[self.char])
        
        def move(self):
            global start
            global score
            global life
            global xxx
            self.x -= self.speed
            self.canvas.move(self.canvas_id, -self.speed, 0)
            for bu in bull:
                if (bu.x+100) > self.x > (bu.x-100) and (bu.y+50) > self.y > (bu.y-50):
                    canvas.delete(self.canvas_id)
                    aliens.remove(self)
                    score += 1
                    canvas.delete(bu.canvas_id)
                    bull.remove(bu)
                    PlaySound("sound/explosion.wav", SND_ASYNC)
            if (u.x+100) > self.x > (u.x-50) and (u.y+45) > self.y > (u.y-45) and xxx==0:
                PlaySound("sound/ufo.wav", SND_ASYNC)
                canvas.delete(u.canvas_id)
                start = 2
                end()
                xxx=1
            if self.x < 0:
                canvas.delete(self.canvas_id)
                aliens.remove(self)
                life -= 1
            if life <= 0:
                start = 2
                end()
                
class Bullet:
    def __init__(self, canvas):
        self.canvas = canvas
        self.images = PhotoImage(file='img/bullet.gif')
        self.x = u.x+100
        self.y = u.y+25  
        self.vx = 20
        self.vy = 0  
        self.canvas_id = canvas.create_image(self.x,self.y, anchor=SW,
                                             image=self.images)
    def move(self):
        self.canvas.move(self.canvas_id, self.vx, self.vy)         
        self.x += self.vx
        if self.x >= 900:
            canvas.delete(self.canvas_id)
            bull.remove(self)
        if self.y >= a.y and self.x >= a.x:
            canvas.delete(self.canvas_id)
            bull.remove(self)
            canvas.delete(a.canvas_id)
            aliens.remove(a.self)
        if self.y >= 580:
            self.vy = 0 
        else:
            self.vy = 0
global End_game
def end():
    global bplaygame,End_game,bplayagain,xxx,bmenu
    bplayagain = Button(tk,image=b5,command=playgame)
    bmenu = Button(tk,image=b4,command=begin)
    End_game = canvas.create_image(0,600, anchor=SW,image=over)
    bplayagain.place(x=230,y=300)
    bmenu.place(x=480,y=300)
    xxx = 0
def begin():
    global start,aliens
    PlaySound("sound/click.wav", SND_ASYNC)
    Score()
    canvas.delete(End_game)
    bplayagain.destroy()
    bmenu.destroy()
    aliens = []
    u.y = 0
    s = Start(canvas)
    s.button()
    start = 0
def close():
    PlaySound("sound/click.wav", SND_ASYNC)
    tk.destroy()
def howplay():
    global bmenu,howpage
    bplay.destroy()
    bhow.destroy()
    bexit.destroy()
    canvas.delete(start_game)
    PlaySound("sound/click.wav", SND_ASYNC)
    bmenu = Button(tk,image=b4,borderwidth=2,command=menu)
    howpage = canvas.create_image(0,600, anchor=SW,image=how)
    bmenu.place(x=10,y=530)
def menu():
    PlaySound("sound/click.wav", SND_ASYNC)
    s = Start(canvas)
    s.button()
    bmenu.destroy()
    canvas.delete(howpage)
    canvas.delete(game_over)
def playgame():
    global u,bg,a,start,score,life,End_game,xxx
    canvas.delete(start_game)
    if xxx == 1:
        canvas.delete(End_game)
        bplayagain.destroy()
        bmenu.destroy()
        xxx=0
    PlaySound("sound/click.wav", SND_ASYNC)
    bplay.destroy()
    bhow.destroy()
    bexit.destroy()
    u = ufo(canvas)
    a = Alien(canvas)
    start = 1
    score = 0
    life = 5
def Score():
    global label1,label2
    label1.destroy()
    label2.destroy()
    start = 0
def move_ufo(event):
    if event.keysym =='space':
        if start == 1:
            if u.y >= 20:
                u.vy = -15
canvas.bind_all('<KeyPress-space>', move_ufo)
def Shoot(event):
    if start == 1:
        PlaySound("sound/sh1.wav", SND_ASYNC)
        bull.append(Bullet(canvas))
canvas.bind('<Button-1>', Shoot)
bull = []       
aliens = []
score = 0
life = 5
start = 0
xxx = 0
u = ufo(canvas)
bg = BG(canvas)
s = Start(canvas)
s.button()
while True:
    for i in range(100):
        if len(aliens) == 0:
            if start == 1:
                if bg.x > -1000:
                    aliens.append(random.choice([Alien(canvas),
                    Alien(canvas,5),
                    Alien(canvas,7)]))
                elif bg.x <= -1000:
                    aliens.append(random.choice([Alien(canvas),
                    Alien(canvas,10),
                    Alien(canvas,11)]))
                elif bg.x <= -8000:
                    aliens.append(random.choice([Alien(canvas),
                    Alien(canvas,16),
                    Alien(canvas,17)]))
        if len(aliens) == 1:
            if start == 1:
                if bg.x > -1000:
                    aliens.append(random.choice([Alien(canvas),
                    Alien(canvas,8),
                    Alien(canvas,9)]))
                elif bg.x <= -1000:
                    aliens.append(random.choice([Alien(canvas),
                    Alien(canvas,12),
                    Alien(canvas,13)]))
                elif bg.x <= -80000:
                    aliens.append(random.choice([Alien(canvas),
                    Alien(canvas,18),
                    Alien(canvas,19)]))
        if len(aliens) == 2:
            if start == 1:
                if bg.x > -1000:
                    aliens.append(random.choice([Alien(canvas),
                    Alien(canvas,4),
                    Alien(canvas,3)]))
                elif bg.x <= -1000:
                    aliens.append(random.choice([Alien(canvas),
                    Alien(canvas,14),
                    Alien(canvas,15)]))
                elif bg.x <= -8000:
                    aliens.append(random.choice([Alien(canvas),
                    Alien(canvas,20),
                    Alien(canvas,21)]))
    for d in aliens:
        if bg.x < -80 and start == 1:
            d.move()
    for rocket in bull:
        rocket.move()
    if start == 1:
        label1.destroy()
        label2.destroy()
        label1 = Label(tk, font='Hobostd',text='Score : '+ str(score)+'        ')
        label1.place(x=330,y=20)
        label2 = Label(tk, font='Hobostd',text='Life : '+ str(life)+'   ')
        label2.place(x=500,y=20)
    if start == 0:
        label1 = Label(tk, font='Hobostd',text='Score : '+ str(score)+'        ')
        label1.place(x=330,y=20)
        label2 = Label(tk, font='Hobostd',text='Life : '+ str(life)+'   ')
        label2.place(x=500,y=20)
        Score()
    if start == 1:
        u.move()
    bg.move()
    tk.update()
    time.sleep(0.03)
    
