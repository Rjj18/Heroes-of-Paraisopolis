import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE, TEXT_PATH
from game import load_assets, render_game
from menu import render_menu
from scrolling_text import render_scrolling_text

# Import text assets dynamically from the text_assets module
import importlib.util
spec = importlib.util.spec_from_file_location("text_assets", TEXT_PATH + "text_assets.py")
text_assets = importlib.util.module_from_spec(spec)
spec.loader.exec_module(text_assets)

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Heroes of Paraisópolis")

# Fonts
title_font = pygame.font.Font(None, 74)
menu_font = pygame.font.Font(None, 30)
text_font = pygame.font.Font(None, 40)

# Load assets
sword_image, shield_image, _ = load_assets()  # Ignore the background image for now

# Game states
STATE_MENU = "menu"
STATE_GAME = "game"
current_state = STATE_MENU

# Scrolling text
scrolling_text = text_assets.SCROLLING_TEXT  # Use SCROLLING_TEXT from text_assets
text_y = SCREEN_HEIGHT  # Start the text at the bottom of the screen

# Timer for transitioning from menu to game
menu_start_time = pygame.time.get_ticks()  # Record the time when the menu starts

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if 5 seconds have passed to transition to the game screen
    if current_state == STATE_MENU:
        elapsed_time = pygame.time.get_ticks() - menu_start_time
        if elapsed_time >= 5000:  # 5000 milliseconds = 5 seconds
            current_state = STATE_GAME

    # Render based on the current state
    if current_state == STATE_MENU:
        # Render the game screen
        render_game(screen, title_font, sword_image, shield_image)

        # Render the menu
        render_menu(screen, menu_font)
    elif current_state == STATE_GAME:
        # Render a simple black screen with scrolling text
        screen.fill(BLACK)
        text_y = render_scrolling_text(screen, text_font, scrolling_text, text_y, 0.03)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()