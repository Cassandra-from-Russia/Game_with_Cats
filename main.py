# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

# Задаем цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MOD_SIZE = 15


class Player(pygame.sprite.Sprite):
    def __init__(self, color=GREEN, x=WIDTH/2, y=HEIGHT/2, step_x=5, step_y=5):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.step_x = step_x
        self.step_y = step_y


    def update (self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] and self.rect.left > 0:
            self.speedx = -8

        if keystate[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.speedx = 8
            
        self.rect.x += self.speedx    


class Mod(pygame.sprite.Sprite):
    def __init__(self, color=RED, x=WIDTH/2, y=HEIGHT/2, step_x=3, step_y=8):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((MOD_SIZE, MOD_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        center_x = random.randrange(int(MOD_SIZE/2), int(WIDTH-MOD_SIZE/2))
        center_y = random.randrange(-HEIGHT, 0) - MOD_SIZE
        self.rect.center = (center_x, center_y)
        # self.rect.center = (random.randrange(0, WIDTH), -MOD_SIZE)
        self.step_x = step_x
        self.step_y = step_y

    
    def update (self):
        self.rect.y += self.step_y
        self.rect.x += self.step_x
        if self.rect.top >= HEIGHT:
            center_x = random.randrange(int(MOD_SIZE/2), int(WIDTH-MOD_SIZE/2))
            center_y = -MOD_SIZE
            self.rect.center = (center_x, center_y)
        if self.rect.left <= 0:
            self.step_x = abs(self.step_x)
        if self.rect.right >= WIDTH:
            self.step_x = -abs(self.step_x)    

        
        

         

           
        # if self.rect.right >= WIDTH:
        #     self.speedx = 0
        
        # if self.rect.left <= 0:
        #     self.speedx = 0
        # self.rect.x += self.speedx    


    # def update(self):
        # self.rect.y += self.step_y
        # self.rect.x += self.step_x
        # if self.rect.bottom >= HEIGHT:
        #     self.step_y = -abs(self.step_y)
        # if self.rect.top <= 0:
        #     self.step_y = abs(self.step_y)
        # if self.rect.right >= WIDTH:
        #     self.step_x = -abs(self.step_x)      
        # if self.rect.left <= 0:
        #     self.step_x = abs(self.step_x) 

    # def update(self):
    #     self.rect.y += self.step_y
    #     self.rect.x += self.step_x
    #     if self.rect.bottom >= HEIGHT:
    #         self.step_y = -5
    #     if self.rect.top <= 0:
    #         self.step_y = 5
    #     if self.rect.left <= 0:
    #         self.step_x = +5 
    #     if self.rect.right >= WIDTH:
    #         self.step_x = -5  

    # def update(self):
    #     self.rect.y += self.step
    #     if self.rect.bottom >= HEIGHT:
    #         self.step = -5
    #     if self.rect.top <= 0:
    #         self.step = 5
    
    # # def update(self):   
    #     self.rect.x += self.step
    #     if self.rect.right >= WIDTH:
    #         self.step = -5
    #     if self.rect.left <= 0:
    #         self.step = 5
    


    # def update(self):
    #     self.rect.x += self.step
    #     if self.rect.right >= WIDTH:
    #        self.rect.x = 0
       
    # def update(self):
    #     self.rect.y -= 5
    #     if self.rect.top <= 0:
    #         self.rect.bottom = HEIGHT
    
    # def update(self):
    #     self.rect.y += 5
    #     if self.rect.bottom >= HEIGHT:
    #         self.rect.y = 0


# Создаем игру и окно
pygame.init()
# pygame.mixer.init() # звук может не работать
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My Cats")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

player = Player(color=GREEN, y=HEIGHT-25)
all_sprites.add(player)

mods = pygame.sprite.Group()
for i in range(4):
    mod = Mod()
    all_sprites.add(mod)
    mods.add(mod)

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

    # После отрисовки всего, переворачиваем (вскрываем) экран
    pygame.display.flip()

# не забываем закрывать игру
