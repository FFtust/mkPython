import pygame
from sys import exit
import random
import time
import threading

SCREEN_DIR = "ACROSS" # UPRIGHT
WIDTH = 512
HEIGHT = 256
TITLE = "16 * 8 点阵游戏模拟机"

ROW = 8
CLO = 16

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
    global SCREEN_DIR

    if not window:
        initialize()

    draw_background()
    if SCREEN_DIR == "ACROSS":
        for i in range(CLO):
            for j in range(ROW):
                if (data[i] & (0x01 << j)):
                    rect(Point(j, i), POINT_COLOR)
    else:
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
    global SCREEN_DIR

    pygame.init()

    if SCREEN_DIR == "UPRIGHT":
        temp = WIDTH
        WIDTH = HEIGHT
        HEIGHT = temp

        temp = ROW
        ROW = CLO
        CLO = temp

    print(WIDTH, HEIGHT, ROW, CLO)

    window = pygame.display.set_mode((WIDTH, HEIGHT))


    pygame.display.set_caption(TITLE)

def set_dir(s_dir = "ACROSS"):
    global SCREEN_DIR
    
    SCREEN_DIR = s_dir 

def simulator_quit():
    pygame.quit()


pygame.mixer.init()
def play_music(name):
    pygame.mixer.music.load(r"mkPython/resource/music/" + name)
    pygame.mixer.music.play()