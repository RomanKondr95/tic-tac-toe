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
query = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (margin + size_block)
            row = y_mouse // (margin + size_block)
            if mas[row][col] == 0:
                if query%2 == 0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'o'
                query+=1
# задаем координаты клеток
    for row in range(3):
        for col in range(3):
            if mas[row][col] == 'x':
                color = red
            elif mas[row][col] == 'o':
                color = green
            else:
                color = white
            x = col * size_block + (col + 1) * margin
            y = row * size_block + (row + 1) * margin
            pygame.draw.rect(screen,color,(x,y,size_block,size_block))
    pygame.display.update()
