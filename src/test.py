import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE
from title import Title
from opening import Opening
from text.text_assets import TITLE_TEXT, SCROLLING_TEXT

class NewScreen:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font

    def render(self):
        # Fill the screen with a color (e.g., blue)
        self.screen.fill((0, 0, 255))

        # Render some text in the center of the screen
        text = self.font.render("New Screen", True, WHITE)
        text_x = SCREEN_WIDTH // 2 - text.get_width() // 2
        text_y = SCREEN_HEIGHT // 2 - text.get_height() // 2
        self.screen.blit(text, (text_x, text_y))

# Add the new screen to the test setup
new_screen = NewScreen(screen, title_font)

# Update the main loop to include the new screen
current_screen = "new_screen"  # Start with the new screen for testing

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Render the current screen
    if current_screen == "title":
        title_screen.render()
    elif current_screen == "scrolling_text":
        scrolling_text_screen.render(0.7)
    elif current_screen == "new_screen":
        new_screen.render()

    # Update the display
    pygame.display.flip()