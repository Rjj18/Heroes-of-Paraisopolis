import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from game import load_assets, render_game
from menu import render_menu

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Heroes of Paraisópolis")

# Fonts
title_font = pygame.font.Font(None, 74)
menu_font = pygame.font.Font(None, 30)

# Load assets
sword_image, shield_image = load_assets()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Render the game screen
    render_game(screen, title_font, sword_image, shield_image)

    # Render the menu
    render_menu(screen, menu_font)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()