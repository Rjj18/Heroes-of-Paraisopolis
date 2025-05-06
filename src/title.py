import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, TEXT_PATH, SOUNDS_PATH

# Import text assets dynamically from the text_assets module
import importlib.util
spec = importlib.util.spec_from_file_location("text_assets", TEXT_PATH + "text_assets.py")
text_assets = importlib.util.module_from_spec(spec)
spec.loader.exec_module(text_assets)

class Title:
    def __init__(self, screen, font, text_assets):
        self.screen = screen
        self.font = font
        self.text_assets = text_assets
        self.load_music()

    def load_music(self):
        pygame.mixer.music.load(SOUNDS_PATH + "Cheers For Starlight Loop.mp3")
        pygame.mixer.music.play(-1)  # Loop the music indefinitely

    def render(self):
        title_text = self.font.render(self.text_assets.MENU_TEXT["title"], True, WHITE)
        self.screen.fill((0, 0, 0))  # Clear the screen with black
        self.screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 2))

    def is_text_out_of_bounds(self, text, x, y):
        text_width, text_height = self.font.size(text)
        if x < 0 or x + text_width > SCREEN_WIDTH or y < 0 or y + text_height > SCREEN_HEIGHT:
            return True
        return False