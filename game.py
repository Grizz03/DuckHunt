import pygame
import sys
import random

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
crosshair = pygame.image.load('./shooting range assets/crosshair.png')
duck = pygame.image.load('./shooting range assets/duck.png')

# Animations
land_position_y = 600
land_speed = 1
water_position_y = 620
water_speed = 1

# Creating duck list to place ducks everywhere
duck_list = []

# Repeats 20 objects
for x in range(20):
    # Generating random number for rectangle position
    duck_position_x = random.randrange(50,1200)
    duck_position_y = random.randrange(120,630)
    duck_rect = duck.get_rect(center=(duck_position_x,duck_position_y))
    duck_list.append(duck_rect)

# MAIN GAME LOOP
while True:
    # While loop for closing game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Creating rectangle around mouse cursor with rect for crosshair
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair.get_rect(center=event.pos)

    # Applying background (background always on top)
    screen.blit(wood_bg, (0, 0))

    screen.blit(cloud1, (150, 50))
    screen.blit(cloud1, (600, 150))
    screen.blit(cloud2, (800, 100))
    screen.blit(cloud2, (300, 100))

    # duck image
    for duck_rect in duck_list:
        screen.blit(duck, duck_rect)

    # Animation ranges of water
    # Makes water move down the y-axis
    water_position_y -= water_speed
    # When object reaches y-axis points it will move UP the y-axis
    if water_position_y <= 590 or water_position_y >= 640:
        water_speed *= -1

    # calling crosshair and the rectangle around mouse(crosshair_rect)
    screen.blit(crosshair,crosshair_rect)
    # Setting images in game
    screen.blit(land_bg, (0, land_position_y))
    screen.blit(water_bg, (0, water_position_y))
    # constant game loop with update()
    pygame.display.update()
    # framerate of game
    clock.tick(100)

#     Rect recap for crosshair
# 1. import the picture.
# 2. we draw a rectangle around that surface.
# 3. we place the center of that rectangle on the position of the mouse.
