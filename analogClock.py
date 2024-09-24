import pygame # add the libary for this assignment (recommended)
import math # add the possibility to use math or functions to be used for the watch
from datetime import datetime

#initialize Pygame
pygame.init()

#set up display
screen = pygame.display.set_mode((800, 800))   #800,800 is pixel size of the window
pygame.display.set_caption("Analog Watch by Kasper Siebrands") # added a name for my watch
background_color = (255,255,255)

clock = pygame.time.Clock()

#information about big clock, where hours and minutes are shown
big_clock_color = (0,0,0)
big_clock_position = (400, 400)
big_clock_radius = 380
big_clock_widht = 10
big_clock_hour_text_lenght =  40
big_clock_text_space = 2

#information about the little center-dot to show the middle of the each clock  
dot_big_clock_radius = 10
dot_big_clock_width = 100

dot_small_clock_radius = 5
dot_small_clock_width = 100

#information about the smaller clocks inside the bigger one, here are seconds and miliseconds shown.
small_clock_color = (100,100,100)
small_clock_position_left = (250, 525)
small_clock_position_right = (550, 525)
small_clock_radius = 100
small_clock_width = 5
small_clock_text_space = 2

#information about the hands who show what time it is.
line_color_hours = (0,0,0)
line_width_hours = 10
line_length_big_clock_hours = 200

line_color_minutes = (0,0,0)
line_width_minutes = 10
line_length_big_clock_minutes = 350
minute_text_length = 20

line_color_seconds = (100,100,100)
line_width_seconds = 3
line_lenght_small_clock_seconds = 90
second_text_length = 10

#calculation for smaller en bigger clocks.
x_center_small_clock_left, y_center_small_clock_left = small_clock_position_left
x_center_small_clock_right, y_center_small_clock_right = small_clock_position_right

x_center_big_clock_minutes, y_center_big_clock_minutes = big_clock_position[0], big_clock_position[1]
x_center_big_clock_hours, y_center_big_clock_hours = big_clock_position[0], big_clock_position[1]

