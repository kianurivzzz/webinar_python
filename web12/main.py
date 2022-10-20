import pygame
from ball import *
import random


def create_ball(group):
    index = random.randint(0, len(balls_data) - 1)
    x = random.randint(20, WIDTH - 20)
    speed = random.randint(1, 4)

    return Ball(x, balls_data[index]['path'],
                balls_data[index]['score'], speed, group)

game_score = 0

def colide_balls():
    global game_score
    for ball in balls_group:
        if cart_rect.collidepoint(ball.rect.center):
            game_score += ball.score
            ball.kill()



pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)

WIDTH = 1000
HEIGHT = 570

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Balls')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60
clock = pygame.time.Clock()

bg_image = pygame.image.load('web12/img/bg_image.jpg').convert()

cart_image = pygame.image.load('web12/img/telega.png').convert_alpha()
cart_rect = cart_image.get_rect(centerx = WIDTH // 2, bottom=HEIGHT - 5)

score_image = pygame.image.load('web12/img/score_fon.png').convert_alpha()
score_font = pygame.font.SysFont('arial', 30)

balls_group = pygame.sprite.Group()
balls_data = ({'path': 'web12/img/ball_rabbit.png', 'score': 100},
               {'path': 'web12/img/ball_lemur.png', 'score': 150},
               {'path': 'web12/img/ball_pantera.png', 'score': 200})


cart_speed = 10

create_ball(balls_group)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            create_ball(balls_group)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        cart_rect.x -= cart_speed

    #контроль выезда за окно
        if cart_rect.x < 0:
            cart_rect.x = 0

    elif keys[pygame.K_RIGHT]:
        cart_rect.x += cart_speed

        if cart_rect.x > WIDTH - cart_rect.width:
            cart_rect.x = WIDTH - cart_rect.width

    colide_balls()

    screen.blit(bg_image, (0, 0))
    screen.blit(score_image, (0, 0))
    score_text = score_font.render(str(game_score), True, (94, 138, 14))
    screen.blit(score_text, (40, 10))

    balls_group.draw(screen)
    screen.blit(cart_image, cart_rect)
    pygame.display.update()

    balls_group.update(HEIGHT)

    clock.tick(FPS)


# pygame.Rect.collidepoint
# проверить, находится ли точка внутри прямоугольника

# pygame.Rect.colliderect
# тест, пересекаются ли два прямоугольника

# pygame.Rect.collidelist
# проверить, пересекается ли хоть один прямоугольник в списке

# pygame.Rect.collidelistall
# пересекаются ли все прямоугольники в списке

# pygame.Rect.collidedict
# проверить, если один прямоугольник в словаре пересекается

# pygame.Rect.collidedictall
# пересекаются ли все прямоугольники в словаре
