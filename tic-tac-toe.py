# Создаю крестики-нолики
import pygame
import sys
def check_winner(mas,sign):
    """
    функция проверяет победителя

    """
    zeroes = 0
    for row in mas:
        zeroes += row.count(0)
        if row.count(sign) == 3:
            return f'победа за {sign}'
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return f'победа за {sign}'
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return f'победа за {sign}'
    if mas[0][2] == sign and mas [1][1] == sign and mas[2][0] == sign:
        return f'победа за {sign}'
    if zeroes == 0:
        return 'Ничья!'
    return False    
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
yellow = (255,255,0)
mas = [[0] * 3 for i in range(3)]
query = 0
game_over = False
# задаем ситуации с нажатием мыши и клвиши space
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (margin + size_block)
            row = y_mouse // (margin + size_block)
            if mas[row][col] == 0:
                if query%2 == 0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'o'
                query+=1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            query = 0
            screen.fill(black)

# задаем координаты клеток
    if not game_over:
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
                if color == red:
                    pygame.draw.line(screen,black,(x+5,y+5),(x+size_block-5,y+size_block-5),10)
                    pygame.draw.line(screen,black,(x+size_block-5,y+5),(x+5,y+size_block-5),10)
                elif color == green:
                    pygame.draw.circle(screen,yellow,(x+size_block//2,y+size_block//2),size_block//2,10)

    if (query-1)%2 == 0:
        game_over = check_winner(mas,'x')
    else:
        game_over = check_winner(mas,'o')
    
    if game_over:
        # цвет экрана
        screen.fill(black)
        # шрифт ткста
        font = pygame.font.SysFont('stxinqkai',80)
        # текст и его цвет
        text1 = font.render(game_over,True,white)
        # координаты
        text_rect = text1.get_rect()
        # центр экрана
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        # прикрепление текста по координатам
        screen.blit(text1, [text_x,text_y])

    pygame.display.update()
