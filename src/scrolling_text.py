import pygame
from settings import SCREEN_WIDTH, BLACK, WHITE

class ScrollingText:
    def __init__(self, screen, font, text_lines):
        self.screen = screen
        self.font = font
        self.text_lines = text_lines
        self.text_y = SCREEN_WIDTH  # Start the text at the bottom of the screen

    def render(self, speed=1):
        self.screen.fill(BLACK)
        line_height = self.font.get_linesize()
        for i, line in enumerate(self.text_lines):
            text_surface = self.font.render(line, True, WHITE)
            self.screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, self.text_y + i * line_height))
        self.text_y -= speed