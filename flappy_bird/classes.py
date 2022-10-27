import pygame

class Bird(pygame.sprite.Sprite):

    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []


        for i in range(1, 4):
            self.images.append(pygame.image.load(f'flappy_bird/img/bird{i}.png').convert_alpha())
        self.index = 0
        self.image = self.images[self.index]
        self.counter = 0
        self.rect = self.image.get_rect(center=(x,y))


    def update(self):
        self.counter += 1
        flap_cooldown = 5

        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0

        self.image = self.images[self.index]
