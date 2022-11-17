import pygame  # импорт основного модуля

pygame.init()  # импорт других необходимых расширений

WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Моя первая программа")
pygame.display.set_icon(pygame.image.load('img/icon.bmp'))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (183, 98, 228)
YELLOW = (239, 228, 176)

FPS = 60
clock = pygame.time.Clock()

# print(pygame.image.get_extended())

car_image = pygame.image.load('img/car.png').convert_alpha()
car_image = pygame.transform.scale(car_image, (car_image.get_width() // 2, car_image.get_height() // 2))
#поворот на 90 градусов
car_image = pygame.transform.rotate(car_image, 90)
car_image = pygame.transform.flip(car_image, True, False)
# car_image.set_colorkey((255, 255, 255))

bg_image = pygame.image.load('img/bg.bmp').convert()
screen.blit(bg_image,(0,0))

car_rect = car_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(car_image, car_rect)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    clock.tick(FPS)
