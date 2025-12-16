from tkinter import *
from Point import Point
import pygame as pg
import time, random , Movment ,Graphics

##   global variabels  ##
points = []
game_X = 1600
game_Y = 900
speed = 0
position_x = game_X/2
position_y = game_Y/2
speed_factor = 1.02

##  movement logic ##
def turn_left():
    global position_x
    global speed_factor
    if game_X > position_x > 0:
        position_x -= 1

def turn_right():
    global position_x
    if game_X > position_x> 0:
        position_x+= 1
def turn_up():
    global position_y
    if game_Y > position_y > 0:
        position_y -= 1
def turn_down():
    global position_y
    if game_Y > position_y >0:
        position_y += 1

## movement event check

def check_movement():
    global speed_factor
    global speed
    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE]:
        speed_factor = 1.05
        if speed < 510:
            speed += 1
    if not keys[pg.K_SPACE]:
        if speed > 340:
            speed -= 1
        speed_factor = 1.02
    if keys[pg.K_LEFT]:
        turn_left()
    if keys[pg.K_RIGHT]:
        turn_right()
    if keys[pg.K_UP]:
        turn_up()
    if keys[pg.K_DOWN]:
        turn_down()


screen = pg.display.set_mode((game_X, game_Y))

##return the mouse cord's
def get_mouse_pos():
       x,y= pg.mouse.get_pos()
       return x,y

#draw the points in a loop (deletes points that gone out of the screen)
def draw_points(points):
        for point in points:
                point.draw(screen)
                point.show_trail(screen,Point(game_X,game_Y))
                if not point.is_inside(50, 70, game_X-150, game_Y-150):
                        points.remove(point)
def add_stars(n):
        for i in range(n):
                p = Point(position_x, position_y)
                p.set_velocity(random.randint(0, 360), 0.1)
                points.append(p)

def animation():
        global speed
        for point in points:
                point.move()
                if speed <340:
                        speed += 1

                point.change_radius(point.radius+0.01*point.speed)
                point.change_speed(point.speed*speed_factor)

## Init the game points, cursor, and physics engine

def add_point(point):
        points.append(point)


def __init__():
        pg.init()

##  Main Animation  ##
def gui_show():
        screen.fill((0, 0, 0))
        pg.init()
        __init__()
        running = True
        fps = 60

        frame_count = 0
        while running:
                if frame_count <200:
                        my_font = pg.font.SysFont('Comic Sans MS', 30)
                        text = my_font.render("Use the arrows to move around space, shift to brake and space to speed up", True, (255, 255, 255))
                        screen.blit(text, (300, 300))
                        frame_count += 1

                start_time = time.time()
                for event in pg.event.get():
                        if event.type == pg.QUIT:
                                running = False
                pg.display.update()
                check_movement()
                screen.fill((0, 0, 0))
                draw_points(points)
                add_stars(4)
                animation()
                Graphics.draw_hud(screen,speed)
                time.sleep(0.01)
        # while True:
gui_show()

