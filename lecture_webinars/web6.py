from configparser import NoSectionError
from turtle import position, width
import pygame  # импорт основного модуля

pygame.init()  # импорт других необходимых расширений
WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Моя первая программа")
pygame.display.set_icon(pygame.image.load("img/icon.bmp"))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FPS = 60
clock = pygame.time.Clock()

st_pos = None

screen.fill(WHITE)
pygame.display.update()

pygame.mouse.set_visible(False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        screen.fill(WHITE)
        position = pygame.mouse.get_pos()
        if pygame.mouse.get_focused():
            pygame.draw.circle(screen, BLUE, position, 7)
        pressed = pygame.mouse.get_pressed()
        if pressed[0]:

            if st_pos is None:
                st_pos = position

            width = position[0] - st_pos[0]
            height = position[1] - st_pos[1]

            screen.fill(WHITE)
            pygame.draw.rect(screen, BLUE, (st_pos[0], st_pos[1], width, height))
        else:
            st_pos = None
        pygame.display.update()

    clock.tick(FPS)



        # elif event.type == pygame.MOUSEBUTTONUP and event.button == 1: #нажата левая кнопка
        #     startDraw = True
        #     st_pos = event.pos #координата курсора мыши
        #     # print(f'Нажата кнопка: {event.button}')
        # elif event.type == pygame.MOUSEMOTION:
        #     if startDraw:
        #         position = event.pos
        #         width = position[0] - st_pos[0]
        #         height = position[1] - st_pos[1]

        #         screen.fill(WHITE)
        #         pygame.draw.rect(screen, BLUE, (st_pos[0], st_pos[1], width, height))
        #         pygame.display.update()
        # elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        #     startDraw = False



# pygame.MOUSEBUTTONDOWN - нажатие на кнопку мыши
# pygame.MOUSEBUTTONUP - отпускание кнопки мыши
# pygame.MOUSEWHEEL - движение колесом мыши
# pygame.MOUSEMOTION - движение курсором мыши

# левая кнопка: 1
# центральная кнопка: 2
# правая кнопка: 3
# колёсико мыши: 4-5 вверх-вниз
