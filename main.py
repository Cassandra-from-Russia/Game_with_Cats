# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
from os import path 
img_dir = path.join(path.dirname(__file__), 'img')


WIDTH = 360
HEIGHT = 480
FPS = 30
LEVEL = 1
COUNT = 0
LIFE_START = 5
LIFE = LIFE_START
calichestvo = 4

# Задаем цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MOD_SIZE = 15
# Создаем игру и окно
pygame.init()
# pygame.mixer.init() # звук может не работать
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My Cats")
clock = pygame.time.Clock()

background = pygame.image.load(path.join(img_dir,'background.png')).convert()

background_rect = background.get_rect()

cat = pygame.image.load(path.join(img_dir,'Cat_02_red_goes_left.png')).convert_alpha()
drop = pygame.image.load(path.join(img_dir,'water_drop_05.png')).convert_alpha()
Fire = pygame.image.load(path.join(img_dir,'Fire.png')).convert_alpha()
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def show_go_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "GAME OVER!", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Press a key to begin", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                waiting = False    

class Player(pygame.sprite.Sprite):
    def __init__(self, color=GREEN, x=WIDTH/2, y=HEIGHT/2, step_x=5, step_y=5):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(cat,(50,38))
        
        # self.image.fill(color)
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
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        
                    

class Mod(pygame.sprite.Sprite):
    def __init__(self, color=RED, x=WIDTH/2, y=HEIGHT/2, step_x=3, step_y=8):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((MOD_SIZE, MOD_SIZE))
        self.image = pygame.transform.scale(drop,(50,38))
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

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.speedy = -10
        # self.image = pygame.Surface((10, 20))
        # self.image.fill(GREEN)
        self.image = pygame.transform.scale(Fire,(50,38))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update (self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.top <= 0:
            self.kill()
        


all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player(color=GREEN, y=HEIGHT-25)
all_sprites.add(player)

mods = pygame.sprite.Group()
for i in range(calichestvo):
    mod = Mod()
    all_sprites.add(mod)
    mods.add(mod)
game_over = False

          
# Цикл игры
running = True
while running:
    COUNT += 1
    if game_over:
        show_go_screen()
        game_over = False 
        all_sprites = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        player = Player(color=GREEN, y=HEIGHT-25)
        all_sprites.add(player)
        LIFE = LIFE_START

        mods = pygame.sprite.Group()
        for i in range(calichestvo):
            mod = Mod()
            all_sprites.add(mod)
            mods.add(mod)

    
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    
    # Ввод процесса (события)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            player.shoot()
    # Обновление
    all_sprites.update()
    hits = pygame.sprite.spritecollide(player,mods,True)
    if hits:
        m = Mod()       
        all_sprites.add(m)
        mods.add(m)
        LIFE -= 1
        if LIFE <= 0:
            game_over = True
            
    hits1 = pygame.sprite.groupcollide(mods,bullets,True,True)
    for hit in hits1:
        m = Mod()       
        all_sprites.add(m)
        mods.add(m)
    if COUNT == 500 * LEVEL:
        LEVEL += 1

    # Рендеринг
    screen.fill(BLACK)
    screen.blit(background,background_rect)
    all_sprites.draw(screen)
    draw_text(screen,str('Level: ') + str(LEVEL) ,28,WIDTH/2,20)
    draw_text(screen,str('Life: ') + str(LIFE) ,28,WIDTH/2,50)

    # После отрисовки всего, переворачиваем (вскрываем) экран
    pygame.display.flip()

# не забываем закрывать игру

# show_end_screen = True
# while show_end_screen:
#     show_go_screen()
#     for event in pygame.event.get():

#         if event.type==pygame.QUIT:
#             show_end_screen = False
    
