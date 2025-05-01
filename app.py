import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Heroes of Paraisópolis")

# Font for the title and menu
title_font = pygame.font.Font(None, 74)
menu_font = pygame.font.Font(None, 30)  # Smaller font for the menu

# Render the title and menu text
title_text = title_font.render("Heroes of Paraisópolis", True, WHITE)
menu_text = menu_font.render("Iniciar Aventura", True, WHITE)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a black background
    screen.fill(BLACK)

    # Draw the title text
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 2 - title_text.get_height() // 2 - 100))

    # Draw the menu text closer to halfway to the bottom of the screen
    screen.blit(menu_text, (SCREEN_WIDTH // 2 - menu_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()