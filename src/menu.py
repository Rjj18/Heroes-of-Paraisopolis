import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, TEXT_PATH

# Import text assets dynamically from the text_assets module
import importlib.util
spec = importlib.util.spec_from_file_location("text_assets", TEXT_PATH + "text_assets.py")
text_assets = importlib.util.module_from_spec(spec)
spec.loader.exec_module(text_assets)

class Menu:
    def __init__(self, screen, font, text_assets):
        self.screen = screen
        self.font = font
        self.text_assets = text_assets

    def render(self):
        menu_text = self.font.render(self.text_assets.MENU_TEXT["title"], True, WHITE)
        self.screen.fill((0, 0, 0))  # Clear the screen with black
        self.screen.blit(menu_text, (SCREEN_WIDTH // 2 - menu_text.get_width() // 2, SCREEN_HEIGHT // 2))