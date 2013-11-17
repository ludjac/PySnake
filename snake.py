import pygame, sys, time
from pygame.locals import *
import numpy as N
from random import randint

CAPTION = 'Snake'
RES = (640, 640)
WAIT = 0.5
PIXEL = 16
WALL = []
FOOD = []
# Init
pygame.init()

# Window set up
window = pygame.display.set_mode(RES)
pygame.display.set_caption(CAPTION)

# Define Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)

def draw_pixel(coord, color):
    pygame.draw.rect(window, color, (N.dot(coord, PIXEL), (PIXEL,  PIXEL)))

class board():
    """ Play board """
    def __init__(self, RES,  PIXEL):
        window.fill(GREEN)
    
        WALL.extend([(i, 0) for i in xrange(RES[0]/PIXEL)])
        WALL.extend([(0, i) for i in xrange(RES[1]/PIXEL)])
        WALL.extend([(i, RES[0]/PIXEL-1) for i in xrange(RES[0]/PIXEL)])
        WALL.extend([(RES[1]/PIXEL-1, i) for i in xrange(RES[1]/PIXEL)]) 
    
        for coord in WALL:
            draw_pixel(coord, RED)
        pygame.display.flip()

class snake():
    """ Snake class """

    def __init__(self):
        self.head = (20, 20)
        self.vel = [1,0]
        self.body = [self.head]
        self.length = 1
        draw_pixel(self.head, BLUE)
        pygame.display.flip()

    def move(self):
        draw_pixel(self.body[-1], GREEN)
        if not self.isbug():
            self.body.pop()
        self.head = (self.head[0]+self.vel[0], self.head[1]+self.vel[1])
        self.body = [self.head]+self.body[0:]
        self.isdead()
        for coords in self.body:
            draw_pixel(coords, BLUE)
        pygame.display.flip()
        

    def isdead(self):
        if self.head in WALL:
            exit()
        if self.head in self.body[1:]:
            exit()

    def isbug(self):
        if FOOD[0] in self.body:
            FOOD.pop()
            create_food()
            return True
        else:
            return False


def main_loop():
    while True:
        time.sleep(WAIT)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_UP:
                    if SNAKE.vel != [0, 1]:
                        SNAKE.vel = [0,-1]
                elif event.key == pygame.K_DOWN:
                    if SNAKE.vel != [0, -1]:
                        SNAKE.vel = [0, 1]
                elif event.key == pygame.K_RIGHT:
                    if SNAKE.vel != [-1, 0]:
                        SNAKE.vel = [1,0]
                elif event.key == pygame.K_LEFT:
                    if SNAKE.vel != [1, 0]:
                         SNAKE.vel = [-1,0]
        SNAKE.move()

def create_food():
    FOOD.extend([(randint(1,RES[0]/PIXEL-2), randint(1, RES[1]/PIXEL-2))])
    draw_pixel(FOOD[0], PURPLE)

def exit():
    time.sleep(1)
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    BOARD = board(RES, PIXEL)
    #init()
    create_food()
    SNAKE = snake()
    main_loop()

#car = pygame.image.load('car.png')
#screen.blit(car, (50, 100))
#pygame.display.flip()

