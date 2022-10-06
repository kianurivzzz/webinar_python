import pygame  # импорт основного модуля

pygame.init()  # импорт других необходимых расширений

WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Вебинар 8")
pygame.display.set_icon(pygame.image.load("img/icon.bmp"))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (183, 98, 228)

FPS = 60
clock = pygame.time.Clock()

ground = HEIGHT - 70
jump_force = 20 # сила прыжка
move = jump_force + 1

hero = pygame.image.load('img/mario.png').convert_alpha() # .convert_alpha()
hero = pygame.transform.scale(hero, (40, 50))
rect = hero.get_rect(centerx = WIDTH // 2)
rect.bottom = ground

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_SPACE and ground == rect.bottom:
                move = -jump_force

    if move <= jump_force:
        if rect.bottom + move < ground:
            rect.bottom += move
            if move < jump_force:
                move += 1
            else:
                rect.bottom = ground
                move = jump_force + 1

    screen.fill(WHITE)
    screen.blit(hero, rect)
    pygame.display.update()
    clock.tick(FPS)
