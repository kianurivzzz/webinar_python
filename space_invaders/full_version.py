import pygame
import random

pygame.init()

WIDTH, HEIGHT = 750, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Космические захватчики")

# Цвета
WHITE = (255, 255, 255)

# Фон
bg_image = pygame.image.load("space_invaders/img/background-black.png").convert()
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

# Загрузка изображений
RED_SPACE_SHIP = pygame.image.load("space_invaders/img/pixel_ship_red_small.png")
GREEN_SPACE_SHIP = pygame.image.load("space_invaders/img/pixel_ship_green_small.png")
BLUE_SPACE_SHIP = pygame.image.load("space_invaders/img/pixel_ship_blue_small.png")

# Игрок
YELLOW_SPACE_SHIP = pygame.image.load("space_invaders/img/pixel_ship_yellow.png")

# Лазеры
RED_LASER = pygame.image.load("space_invaders/img/pixel_laser_red.png")
GREEN_LASER = pygame.image.load("space_invaders/img/pixel_laser_green.png")
BLUE_LASER = pygame.image.load("space_invaders/img/pixel_laser_blue.png")
YELLOW_LASER = pygame.image.load("space_invaders/img/pixel_laser_yellow.png")


class Laser():
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)

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
            # !!!!!!!!!!!
            elif collide(laser, obj):
                obj.health -= 10
                self.lasers.remove(laser)
            # !!!!!!!!!!!

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_image)
            self.lasers.append(laser)
            self.cool_down_counter = 1


class Player(Ship):
    def __init__(self, x, y, health=100):
        Ship.__init__(self, x, y, health)
        self.ship_image = YELLOW_SPACE_SHIP
        self.rect = self.ship_image.get_rect(topleft=(self.x, self.y))
        self.laser_image = YELLOW_LASER
        self.max_health = health
        self.mask = pygame.mask.from_surface(self.ship_image)

    def move_lasers(self, speed, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(speed)
            if laser.off_screen():
                self.lasers.remove(laser)
            # !!!!!!!!!!!
            else:
                for obj in objs:
                    if collide(laser, obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self):
        Ship.draw(self)
        self.healthbar()  # !!!!!!

    # !!!!!!!!!!!
    def healthbar(self):
        pygame.draw.rect(screen, (255, 0, 0),
                        (self.x, self.y + self.ship_image.get_height() + 10, self.ship_image.get_width(), 10))
        pygame.draw.rect(screen, (0, 255, 0), (
            self.x, self.y + self.ship_image.get_height() + 10,
            self.ship_image.get_width() * (self.health / self.max_health),
            10))


class Enemy(Ship):
    COLOR_MAP = {
        "red": (RED_SPACE_SHIP, RED_LASER),
        "green": (GREEN_SPACE_SHIP, GREEN_LASER),
        "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
    }

    def __init__(self, x, y, color, health=100):
        Ship.__init__(self, x, y, health)
        self.ship_image, self.laser_image = self.COLOR_MAP[color]
        self.rect = self.ship_image.get_rect(topleft=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.ship_image)

    def move(self, speed):
        self.y += speed

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x - 20, self.y, self.laser_image)
            self.lasers.append(laser)
            self.cool_down_counter = 1


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


def start_game():
    FPS = 60
    clock = pygame.time.Clock()

    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 40)
    lost_font = pygame.font.SysFont("comicsans", 50)

    enemies = []
    wave_length = 5
    enemy_speed = 1

    player_speed = 5
    laser_speed = 5

    player = Player(300, 630)

    lost = False
    lost_count = 0

    run = True

    def redraw_window():
        screen.blit(bg_image, (0, 0))
        # отрисовка текста
        lives_label = main_font.render(f"Жизни: {lives}", True, WHITE)
        level_label = main_font.render(f"Уровень: {level}", True, WHITE)

        screen.blit(lives_label, (10, 10))
        screen.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw()

        player.draw()

        if lost:
            lost_label = lost_font.render("Ты проиграл!!", True, WHITE)
            screen.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))

        pygame.display.update()

    while run:
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100),
                            random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_speed > 0:  # left
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.x + player_speed + player.ship_image.get_width() < WIDTH:  # right
            player.x += player_speed
        if keys[pygame.K_UP] and player.y - player_speed > 0:  # up
            player.y -= player_speed
        if keys[pygame.K_DOWN] and player.y + player_speed + player.ship_image.get_height() + 15 < HEIGHT:  # down
            player.y += player_speed
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_speed)
            enemy.move_lasers(laser_speed, player)

            if random.randrange(0, 2 * 60) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.ship_image.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_speed, enemies)
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
