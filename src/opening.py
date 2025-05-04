import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE

class Opening:
    def __init__(self, screen, font, text_lines):
        self.screen = screen
        self.font = font
        self.text_lines = text_lines
        self.text_y = SCREEN_HEIGHT  # Start the text at the bottom of the screen

    def render(self, speed=1):
        self.screen.fill(BLACK)
        for i, line in enumerate(self.text_lines):
            text_surface = self.font.render(line, True, WHITE)
            self.screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, self.text_y + i * self.font.get_linesize()))
        self.text_y -= speed

    def out_of_bounds(self):
        # Check if the text has scrolled completely off the screen
        last_line_y = self.text_y + len(self.text_lines) * self.font.get_linesize()
        return last_line_y < 0
