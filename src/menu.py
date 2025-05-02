import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, TEXT_PATH

# Import text assets dynamically from the text_assets module
import importlib.util
spec = importlib.util.spec_from_file_location("text_assets", TEXT_PATH + "text_assets.py")
text_assets = importlib.util.module_from_spec(spec)
spec.loader.exec_module(text_assets)

def render_menu(screen, menu_font):
    menu_text = menu_font.render(text_assets.MENU_TEXT["start_adventure"], True, WHITE)
    screen.blit(menu_text, (SCREEN_WIDTH // 2 - menu_text.get_width() // 2, SCREEN_HEIGHT // 2 + 150))