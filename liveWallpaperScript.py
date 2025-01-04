import pygame
import os
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Font settings
font = pygame.font.Font(None, 120)
background_color = (27, 38, 59)  # Black background
text_color = (167, 211, 219)  # White text

# mark startdateTime object

startTime = datetime(2001,2,15)


# Main loop
running = True
while running:
    # Calculate elapsed time
    currentTime = datetime.today()

    diffDate = relativedelta(currentTime,startTime)

    years = diffDate.years
    months = diffDate.months
    days = diffDate.days
    
    hours = diffDate.hours
    minutes = diffDate.minutes
    seconds = diffDate.seconds 

    
    time_str = f"{years:02}years {months:02}months {days:02}days\n{hours:02}:{minutes:02}:{seconds:02}"

    # Create a surface
    surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    surface.fill(background_color)

    # Render the text
    lines = time_str.split("\n")
    y_offset = SCREEN_HEIGHT // 2 - (len(lines) * font.get_height()) // 2  # Center vertically
    
    for line in lines:
        text_surface = font.render(line, True, text_color)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
        surface.blit(text_surface, text_rect)
        y_offset += font.get_height()  # Move down for the next line


    # Save the surface as an image
    pygame.image.save(surface, "/tmp/live_wallpaper.png")

    # Set the image as the wallpaper using feh
    feh_command = f"feh --bg-scale /tmp/live_wallpaper.png"
    os.system(feh_command)

    # Wait for 1 second
    time.sleep(1)

