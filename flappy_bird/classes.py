import pygame
# from main import scroll_speed

class Bird(pygame.sprite.Sprite):


    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.flying = False


        for i in range(1, 4):
            self.images.append(pygame.image.load(f'flappy_bird/img/bird{i}.png').convert_alpha())
        self.index = 0
        self.image = self.images[self.index]
        self.counter = 0
        self.rect = self.image.get_rect(center=(x,y))
        self.vel = 0
        self.clicked = False


    def update(self):
        if self.flying == True:
            self.vel += 0.5

        if self.vel > 8:
            self.vel = 8

        if self.rect.bottom < 640:
            self.rect.y += int(self.vel)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.clicked == False:  # if keys[pygame.K_SPACE] == 1:
            self.clicked = True
            self.vel = -15
        if not keys[pygame.K_SPACE]:
            self.clicked = False

        self.counter += 1
        flap_cooldown = 5

        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0

        # self.image = self.images[self.index]
        self.image = pygame.transform.rotate(self.images[self.index], self.vel * 2)

pipe_gap = 150

class Pipe(pygame.sprite.Sprite):


    def __init__(self, x, y, position, scroll_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('flappy_bird/img/pipe.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.scroll_speed = scroll_speed

        #postion 1 - верх, position -1 - низ
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - pipe_gap // 2]
        if position == -1:
            self.rect.topleft = [x, y + pipe_gap // 2]


    def update(self):
        self.rect.x -= self.scroll_speed
        if self.rect.right < 0:
            self.kill()
