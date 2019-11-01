'''
pygame游戏库
https://eyehere.net/tag/pygame/
https://eyehere.net/2011/python-pygame-novice-professional-1/
'''

import pygame
from pygame.locals import *
from sys import exit
import sys

background_image_filename = 'sushiplate.jpg'
mouse_image_filename = 'fugu.png'

pygame.init()
# 创建一个窗口
screen = pygame.display.set_mode((640, 480), 0, 32)
# 设置窗口标题
pygame.display.set_caption("hello, world!")

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            break
            #sys.exit()
    # 将背景图画上去
    screen.blit(background, (0, 0))
    # 获得鼠标位置
    x, y = pygame.mouse.get_pos()
    # 计算光标左上角位置
    x-= mouse_cursor.get_width() / 2
    y-= mouse_cursor.get_height() / 2
    # 把光标画上去
    screen.blit(mouse_cursor, (x, y))
    # 刷新画面
    pygame.display.update()