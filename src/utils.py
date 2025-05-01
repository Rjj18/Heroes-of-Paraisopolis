import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, IMAGES_PATH, SOUNDS_PATH

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Assets paths
ASSETS_PATH = "../assets/"
IMAGES_PATH = ASSETS_PATH + "images/"
SOUNDS_PATH = ASSETS_PATH + "sounds/"

def load_assets():
    # Load images
    sword_image = pygame.image.load(IMAGES_PATH + "sword_normal.png")
    shield_image = pygame.image.load(IMAGES_PATH + "a_shield_kite_gold.png")

    # Load background music
    pygame.mixer.music.load(SOUNDS_PATH + "Cheers For Starlight Loop.mp3")
    pygame.mixer.music.play(-1)  # Loop the music indefinitely

    return sword_image, shield_image

def render_menu(screen, menu_font):
    menu_text = menu_font.render("Iniciar Aventura", True, WHITE)
    screen.blit(menu_text, (SCREEN_WIDTH // 2 - menu_text.get_width() // 2, SCREEN_HEIGHT // 2 + 150))

def render_game(screen, title_font, sword_image, shield_image):
    # Render title
    title_text = title_font.render("Heroes of Paraisópolis", True, WHITE)

    # Scale images to match the height of the title
    title_height = title_text.get_height()
    sword_image = pygame.transform.scale(sword_image, (int(title_height * 0.5), title_height))
    shield_image = pygame.transform.scale(shield_image, (int(title_height * 0.75), title_height))

    # Calculate positions for sword, title, and shield
    total_width = sword_image.get_width() + title_text.get_width() + shield_image.get_width() + 40
    sword_x = SCREEN_WIDTH // 2 - total_width // 2
    title_x = sword_x + sword_image.get_width() + 20
    shield_x = title_x + title_text.get_width() + 20

    # Fill the screen with a black background
    screen.fill(BLACK)

    # Draw the sword on the left
    screen.blit(sword_image, (sword_x, SCREEN_HEIGHT // 2 - sword_image.get_height() // 2))

    # Draw the title text in the center
    screen.blit(title_text, (title_x, SCREEN_HEIGHT // 2 - title_text.get_height() // 2))

    # Draw the shield on the right
    screen.blit(shield_image, (shield_x, SCREEN_HEIGHT // 2 - shield_image.get_height() // 2))

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