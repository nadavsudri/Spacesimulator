import pygame as pg
import math

class Point:
    def __init__(self,x,y):
        self.speed = None
        self.angle = None
        self.radius = 1
        self.x = x
        self.y = y

    def draw(self,screen):
        pg.draw.circle(screen,(255,255,255),(self.x,self.y),self.radius)
        # pg.draw.circle(screen,(0+self.speed*10,0+self.speed*10,0+self.speed*10),(self.x,self.y),self.radius)

    def change_radius(self,radius):
        self.radius = radius

    def change_speed(self,speed):
        self.speed = speed

    def show_trail(self,screen,center):
        trail_size = math.floor(self.speed)
        for i in range(trail_size):
            decrimentor = (255/trail_size)*i
            pg.draw.circle(screen,(255-decrimentor,255-decrimentor,255-decrimentor)
                           ,(self.x-i*self.speed*math.cos(math.radians(self.angle)),self.y-i*self.speed*math.sin(math.radians(self.angle)))
                           ,self.radius-(i*(self.radius/trail_size))
                           )

    def distance(self,other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

    def set_velocity(self,angle,speed):
        self.angle = angle
        self.speed = speed

    def move(self):
        self.x += self.speed*math.cos(math.radians(self.angle))
        self.y += self.speed*math.sin(math.radians(self.angle))

    def is_inside(self,x,y,w,h):
        return x < self.x < x + w and y < self.y < y + h

    def reset(self,x,y):
        self.x = x
        self.y = y
        self.radius = 1
        self.speed = 0.1
        print("reset")


