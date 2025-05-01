import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE

def render_menu(screen, menu_font):
    menu_text = menu_font.render("Iniciar Aventura", True, WHITE)
    screen.blit(menu_text, (SCREEN_WIDTH // 2 - menu_text.get_width() // 2, SCREEN_HEIGHT // 2 + 150))