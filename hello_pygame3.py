'''
https://eyehere.net/2011/python-pygame-novice-professional-2/
'''

import pygame
from pygame.locals import *

background_image_filename = 'sushiplate.jpg'

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load(background_image_filename).convert()

x, y = 0, 0
move_x, move_y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                print('K_LEFT')
                move_x = -1
            elif event.key == K_RIGHT:
                #右方向键则加一
                move_x = 1
            elif event.key == K_UP:
                print('K_UP')
                move_y = -1
            elif event.key == K_DOWN:
                print('K_DOWN')
                move_y = 1
        elif event.type == KEYUP:
            move_x = 0
            move_y = 0
        # 计算出新的坐标
        x+= move_x
        y+= move_y

        screen.fill((0, 0, 0))
        screen.blit(background, (x, y))
        # 在新的位置上画图
        pygame.display.update()
