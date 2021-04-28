import pygame
import sys

pygame.init()

# Initialize screen size
screen = pygame.display.set_mode((1280, 720))

# Creates clock object for same framerate for every computer
clock = pygame.time.Clock()

# Importing images
wood_bg = pygame.image.load('./shooting range assets/Wood_BG.png')
land_bg = pygame.image.load('./shooting range assets/Land_BG.png')
water_bg = pygame.image.load('./shooting range assets/Water_BG.png')
cloud1 = pygame.image.load('./shooting range assets/Cloud1.png')
cloud2 = pygame.image.load('./shooting range assets/Cloud2.png')

# Animations
land_position_y = 550
land_speed = 1

water_position_y = 620
water_speed = 1

while True:
    # While loop for closing game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Applying background (background always on top)
    screen.blit(wood_bg, (0, 0))

    # Animation ranges of water
    # Makes water move down the y-axis
    water_position_y -= water_speed
    # When object reaches y-axis points it will move UP the y-axis
    if water_position_y <= 590 or water_position_y >= 640:
        water_speed *= -1

    # Setting images in game
    screen.blit(land_bg, (0, land_position_y))
    screen.blit(water_bg, (0, water_position_y))
    screen.blit(cloud1, (150, 50))
    screen.blit(cloud1, (600, 150))
    screen.blit(cloud2, (800, 100))
    screen.blit(cloud2, (300, 100))
    pygame.display.update()
    clock.tick(60)
