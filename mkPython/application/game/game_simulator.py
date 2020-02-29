import pygame
from sys import exit
import random
import time
import threading

WIDTH = 256
HEIGHT = 512
TITLE = "16 * 8 点阵游戏模拟机"

ROW = 16
CLO = 8

BACK_COLOR = (10, 20, 30)
POINT_COLOR = (0, 0, 200)

def config(width, height, row = 8, clo = 16, b_clolor = (1, 2, 3), itle = ""):
    global WIDTH, HEIGHT, TITLE, ROW, CLO
    WIDTH = width
    HEIGHT = height
    TITLE = title

    ROW = row
    CLO = clo

    BACK_COLOR = b_clolor

class Point():
    def __init__(self, row, clo):
        self.row = row
        self.clo = clo

    def copy(self):
        return Point(row=self.row, clo=self.clo)

def rect(point, color):
    global WIDTH, HEIGHT, TITLE, ROW, CLO

    left = point.clo * WIDTH / CLO
    top = point.row * HEIGHT / ROW
    # 将方块涂色
    pygame.draw.rect(window, color, (left, top, WIDTH / CLO, HEIGHT / ROW))


def draw_background(color = (1,2,3)):
    global window    
    global WIDTH, HEIGHT, TITLE, ROW, CLO

    pygame.draw.rect(window, color, (0, 0, WIDTH, HEIGHT))

def update_screen(data):
    global pygame_events, window
    '''
    8 * 16
    '''
    global WIDTH, HEIGHT, TITLE, ROW, CLO

    if not window:
        initialize()

    draw_background()

    for i in range(ROW):
        for j in range(CLO):
            if (data[i] & (0x01 << j)):
                rect(Point(i, j), POINT_COLOR)
    pygame.display.flip()
    if pygame_events == []:
        pygame_events = pygame.event.get()

pygame_events = []
def get_events():
    global pygame_events
    ret = pygame_events
    pygame_events = []
    return ret


window = None
def initialize():
    global WIDTH, HEIGHT, TITLE, ROW, CLO
    global window
    
    pygame.init()

    window = pygame.display.set_mode((WIDTH, HEIGHT))


    pygame.display.set_caption(TITLE)

def simulator_quit():
    pygame.quit()
# initialize()
# while True:
#     update_screen([0x01] * 16)