#Make sure the window stays open until the user closes it copied from draw.py
#here is the loop where all animations happen...
run_flag = True
while run_flag is True:
    screen.fill(background_color) # refresh background

    #setup clock big
    pygame.draw.circle(screen, big_clock_color, big_clock_position, big_clock_radius, big_clock_widht) #where to draw, colour, placement, radius, width
    #setup clock small left
    pygame.draw.circle(screen, small_clock_color, small_clock_position_left, small_clock_radius, small_clock_width) #where to draw, colour, placement, radius, width
    #setup clock small right
    pygame.draw.circle(screen, small_clock_color, small_clock_position_right, small_clock_radius, small_clock_width) #where to draw, colour, placement, radius, width

    #draw small circle in the middle 
    pygame.draw.circle(screen, big_clock_color, big_clock_position, dot_big_clock_radius, dot_big_clock_width)
    pygame.draw.circle(screen, small_clock_color, small_clock_position_left, dot_small_clock_radius, dot_small_clock_width)
    pygame.draw.circle(screen, small_clock_color, small_clock_position_right, dot_small_clock_radius, dot_small_clock_width)

    #added numbers to the hours
    font = pygame.font.SysFont(None, 40)
    for hour in range(1, 13): #1-13 is 12 steps....
        angle_text_hour = math.radians(hour * 30 - 90)  # 30 degrees per hour, -90 to start at the top
        x = big_clock_position[0] + (big_clock_radius - big_clock_hour_text_lenght) * math.cos(angle_text_hour) #calculate where to place x
        y = big_clock_position[1] + (big_clock_radius - big_clock_hour_text_lenght) * math.sin(angle_text_hour) #calculate where to place y
        text = font.render(str(hour), True, big_clock_color) #render in text
        text_rect = text.get_rect(center=(x, y)) #setting up possition for text
        screen.blit(text, text_rect) #draw the text

    #added numbers to the seconds
    font = pygame.font.SysFont(None, 10)
    for second in range(1, 61): #1-61 is 60 steps....
        angle_text_seconds = math.radians(second * 6 - 90)  # 30 degrees per hour, -90 to start at the top
        x = small_clock_position_left[0] + (small_clock_radius - 20) * math.cos(angle_text_seconds) #calculate where to place x
        y = small_clock_position_left[1] + (small_clock_radius - 20) * math.sin(angle_text_seconds) #calculate where to place y
        text = font.render(str(second), True, small_clock_color) #render in text
        text_rect = text.get_rect(center=(x, y)) #setting up possition for text
        screen.blit(text, text_rect) #draw the text

    #added numbers to the milliseconds
    font = pygame.font.SysFont(None, 10)
    for millisecond in range(0, 1000,50):  # 0-1000 in steps of 100... because 1000 is to much
        angle_text_milliseconds = math.radians(millisecond * 0.36 - 90)  # 30 degrees per hour, -90 to start at the top
        x = small_clock_position_right[0] + (small_clock_radius - 20) * math.cos(angle_text_milliseconds) #calculate where to place x
        y = small_clock_position_right[1] + (small_clock_radius - 20) * math.sin(angle_text_milliseconds) #calculate where to place y
        text = font.render(str(millisecond), True, small_clock_color) #render in text
        text_rect = text.get_rect(center=(x, y)) #setting up possition for text
        screen.blit(text, text_rect) #draw the text


     # Add second-marks to the small clock, it reads first in document so it's a lower layer than the minutemark so it overlaps as wanted.
    for second in range(60):
        angle_text_seconds = math.radians(second * 6 - 90)
        x_start = small_clock_position_left[0] + (small_clock_radius - second_text_length) * math.cos(angle_text_seconds)
        y_start = small_clock_position_left[1] + (small_clock_radius - second_text_length) * math.sin(angle_text_seconds)
        x_end = small_clock_position_left[0] + (small_clock_radius - small_clock_text_space) * math.cos(angle_text_seconds)
        y_end = small_clock_position_left[1] + (small_clock_radius - small_clock_text_space) * math.sin(angle_text_seconds)
        
        pygame.draw.line(screen, small_clock_color, (x_start, y_start), (x_end, y_end), 1)
        
    #add millisecond marks to the small clock
    for millisecond in range(0, 1000,50):
        angle_text_milliseconds = math.radians(millisecond * 0.36 - 90)
        x_start = small_clock_position_right[0] + (small_clock_radius - second_text_length) * math.cos(angle_text_milliseconds)
        y_start = small_clock_position_right[1] + (small_clock_radius - second_text_length) * math.sin(angle_text_milliseconds)
        x_end = small_clock_position_right[0] + (small_clock_radius - small_clock_text_space) * math.cos(angle_text_milliseconds)
        y_end = small_clock_position_right[1] + (small_clock_radius - small_clock_text_space) * math.sin(angle_text_milliseconds)
        
        pygame.draw.line(screen, small_clock_color, (x_start, y_start), (x_end, y_end), 1)
    
    # Add minute marks to the big clock
    for minute in range(60):
        angle_text_minutes = math.radians(minute * 6 - 90) #-90 to start at top
        x_start = big_clock_position[0] + (big_clock_radius - minute_text_length) * math.cos(angle_text_minutes)
        y_start = big_clock_position[1] + (big_clock_radius - minute_text_length) * math.sin(angle_text_minutes)
        x_end = big_clock_position[0] + (big_clock_radius - big_clock_text_space) * math.cos(angle_text_minutes) 
        y_end = big_clock_position[1] + (big_clock_radius - big_clock_text_space) * math.sin(angle_text_minutes) 
    
        pygame.draw.line(screen, big_clock_color, (x_start, y_start), (x_end, y_end), 4)
    
    now = datetime.now()
    hours = now.hour % 12 #12 is needed to make it a 12 hour clock, otherwise it wont be like an analog clock...
    minutes = now.minute
    seconds = now.second
    milliseconds = now.microsecond // 1000
    
    #made a mistake earlier with calucation of miliseconds so now with explanation...
    angle_hours = math.radians((hours + minutes / 60 + seconds / 3600) * 30)  # 360 degrees / 12 hours = 30 degrees per hour, added fraction of minutes and seconds so it moves not only att 09:59 to 10:00 but progresses.
    angle_minutes = math.radians(minutes * 6)  # 360 degrees for whole circle / 60 minutes = 6 degrees per minute
    angle_seconds = math.radians(seconds * 6) # 360 degrees / 60 seconds = 6 degrees per second
    angle_milliseconds = math.radians(milliseconds * 0.36) # 360 degrees / 1000 milliseconds = 0.36 degrees per millisecond

    # Calculate the end position of the hours for big circle
    x_end_big_clock_hours = x_center_big_clock_hours + line_length_big_clock_hours * math.sin(angle_hours) #calculate the end of the line
    y_end_big_clock_hours = y_center_big_clock_hours - line_length_big_clock_hours * math.cos(angle_hours) #calculate the end of the line
    
    # Calculate the end position of the minutes for big circle
    x_end_big_clock_minutes = x_center_big_clock_minutes + line_length_big_clock_minutes * math.sin(angle_minutes) #calculate the end of the line
    y_end_big_clock_minutes = y_center_big_clock_minutes - line_length_big_clock_minutes * math.cos(angle_minutes) #calculate the end of the line
    
    # Calculate the end position of the second for left circle
    x_end_small_clock_left = x_center_small_clock_left + line_lenght_small_clock_seconds * math.sin(angle_seconds) #calculate the end of the line
    y_end_small_clock_left = y_center_small_clock_left - line_lenght_small_clock_seconds * math.cos(angle_seconds) #calculate the end of the line

   # Calculate the end position of the second for right circle
    x_end_small_clock_right = x_center_small_clock_right + line_lenght_small_clock_seconds * math.sin(angle_milliseconds) #calculate the end of the line
    y_end_small_clock_right = y_center_small_clock_right - line_lenght_small_clock_seconds * math.cos(angle_milliseconds) #calculate the end of the line

    # Draw the millisecond hand right
    pygame.draw.line(screen, line_color_seconds, (x_center_small_clock_right, y_center_small_clock_right), (x_end_small_clock_right, y_end_small_clock_right), line_width_seconds)  #aaline is more soft around edges...
    
    # Draw the second hand left
    pygame.draw.line(screen, line_color_seconds, (x_center_small_clock_left, y_center_small_clock_left), (x_end_small_clock_left, y_end_small_clock_left), line_width_seconds)  #aaline is more soft around edges...

    # Draw the minutes big clock
    pygame.draw.line(screen, line_color_minutes, (x_center_big_clock_minutes, y_center_big_clock_minutes), (x_end_big_clock_minutes, y_end_big_clock_minutes), line_width_minutes)  #aaline is more soft around edges...
 
    # Draw the hours big clock
    pygame.draw.line(screen, line_color_hours, (x_center_big_clock_hours, y_center_big_clock_hours), (x_end_big_clock_hours, y_end_big_clock_hours), line_width_hours)  #aaline is more soft around edges...

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False

    pygame.display.flip()  # Refresh the screen so drawing appears

    #Limit the framerate to 60 FPS, better for a stopwatch to have a higher framerate...
    clock.tick(60)

pygame.quit()