import pygame
import sys

pygame.init()

# initialize screen size
screen = pygame.display.set_mode((1280, 720))

# creates clock object for same framerate for every computer
clock = pygame.time.Clock()

# importing images
wood_bg = pygame.image.load('./shooting range assets/Wood_BG.png')


while True:
    # while loop for closing game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    # applying background
    screen.blit(wood_bg,(0,0))
    pygame.display.update()
    clock.tick(60)
