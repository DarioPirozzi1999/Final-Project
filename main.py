import pygame
import time
import random

pygame.init()
screen_width = 900
screen_height = 700
screen= pygame.display.set_mode([screen_width, screen_height])

lives = 3
score = 0
level = 1

pygame.display.set_caption("Zombie Game")

def set_background(image):
   bg = pygame.image.load(image)
   bg = pygame.transform.scale(bg, [screen_width, screen_height])
   screen.blit(bg, (0,0))


class CrossHair(pygame.sprite.Sprite):
   def __init__(self):
    super().__init__()
    self.image = pygame.image.load("CrossHair.png")
    self.image = pygame.transform.scale(self.image, (60, 60))
    self.rect = self.image.get_rect()

class Zombies(pygame.sprite.Sprite):
   def __init__(self, img):
    super().__init__()
    self.image = pygame.image.load(img)
    self.image = pygame.transform.scale(self.image, (60, 60))
    self.rect = self.image.get_rect()


zombies_list = pygame.sprite.Group()
allSprites = pygame.sprite.Group()
crosshair = CrossHair()
allSprites.add(crosshair)

img = ["Zombie.png", "FlagZombie.png", "CaveZombie.png"]

for i in range(level*5):
  spawn = Zombies(random.choice(img))
  spawn.rect.x = random.randrange(200, 700)
  spawn.rect.y = random.randrange(200, 600)
  zombies_list.add(spawn)
  allSprites.add(spawn)

while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         playing = False
   
   set_background("Background.png")
   position = pygame.mouse.get_pos()
   crosshair.pos = position
   allSprites.draw(screen)
   pygame.display.update()