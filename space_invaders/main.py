import pygame
import random

pygame.init()

WIDTH, HEIGHT = 750, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Космические захватчики')

# Цвета
WHITE = (255, 255, 255)

bg_image = pygame.image.load('space_invaders/img/background-black.png').convert()
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

RED_SPACE_SHIP = pygame.image.load('space_invaders/img/pixel_ship_red_small.png')
GREEN_SPACE_SHIP = pygame.image.load('space_invaders/img/pixel_ship_green_small.png')
BLUE_SPACE_SHIP = pygame.image.load('space_invaders/img/pixel_ship_blue_small.png')

# Игрок
YELLOW_SPACE_SHIP = pygame.image.load('space_invaders/img/pixel_ship_yellow.png')

# Лазеры
RED_LASER = pygame.image.load('space_invaders/img/pixel_laser_red.png')
GREEN_LASER = pygame.image.load('space_invaders/img/pixel_laser_green.png')
BLUE_LASER = pygame.image.load('space_invaders/img/pixel_laser_blue.png')
YELLOW_LASER = pygame.image.load('space_invaders/img/pixel_laser_yellow.png')


class Lazer():

    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self, speed):
        self.y += speed

    def off_screen(self):
        return self.y > HEIGHT or self.y < 0


class Ship():
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_image = None
        self.rect = None
        self.laser_image = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self):
        screen.blit(self.ship_image, (self.x, self.y))
        for laser in self.lasers:
            laser.draw()

    def move_lasers(self, speed, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(speed)
            if laser.off_screen():
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Lazer(self.x, self.y, self.laser_image)
            self.lasers.append(laser)
            self.cool_down_counter = 1



class Player(Ship):

    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_image = YELLOW_SPACE_SHIP
        self.rect = self.ship_image.get_rect(topleft=(self.x, self.y))
        self.laser_image = YELLOW_LASER
        self.max_health = health

    def draw(self):
        super().draw()

    def move_lasers(self, speed, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(speed)
            if laser.off_screen():
                self.lasers.remove(laser)



class Enemy(Ship):

    COLOR_MAP = {
        'red' : (RED_SPACE_SHIP, RED_LASER),
        'green' : (GREEN_SPACE_SHIP, GREEN_LASER),
        'blue' : (BLUE_SPACE_SHIP, BLUE_LASER),
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_image, self.laser_image = self.COLOR_MAP[color]
        self.rect = self.ship_image.get_rect(topleft = (self.x, self.y))

    def move(self, speed):
        self.y += speed

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Lazer(self.x - 20, self.y, self.laser_image)
            self.lasers.append(laser)
            self.cool_down_counter = 1

def start_game():

    FPS = 60
    clock = pygame.time.Clock()

    level = 0
    lives = 5
    run = True
    player = Player(300, 630)
    main_font = pygame.font.SysFont('comicsans', 40)
    player_speed = 5
    enemies = []

    def redraw_window():
        screen.blit(bg_image, (0, 0))
        # отрисовка текста
        lives_label = main_font.render(f"Жизни: {lives}", True, WHITE)
        level_label = main_font.render(f"Уровень: {level}", True, WHITE)

        screen.blit(lives_label, (10, 10))
        screen.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        player.draw()

        for enemy in enemies:
            enemy.draw()

        pygame.display.update()

    wave_lenght = 5

    while run:

        redraw_window()

        for i in range(wave_lenght):
            enemy = Enemy(random.randrange(50, WIDTH - 100),
                        random.randrange(-1500, -100),
                        random.choice(['red', 'blue', 'green']))
            enemies.append(enemy)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.x - player_speed > 0: # left
            player.x -= player_speed

        if keys[pygame.K_UP] and player.y - player_speed > 0: # up
            player.y -= player_speed

        if keys[pygame.K_RIGHT] and player.x + player_speed + player.ship_image.get_width() < WIDTH: # right
            player.x += player_speed

        if keys[pygame.K_DOWN] and player.y + player_speed + player.ship_image.get_height() + 15 < HEIGHT:
            player.y += player_speed

        if keys[pygame.K_SPACE]:
            player.shoot()

        clock.tick(FPS)


title_font = pygame.font.SysFont('comicsans', 56)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_game()

    screen.blit(bg_image, (0, 0))
    title_label = title_font.render('Нажми, чтобы начать...', True, WHITE)
    title_rect = title_label.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(title_label, title_rect)
    pygame.display.update()
