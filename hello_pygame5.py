'''
可变尺寸
https://eyehere.net/2011/python-pygame-novice-professional-3/
'''

import pygame
from pygame.locals import *

background_image_filename = 'sushiplate.jpg'
SCREEN_SIZE = (640, 480)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
background = pygame.image.load(background_image_filename).convert()

while True:

    event = pygame.event.wait()
    if event.type == QUIT:
        pygame.quit()
    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        pygame.display.set_caption('Window resized to' + str(event.size))

    screen_width, screen_height = SCREEN_SIZE
    # 这里需要重新填满窗口
    for y in range(0, screen_height, background.get_height()):
        for x in range(0, screen_width, background.get_width()):
            screen.blit(background, (x, y))
    pygame.display.update()