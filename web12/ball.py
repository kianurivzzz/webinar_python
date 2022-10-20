from tkinter import scrolledtext
import pygame

pygame.init()


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, filename, score, speed, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        # self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed
        self.score = score

        self.add(group)

    def update(self, *args):
        if self.rect.y < args[0] - 20:
            self.rect.y += self.speed
        else:
            self.kill()
