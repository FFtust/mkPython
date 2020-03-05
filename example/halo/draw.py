import pygame
from pygame.locals import *
import math
import time
import sys

from mkPython import halo

pygame.init()

# 窗口尺寸
WIDTH = 512 * 2
HEIGHT = 256 * 2

TITLE = "game"

# 画笔颜色
PEN_COLOR = (255, 255, 255) 
# 背景颜色
BACKGROUND_COLOR = (0, 0, 0)

# 画笔尺寸
PEN_SIZE = [20, 20]
# 鼠标尺寸， 非绘图状态
MOUSE_SIZE = [5, 5]

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

x = WIDTH / 2
y = HEIGHT / 2

last_x = x
last_y = y

while True:
    g_x = halo.motion_sensor.get_gyroscope('x')
    g_z = halo.motion_sensor.get_gyroscope('z')
    
    if math.fabs(g_x) > 3 or math.fabs(g_z) > 3:
        x = x - g_z
        y = y - g_x

    for event in pygame.event.get():
        # 查找关闭窗口事件
        if event.type == QUIT:
            halo.exit()
            pygame.quit()
            sys.exit()

    # 边界控制
    x = 0 if x < 0 else x
    x = WIDTH if x > WIDTH else x
    y = 0 if y < 0 else y
    y = HEIGHT if y > HEIGHT else y

    # 绘图控制
    if not halo.button.is_pressed():
        pygame.draw.rect(window, BACKGROUND_COLOR, (last_x, last_y, MOUSE_SIZE[0], MOUSE_SIZE[1]))
    
    if halo.button.is_pressed():
        pygame.draw.rect(window, PEN_COLOR, (x, y, PEN_SIZE[0], PEN_SIZE[1]))
    else:
        pygame.draw.rect(window, PEN_COLOR, (x, y, MOUSE_SIZE[0], MOUSE_SIZE[1]))

    pygame.display.flip()

    last_x = x
    last_y = y

    time.sleep(0.05)

    # 摇晃清屏
    if halo.motion_sensor.get_shake_strength() > 40:
        pygame.draw.rect(window, (0, 0, 0), (0, 0, WIDTH, HEIGHT))
