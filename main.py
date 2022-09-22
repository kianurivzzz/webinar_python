import pygame  # импорт основного модуля


pygame.init()  # импорт других необходимых расширений
pygame.display.set_mode((600, 400), pygame.RESIZABLE)
pygame.display.set_caption('Вебинар №4')
pygame.display.set_icon(pygame.image.load('img/icon.bmp'))


FPS = 60
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    clock.tick(FPS)
