import pygame
from classes import Bird

pygame.init()

WIDTH = 864
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')
pygame.display.set_icon(pygame.image.load('flappy_bird/img/bird1.png'))

WHITE = (255, 255, 255)

FPS = 60
clock = pygame.time.Clock()


bg_image = pygame.image.load('flappy_bird/img/bg.png')
ground_image = pygame.image.load('flappy_bird/img/ground.png').convert()
ground_scroll = 0
scroll_speed = 4
birds_group = pygame.sprite.Group()
flappy_bird = Bird(100, HEIGHT // 2)
birds_group.add(flappy_bird)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(bg_image, (0, 0))
    birds_group.draw(screen)
    birds_group.update()
    screen.blit(ground_image, (ground_scroll, 570))
    ground_scroll -= scroll_speed



    if abs(ground_scroll) > 35:
        ground_scroll = 0


    pygame.display.update()
    clock.tick(FPS)
