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
length_big_clock_minutes = 360
length_big_clock_hours = 300

small_clock_color = (0,0,0)
small_clock_position_left = (250, 525)
small_clock_position_right = (550, 525)
small_clock_radius = 100
small_clock_width = 3
length_small_clock_seconds = 90  # Length of the second

line_color_seconds = (0,0,0)
line_width_seconds = 3
line_width_minutes = 3
line_width_hours = 5


x_center_small_clock_left, y_center_small_clock_left = small_clock_position_left
x_center_small_clock_right, y_center_small_clock_right = small_clock_position_right
x_center_big_clock_minutes, y_center_big_clock_minutes = big_clock_position[0], big_clock_position[1]
x_center_big_clock_hours, y_center_big_clock_hours = big_clock_position[0], big_clock_position[1]




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
    hours = now.hour % 12 #12 is needed to make it a 12 hour clock, otherwise it wont be like an analog clock...
    minutes = now.minute
    seconds = now.second
    milliseconds = now.microsecond // 1000
    
    #made a mistake earlier with calucation of miliseconds so now with explanation...
    angle_hours = math.radians(hours * 30)  # 360 degrees / 12 hours = 30 degrees per hour
    angle_minutes = math.radians(minutes * 6)  # 360 degrees for whole circle / 60 minutes = 6 degrees per minute
    angle_seconds = math.radians(seconds * 6) # 360 degrees / 60 seconds = 6 degrees per second
    angle_milliseconds = math.radians(milliseconds * 0.36) # 360 degrees / 1000 milliseconds = 0.36 degrees per millisecond

    # Calculate the end position of the hours for big circle
    x_end_big_clock_hours = x_center_big_clock_hours + length_big_clock_hours * math.sin(angle_hours) #calculate the end of the line
    y_end_bog_clock_hours = y_center_big_clock_hours - length_big_clock_hours * math.cos(angle_hours) #calculate the end of the line
    
    # Calculate the end position of the minutes for big circle
    x_end_big_clock_minutes = x_center_big_clock_minutes + length_big_clock_minutes * math.sin(angle_minutes) #calculate the end of the line
    y_end_bog_clock_minutes = y_center_big_clock_minutes - length_big_clock_minutes * math.cos(angle_minutes) #calculate the end of the line
    
    # Calculate the end position of the second for left circle
    x_end_small_clock_left = x_center_small_clock_left + length_small_clock_seconds * math.sin(angle_seconds) #calculate the end of the line
    y_end_small_clock_left = y_center_small_clock_left - length_small_clock_seconds * math.cos(angle_seconds) #calculate the end of the line

   # Calculate the end position of the second for right circle
    x_end_small_clock_right = x_center_small_clock_right + length_small_clock_seconds * math.sin(angle_milliseconds) #calculate the end of the line
    y_end_small_clock_right = y_center_small_clock_right - length_small_clock_seconds * math.cos(angle_milliseconds) #calculate the end of the line


    # Draw the hours big clock
    pygame.draw.line(screen, line_color_seconds, (x_center_big_clock_hours, y_center_big_clock_hours), (x_end_big_clock_hours, y_end_bog_clock_hours), line_width_hours)  #aaline is more soft around edges...
    # Draw the minutes big clock
    pygame.draw.line(screen, line_color_seconds, (x_center_big_clock_minutes, y_center_big_clock_minutes), (x_end_big_clock_minutes, y_end_bog_clock_minutes), line_width_minutes)  #aaline is more soft around edges...
    # Draw the second hand left
    pygame.draw.line(screen, line_color_seconds, (x_center_small_clock_left, y_center_small_clock_left), (x_end_small_clock_left, y_end_small_clock_left), line_width_seconds)  #aaline is more soft around edges...
    # Draw the second hand right
    pygame.draw.line(screen, line_color_seconds, (x_center_small_clock_right, y_center_small_clock_right), (x_end_small_clock_right, y_end_small_clock_right), line_width_seconds)  #aaline is more soft around edges...




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False

    pygame.display.flip()  # Refresh the screen so drawing appears

    # Limit the framerate to 24 FPS
    clock.tick(25)

pygame.quit()