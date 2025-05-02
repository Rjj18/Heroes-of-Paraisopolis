import pygame
from settings import SCREEN_WIDTH, WHITE

def render_scrolling_text(screen, font, text_lines, text_y, speed=1):
    """
    Renders scrolling text on the screen.
    :param screen: The pygame screen object.
    :param font: The font to render the text.
    :param text_lines: A list of strings to render as scrolling text.
    :param text_y: The current vertical position of the text.
    :param speed: The speed at which the text scrolls upwards.
    :return: The updated vertical position of the text.
    """
    # Calculate line height dynamically based on the font size
    line_height = font.get_linesize()

    for i, line in enumerate(text_lines):
        text_surface = font.render(line, True, WHITE)
        screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, text_y + i * line_height))
    
    # Move the text upwards
    text_y -= speed
    return text_y