# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

# Задаем цвета
BLACK = (0, 0, 0)
WHITE = (255, 255,255)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self, color=GREEN, x=WIDTH/2, y=HEIGHT/2):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface((50, 50))
       self.image.fill(color)
       self.rect = self.image.get_rect()
       self.rect.center = (x, y)
    
    # def update(self):
    #   self.rect.x+=5
    #   if self.rect.left >= WIDTH:
    #     self.rect.x = 0
       
    def update(self):
      self.rect.y-=5
      if self.rect.top <= 0:
        self.rect.bottom = HEIGHT
    
    # def update(self):
    #   self.rect.y+=5
    #   if self.rect.bottom >= HEIGHT:
    #     self.rect.y = 0


# Создаем игру и окно
pygame.init()
#pygame.mixer.init() # звук может не работать
screen = pygame.display.set_mode((WIDTH,HEIGHT ))
# screen = pygame.display.set_mode((HEIGHT,WIDTH ))
# screen = pygame.display.set_mode((480,480))

pygame.display.set_caption("My Cats")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player(color=GREEN)
# player2 = Player(color=BLUE, y=HEIGHT/4)
# player3 = Player(GREEN, WIDTH/4, HEIGHT/8)
all_sprites.add(player)
# all_sprites.add(player2)
# all_sprites.add(player3)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        running=False
    # Обновление
    all_sprites.update()

    # Рендеринг
  
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()



# не забываем закрывать игру
