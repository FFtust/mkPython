# import sys, pygame
# from mkPython import halo

# halo.led.show_all(100, 0, 0)
# while True:
#     print(halo.motion_sensor.get_acceleration("\"x\""))

# pygame.init()

# size = width, height = 420, 440
# speed = [0.1, 0.1]
# black = 0, 0, 0

# screen = pygame.display.set_mode(size)

# ball = pygame.image.load("intro_ball.gif")
# ballrect = ball.get_rect()
# print(dir(ballrect))

# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()

#     # speed[0] = halo.motion_sensor.get_acceleration("\'x\'")
#     # speed[1] = halo.motion_sensor.get_acceleration("\'y\'")
#     # if speed[0] != None:
#     #     ballrect = ballrect.move(speed)
#     # if ballrect.left < 0 or ballrect.right > width:
#     #     speed[0] = -speed[0]
#     # if ballrect.top < 0 or ballrect.bottom > height:
#     #     speed[1] = -speed[1]

#     if halo.button.is_pressed():
#         ballrect.right([1,1])
#     screen.fill(black)
#     screen.blit(ball, ballrect)
#     pygame.display.flip()


import sys, time
from mkPython import halo

halo.led.show_all(100, 0, 0)
while True:
    print(halo.motion_sensor.get_acceleration("x"), halo.motion_sensor.get_acceleration("y"))
    time.sleep(0.2)