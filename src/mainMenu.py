import pygame
from settings import IMAGES_PATH

class MainMenu:
    def __init__(self, background_image, title, menu_items):
        self.background_image = background_image
        self.title = title
        self.menu_items = menu_items

# continuar com a função de renderização da imagem de fundo, do titulo e dos itens do menu