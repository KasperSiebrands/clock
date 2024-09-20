import pygame # add the libary for this assignment (recommended)
import math # add the possibility to use math or functions to be used for the watch

#initialize Pygame
pygame.init()

#set up display
screen = pygame.display.set_mode((800, 800))   #800,800 is pixel size of the window
pygame.display.set_caption("Analog Watch by Kasper Siebrands") # added a name for my watch
screen.fill((255, 255, 255)) # Fill the screen with white

big_clock_color = (0,0,0)
big_clock_position = (400, 400)
big_clock_radius = 380
big_clock_widht = 3

small_clock_color = (0,0,0)
small_clock_position = (400, 590)
small_clock_radius = 150
small_clock_width = 2

#setup clock
pygame.draw.circle(screen, big_clock_color, big_clock_position, big_clock_radius, big_clock_widht) #where to draw, colour, placement, radius, width
pygame.draw.circle(screen, small_clock_color, small_clock_position, small_clock_radius, small_clock_width) #where to draw, colour, placement, radius, width

# Make sure the window stays open until the user closes it copied from draw.py
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip() # Refresh the screen so drawing appears

