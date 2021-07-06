import pygame as pg
import sys
import time
import random

from pygame.locals import *

FPS = 5
pg.init()

fpsClock = pg.time.Clock()
clock = pg.time.Clock()
pg.key.set_repeat(1, 30)

WINDOW_WIDTH, WINDOW_HEIGHT = 480, 360
window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
surface = pg.Surface(window.get_size())
surface = surface.convert()
surface.fill((255,255,255))

GRID_SIZE=10
GRID_WIDTH = WINDOW_WIDTH / GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT / GRID_SIZE
UP    = (0, -1)
DOWN  = (0, 1)
LEFT  = (-1, 0)
RIGHT = (1, 0)
    
window.blit(surface, (0,0))

def draw_box(surf, color, pos):
    r = pg.Rect((pos[0], pos[1]), (GRID_SIZE, GRID_SIZE))
    pg.draw.rect(surf, color, r)

class Eagle():
    def __init__(self, name):
        self.charge()
        self.name = name
        self.color = (64,128,64)

    def get_position(self):
        return self.positions[0]

    def charge(self):
        self.strength = 1
        self.positions =  [((GRID_WIDTH / 3), (WINDOW_HEIGHT / 3))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def point(self, pt):
        if self.strength > 1 and (pt[0] * -1, pt[1] * -1) == self.direction:
            return
        else:
            self.direction = pt

    def fly(self):
        cur = self.positions[0]
        x, y = self.direction
        update = (((cur[0]+(x*GRID_SIZE)) % WINDOW_WIDTH), (cur[1]+(y*GRID_SIZE)) % WINDOW_HEIGHT)
        if len(self.positions) > 2 and update in self.positions[2:]:
            self.charge()
        else:
            self.positions.insert(0, update)
            if len(self.positions) > self.strength:
                self.positions.pop()
    
    def plot(self, surf):
        for pos in self.positions:
            draw_box(surf, self.color, pos)

class Prey():
    def __init__(self):
        self.position = (0,0)
        self.color = (0,0,225)
        self.randomize()

    def randomize(self):
        self.position = (random.randint(0, GRID_WIDTH-1) * GRID_SIZE, random.randint(0, GRID_HEIGHT-1) * GRID_SIZE)

    def plot(self, surf):
        draw_box(surf, self.color, self.position)

def eat(eagle, prey):
    if eagle.get_position() == prey.position:
        eagle.strength += 1
        prey.randomize()

if __name__ == '__main__':
    eagle = Eagle("Henry")
    prey = Prey()
    
    while True:

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    eagle.point(UP)
                elif event.key == K_DOWN:
                    eagle.point(DOWN)
                elif event.key == K_LEFT:
                    eagle.point(LEFT)
                elif event.key == K_RIGHT:
                    eagle.point(RIGHT)


        surface.fill((255,255,255))
        eagle.fly()
        eat(eagle, prey)
        eagle.plot(surface)
        prey.plot(surface)

        font = pg.font.Font(None, 36)
        text = font.render(str(eagle.name), 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = 50
        surface.blit(text, textpos)
        window.blit(surface, (0,0))

        pg.display.flip()
        pg.display.update()
        fpsClock.tick(FPS + eagle.strength/3)
