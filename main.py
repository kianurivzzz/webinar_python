from cmath import pi
import pygame  # импорт основного модуля

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
pi = 3.14

pygame.init()  # импорт других необходимых расширений
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Вебинар №4')
pygame.display.set_icon(pygame.image.load('img/icon.bmp'))
screen.fill(WHITE)
# pygame.draw.rect(screen, WHITE, (10, 10, 50, 100), 2)
# pygame.draw.line(screen, BLUE, (200, 20), (350, 50), 5)
# pygame.draw.lines(screen, RED, True, [(200, 80), (250, 200), (300, 200)], 2)
# pygame.draw.aaline(screen, BLUE, True, (200, 40), (350, 70))
# pygame.draw.aalines(screen, RED, True, [(300, 80), (350, 80), (400, 200)], 2)
# pygame.draw.polygon(screen, WHITE, [[150, 210], [180, 250], [90, 290], [30, 230]]) #закрашенный
# pygame.draw.polygon(screen, WHITE, [[150, 310], [180, 350], [90, 390], [30, 330]], 1)
# pygame.draw.circle(screen, BLUE, (300, 250), 40, 5)
# pygame.draw.ellipse(screen, BLUE, (300, 300, 100, 50), 1)
# pygame.draw.arc(screen, RED, (450, 30, 50, 150), pi, 2 * pi, 5)
# Флаг России от Ильи
# pygame.draw.rect(surface=screen, color=(255, 255, 255), rect=(32, 32, 128, 32))
# pygame.draw.rect(surface=screen, color=(0, 0, 255), rect=(32, 65, 128, 32))
# pygame.draw.rect(surface=screen, color=(255, 0, 0), rect=(32, 97, 128, 32))
pygame.display.update()


FPS = 60
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    clock.tick(FPS)


# a = 10
print(f'Переменная a равняется {a}')
