import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, IMAGES_PATH, SOUNDS_PATH

def load_assets():
    # Load images
    sword_image = pygame.image.load(IMAGES_PATH + "sword_normal.png")  # Sword image
    shield_image = pygame.image.load(IMAGES_PATH + "a_shield_kite_gold.png")  # Shield image
    background_image = pygame.image.load(IMAGES_PATH + "castle_entrance.png")  # Background image

    # Scale the background to fit the screen dimensions
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Load background music
    pygame.mixer.music.load(SOUNDS_PATH + "Cheers For Starlight Loop.mp3")  # Background music
    pygame.mixer.music.play(-1)  # Loop the music indefinitely

    return sword_image, shield_image, background_image

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