import pygame # add the libary for this assignment (recommended)
import math # add the possibility to use math or functions to be used for the watch

#initialize Pygame
pygame.init()

#set up display
screen = pygame.display.set_mode((800, 800))   #800,800 is pixel size of the window
pygame.display.set_caption("Analog Watch by Kasper Siebrands") # added a name for my watch
screen.fill((255, 255, 255)) # Fill the screen with white

clock_color = (0,0,0)
clock_position = (400, 400)
clock_radius = 380
clock_widht = 3

#setup clock
pygame.draw.circle(screen, clock_color, clock_position, clock_radius, clock_widht) #where to draw, colour, placement, radius, width

# Make sure the window stays open until the user closes it copied from draw.py
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip() # Refresh the screen so drawing appears

