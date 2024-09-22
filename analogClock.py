import pygame # add the libary for this assignment (recommended)
import math # add the possibility to use math or functions to be used for the watch
from datetime import datetime

#initialize Pygame
pygame.init()

#set up display
screen = pygame.display.set_mode((800, 800))   #800,800 is pixel size of the window
pygame.display.set_caption("Analog Watch by Kasper Siebrands") # added a name for my watch
background_color = (255,255,255)

screen.fill((255, 255, 255)) #backgroundcolor white...

clock = pygame.time.Clock()

big_clock_color = (0,0,0)
big_clock_position = (400, 400)
big_clock_radius = 380
big_clock_widht = 5

small_clock_color = (0,0,0)
small_clock_position_left = (250, 525)
small_clock_position_right = (550, 525)
small_clock_radius = 100
small_clock_width = 3

line_color_seconds = (0,0,0)
line_width_seconds = 3
x_center_small_clock_left, y_center_small_clock_left = 250, 525
x_center_small_clock_right, y_center_small_clock_right = 550, 525



#Make sure the window stays open until the user closes it copied from draw.py
run_flag = True
while run_flag is True:
    screen.fill(background_color) # refresh background

    #setup clock big
    pygame.draw.circle(screen, big_clock_color, big_clock_position, big_clock_radius, big_clock_widht) #where to draw, colour, placement, radius, width

    #setup clock small left
    pygame.draw.circle(screen, small_clock_color, small_clock_position_left, small_clock_radius, small_clock_width) #where to draw, colour, placement, radius, width
    #setup clock small right
    pygame.draw.circle(screen, small_clock_color, small_clock_position_right, small_clock_radius, small_clock_width) #where to draw, colour, placement, radius, width


    now = datetime.now()
    seconds = now.second
    milliseconds = now.microsecond // 1000
    
    angle_seconds = math.radians(seconds * 6)
    
    angle_milliseconds = math.radians(milliseconds * 0.36)
    
    # Calculate the end position of the second for left circle
    length_small_clock = 90  # Length of the second
    x_end_small_clock_left = x_center_small_clock_left + length_small_clock * math.sin(angle_seconds) #calculate the end of the line
    y_end_small_clock_left = y_center_small_clock_left - length_small_clock * math.cos(angle_seconds) #calculate the end of the line

    x_end_small_clock_right = x_center_small_clock_right + length_small_clock * math.sin(angle_milliseconds) #calculate the end of the line
    y_end_small_clock_right = y_center_small_clock_right - length_small_clock * math.cos(angle_milliseconds) #calculate the end of the line

    # Draw the second hand left
    pygame.draw.line(screen, line_color_seconds, (x_center_small_clock_left, y_center_small_clock_left), (x_end_small_clock_left, y_end_small_clock_left), line_width_seconds)  #aaline is more soft around edges...

    # Draw the second hand right
    pygame.draw.line(screen, line_color_seconds, (x_center_small_clock_right, y_center_small_clock_right), (x_end_small_clock_right, y_end_small_clock_right), line_width_seconds)  #aaline is more soft around edges...




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False

    pygame.display.flip()  # Refresh the screen so drawing appears

    # Limit the framerate to 24 FPS
    clock.tick(24)

pygame.quit()