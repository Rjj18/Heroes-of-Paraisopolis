import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, SOUNDS_PATH, TEXT_PATH
# Import text assets dynamically from the text_assets module
import importlib.util
spec = importlib.util.spec_from_file_location("text_assets", TEXT_PATH + "text_assets.py")
text_assets = importlib.util.module_from_spec(spec)
spec.loader.exec_module(text_assets)

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.load_music()  # Load and play music

    def load_music(self):
        pygame.mixer.music.load(SOUNDS_PATH + "Cheers For Starlight Loop.mp3")
        pygame.mixer.music.play(-1)  # Loop the music indefinitely

   