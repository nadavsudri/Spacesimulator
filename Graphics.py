import pygame as pg

def draw_hud(screen,speed):

    #green frame
    pg.draw.line(screen,(0,128,0),(30,50),(1550,50),3)
    pg.draw.line(screen,(0,128,0),(30,50),(30,850),3)
    pg.draw.line(screen,(0,128,0),(30,850),(1550,850),3)
    pg.draw.line(screen,(0,128,0),(1550,50),(1550,850),3)

    #cross
    pg.draw.line(screen,(0,200,0),(800,450),(825,450),5)
    pg.draw.line(screen,(0,200,0),(800,450),(800,475),5)
    pg.draw.line(screen,(0,200,0),(800,450),(775,450),5)
    pg.draw.line(screen,(0,200,0),(800,450),(800,425),5)

    #speed
    my_font = pg.font.SysFont('Comic Sans MS', 20)
    text = my_font.render(f"Speed: {speed} Km/h", True, (255, 255, 255))
    screen.blit(text, (100, 800))

    ## spedometer bar
    min = 0
    max = 510
    pg.draw.line(screen, (0, 200, 0), (30, 840), (speed, 840), 3)


