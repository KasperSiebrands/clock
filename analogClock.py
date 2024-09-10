import pygame # add the libary for this assignment (recommended)
import math # add the possibility to use math or functions to be used for the watch

#initialize Pygame
pygame.init()

#set up display
screen = pygame.display.set_mode((800, 800))   #800,800 is pixel size of the window
pygame.display.set_caption("Analog Watch by Kasper Siebrands") # added a name for my watch
screen.fill((255, 255, 255)) # Fill the screen with white

#setup clock
pygame.draw.circle(screen, (0, 0, 0), (400,400), 380, 3) #where to draw, colour, placement, radius, width

# Make sure the window stays open until the user closes it copied from draw.py
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip() # Refresh the screen so drawing appears

