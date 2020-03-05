# -*- coding: utf-8 -*-
import pygame
import sys
import math 
from pygame.locals import *
import time
from mkPython import halo 

pygame.init()
 
# 检测内容配置
monitor_function = halo.microphone.get_loudness
monitor_function_para = ()

# 参数配置
# 窗口大小
SCREEN_SIZE = WIDTH, HEIGHT = 1200, 400
# 背景颜色
BACKGROUND_COLOR = (255, 255, 255)
# 画笔颜色
PEN_COLOR = (0, 255, 0)
# 画笔尺寸
PEN_SIZE = 5

# 监听频率
MONITOR_FREQUENCY = 50

# 折现两点间间隔
POINTX_INTERVAL = 3
points = [(0, HEIGHT / 2)]

# 设置窗口
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("sensor monitor")
 
screen.fill(BACKGROUND_COLOR)
while True:
    for event in pygame.event.get():
        # 查找关闭窗口事件
        if event.type == QUIT:
            halo.exit()
            pygame.quit()
            sys.exit()
        
    points.append((len(points) * POINTX_INTERVAL, HEIGHT / 2 - monitor_function(*monitor_function_para)))
    pygame.draw.lines(screen, PEN_COLOR, 0, points, PEN_SIZE)

    if len(points) > WIDTH / POINTX_INTERVAL:
        points = [(0, HEIGHT / 2)]
        pygame.draw.rect(screen, BACKGROUND_COLOR, (0, 0, WIDTH, HEIGHT))

    pygame.display.flip()
    time.sleep(1 / MONITOR_FREQUENCY)
 