import pgzrun 
import random 

TITLE = 'Flappy ball By: Avira'
WIDTH = 800 
HEIGHT = 600
gravity = 2000
#pixels per second

class Ball():
    def __init__(self,intial_x, intial_y, color, radius):
        self.x = intial_x
        self.y = intial_y
        self.color = color
        self.vx = 200
        self.vy = 0
        self.radius = radius
    
    def draw(self):
        pos = (self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,self.color)

ball1 = Ball(400,300, 'pink', 40)
ball2 = Ball(300,400, 'light blue' , 70)

def draw():
    screen.clear()
    ball1.draw()
    ball2.draw()

def update(dt):

    uy = ball1.vy
    ball1.vy += gravity*dt
    ball1.y += (uy+ball1.vy)*0.5*dt
    
    if ball1.y > HEIGHT - ball1.radius:
        ball1.y = HEIGHT - ball1.radius
        ball1.vy = - ball1.vy * 0.9
    
    ball1.x += ball1.vx * dt
    if ball1.x > WIDTH - ball1.radius or ball1.x < ball1.radius:
        ball1.vx = - ball1.vx

    uy = ball2.vy
    ball2.vy += gravity * dt
    ball2.y += (uy + ball2.vy) * 0.5 * dt

    if ball2.y > HEIGHT - ball2.radius:
        ball2.y = HEIGHT - ball2.radius
        ball2.vy = - ball2.vy * 0.9

    ball2.x += ball2.vx * dt
    ball2.x += ball2.vx * dt
    if ball2.x > WIDTH - ball2.radius or ball2.x < ball2.radius:
        ball2.vx = - ball2.vx

    uy = ball2.vy
    ball2.vy += gravity * dt
    ball2.y += (uy + ball2.vy) * 0.5 * dt


def on_key_down(key):
    
    if key == keys.SPACE:
        ball1.vy = -300
        ball2.vy = -600


pgzrun.go()