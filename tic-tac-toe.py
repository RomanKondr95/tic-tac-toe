# Создаю крестики-нолики
import pygame
import sys
pygame.init()
# размер
size_block = 100
# отступ
margin = 15
# размер игрового поля
widht = height = size_block * 3 + margin * 4
size_window = (widht,height)
screen = pygame.display.set_mode(size_window)
# заголовок
pygame.display.set_caption('tic-tac-toe')
# моя картинка в качестве иконки
img = pygame.image.load('pyt.png')
pygame.display.set_icon(img)
# цвета
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)

mas = [[0] * 3 for i in range(3)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
# задаем координаты клеток
    for row in range(3):
        for col in range(3):
            x = col * size_block + (col + 1) * margin
            y = row * size_block + (row + 1) * margin
            pygame.draw.rect(screen,white,(x,y,size_block,size_block))
    pygame.display.update()
