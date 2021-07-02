import pygame
import os
from .settings import *

pygame.init()


screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(WINDOW_CAPTION)
# pygame.display.set_icon(surface)

# set framerate
clock = pygame.time.Clock()
FPS = 60 

# ===============================================

# define player action variables
moving_left = False
moving_right = False
# define colors
BG = (144, 201, 120)
def draw_bg():
    screen.fill(BG)

# creating a player
class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1
        self.flip = False
        img = pygame.image.load(os.path.join(os.path.join(os.path.join('img','player'), 'idle'), '0.png'))
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def move(self, moving_left, moving_right):
        # reset movement variables
        dx = 0
        dy = 0

        # asssign moviment varibales if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
        
        # update rectangle position
        self.rect.x += dx 
        self.rect.y += dy

    def draw(self):
        # screen is supposed to be pre defined in the code
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

player = Soldier(200, 200, 0.2, 5)
player2 = Soldier(400, 200, 0.2, 5)

# ===============================================

run = True
while run:
    clock.tick(FPS)
    draw_bg()

    player.draw() # drawing a img in the rect ordinatres
    player.move(moving_left, moving_right)
    # player2.draw() # drawing a img in the rect ordinatres

    for event in pygame.event.get():
        # quit game when clicks 'x' button
        if event.type == pygame.QUIT:
            run = False

        # keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True  
            
            if event.key == pygame.K_ESCAPE: # escape for quitting the game
                run = False
        
        # keyboard releases
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False 

    pygame.display.update()

pygame.quit()


