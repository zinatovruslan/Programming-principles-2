import pygame, sys
from pygame.locals import *
import random

pygame.init()
pygame.mixer.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0
GAME_OVER = False

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text = font.render("Game Over", True, WHITE)

def draw_text_with_outline(surface, text, font, x, y, text_color, outline_color):
    outline_surface = font.render(text, True, outline_color)
    for dx, dy in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
        surface.blit(outline_surface, (x + dx, y + dy))
    text_surface = font.render(text, True, text_color)
    surface.blit(text_surface, (x, y))

background = pygame.image.load(r"C:\Users\Askar\OneDrive - АО Казахстанско-Британский Технический Университет\Рисунки\images\street.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racing Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Askar\OneDrive - АО Казахстанско-Британский Технический Университет\Рисунки\images\enemy.jpg")
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Askar\OneDrive - АО Казахстанско-Британский Технический Университет\Рисунки\images\me.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\Askar\OneDrive - АО Казахстанско-Британский Технический Университет\Рисунки\images\coin.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, SCREEN_WIDTH-30), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.respawn()

    def respawn(self):
        self.rect.center = (random.randint(30, SCREEN_WIDTH-30), 0)

P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

crash_sound = pygame.mixer.Sound(r'C:\Users\Askar\Downloads\crash.mpeg')

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if GAME_OVER and event.type == KEYDOWN:
            if event.key == K_r:
                GAME_OVER = False
                SPEED = 5
                SCORE = 0
                COINS_COLLECTED = 0
                P1 = Player()
                E1 = Enemy()
                C1 = Coin()
                enemies = pygame.sprite.Group()
                enemies.add(E1)
                coins = pygame.sprite.Group()
                coins.add(C1)
                all_sprites = pygame.sprite.Group()
                all_sprites.add(P1, E1, C1)

    if not GAME_OVER:
        DISPLAYSURF.blit(background, (0, 0))
        draw_text_with_outline(DISPLAYSURF, f"Score: {SCORE}", font_small, 10, 10, WHITE, BLACK)
        draw_text_with_outline(DISPLAYSURF, f"Coins: {COINS_COLLECTED}", font_small, 10, 40, YELLOW, BLACK)

        for entity in all_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()

        if pygame.sprite.spritecollideany(P1, enemies):
            crash_sound.play()
            GAME_OVER = True

        if pygame.sprite.spritecollideany(P1, coins):
            COINS_COLLECTED += 1
            C1.respawn()
    else:
        DISPLAYSURF.fill(RED)
        draw_text_with_outline(DISPLAYSURF, "Game Over", font, 30, 250, WHITE, BLACK)
        draw_text_with_outline(DISPLAYSURF, "Press R to restart", font_small, 120, 350, WHITE, BLACK)
        draw_text_with_outline(DISPLAYSURF, f"Final Score: {SCORE}", font_small, 100, 150, WHITE, BLACK)
        draw_text_with_outline(DISPLAYSURF, f"Coins Collected: {COINS_COLLECTED}", font_small, 100, 180, YELLOW, BLACK)

    pygame.display.update()
    FramePerSec.tick(FPS)
