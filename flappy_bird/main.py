import pygame
from classes import Bird, Pipe

pygame.init()

WIDTH = 864
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')
pygame.display.set_icon(pygame.image.load('flappy_bird/img/bird1.png'))

WHITE = (255, 255, 255)
GREEN = (47, 114, 84)

FPS = 60
clock = pygame.time.Clock()


bg_image = pygame.image.load('flappy_bird/img/bg.png')
ground_image = pygame.image.load('flappy_bird/img/ground.png').convert()
ground_scroll = 0
scroll_speed = 4

birds_group = pygame.sprite.Group()
flappy_bird = Bird(100, HEIGHT // 2)
birds_group.add(flappy_bird)

pipe_group = pygame.sprite.Group()
bottom_pipe = Pipe(300, HEIGHT // 2, -1, scroll_speed)
top_pipe = Pipe(300, HEIGHT // 2, 1, scroll_speed)
pipe_group.add(bottom_pipe, top_pipe)

game_over = False
result_is_showed = False
score = 0


def draw_result(x, y):
    font = pygame.font.SysFont('arial', 60)
    text = font.render(f'Счёт: {score}', True, WHITE, GREEN)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and flappy_bird.flying == False and game_over == False:
            flappy_bird.flying = True
        elif event.type == pygame.MOUSEBUTTONDOWN and result_is_showed and game_over:
            exit()
        elif event.type == USEREVENT and game_over == False and flappy_bird.flying == True:
            pipe_height = random.randint(-100, 100)
            bottom_pipe = Pipe(WIDTH, HEIGHT // 2 + pipe_height, -1, scroll_speed)
            top_pipe = Pipe(WIDTH, HEIGHT // 2 + pipe_height, 1, scroll_speed)
            pipe_group.add(bottom_pipe, top_pipe)


    screen.blit(bg_image, (0, 0))
    birds_group.draw(screen)
    birds_group.update()

    pipe_group.draw(screen)
    pipe_group.update()

    screen.blit(ground_image, (ground_scroll, 570))
    ground_scroll -= scroll_speed



    if abs(ground_scroll) > 35:
        ground_scroll = 0


    pygame.display.update()

    if flappy_bird.rect. bottom >= HEIGHT:
        game_over = True
        flappy_bird.flying = False

    if game_over: # game_over == True
        draw_result(WIDTH // 2, HEIGHT // 2)
        result_is_showed = True

    if pygame.sprite.groupcollide(birds_group, pipe_group, False, False) or flappy_bird.rect.top < 0:
        game_over = True
        flappy_bird.flying = False


    if flappy_bird.rect.bottom >= HEIGHT:
        game_over = True
        flappy_bird.flying = False


    clock.tick(FPS)
