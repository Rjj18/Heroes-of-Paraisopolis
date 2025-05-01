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

# Load images for sword and shield
sword_image = pygame.image.load("assets/images/sword_normal.png")
shield_image = pygame.image.load("assets/images/a_shield_kite_gold.png")

# Scale images to match the height of the title
title_height = title_text.get_height()
sword_image = pygame.transform.scale(sword_image, (int(title_height * 0.5), title_height))
shield_image = pygame.transform.scale(shield_image, (int(title_height * 0.75), title_height))

# Load background music
pygame.mixer.music.load("assets/sounds/Cheers For Starlight Loop.mp3")
pygame.mixer.music.play(-1)  # Loop the music indefinitely

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a black background
    screen.fill(BLACK)

    # Calculate positions for sword, title, and shield
    total_width = sword_image.get_width() + title_text.get_width() + shield_image.get_width() + 40
    sword_x = SCREEN_WIDTH // 2 - total_width // 2
    title_x = sword_x + sword_image.get_width() + 20
    shield_x = title_x + title_text.get_width() + 20

    # Draw the sword on the left
    screen.blit(sword_image, (sword_x, SCREEN_HEIGHT // 2 - sword_image.get_height() // 2))

    # Draw the title text in the center
    screen.blit(title_text, (title_x, SCREEN_HEIGHT // 2 - title_text.get_height() // 2))

    # Draw the shield on the right
    screen.blit(shield_image, (shield_x, SCREEN_HEIGHT // 2 - shield_image.get_height() // 2))

    # Draw the menu text closer to halfway to the bottom of the screen
    screen.blit(menu_text, (SCREEN_WIDTH // 2 - menu_text.get_width() // 2, SCREEN_HEIGHT // 2 + 150))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()