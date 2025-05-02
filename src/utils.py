import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK
from text_assets import TITLE_TEXT, MENU_TEXT

def render_screen(screen, title_font, menu_font):
    # Fill the screen with a black background
    screen.fill(BLACK)

    # Render title
    title_text = title_font.render(TITLE_TEXT, True, WHITE)
    title_x = SCREEN_WIDTH // 2 - title_text.get_width() // 2
    title_y = SCREEN_HEIGHT // 2 - title_text.get_height() // 2 - 50  # Position slightly above the center
    screen.blit(title_text, (title_x, title_y))

    # Render menu text
    menu_text = menu_font.render(MENU_TEXT["start_adventure"], True, WHITE)
    menu_x = SCREEN_WIDTH // 2 - menu_text.get_width() // 2
    menu_y = SCREEN_HEIGHT // 2 + 50  # Position slightly below the center
    screen.blit(menu_text, (menu_x, menu_y))

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Heroes of Paraisópolis")

# Fonts
title_font = pygame.font.Font(None, 74)
menu_font = pygame.font.Font(None, 30)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Render the screen with both title and menu
    render_screen(screen, title_font, menu_font)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()