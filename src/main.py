import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, TEXT_PATH
from game import Game
from menu import Menu
from scrolling_text import ScrollingText

# Import text assets dynamically from the text_assets module
import importlib.util
spec = importlib.util.spec_from_file_location("text_assets", TEXT_PATH + "text_assets.py")
text_assets = importlib.util.module_from_spec(spec)
spec.loader.exec_module(text_assets)

class HeroesOfParaisopolis:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Heroes of Paraisópolis")
        self.clock = pygame.time.Clock()

        # Fonts
        self.menu_font = pygame.font.Font(None, 80)
        self.text_font = pygame.font.Font(None, 40)

        # Game states
        self.STATE_MENU = "menu"
        self.STATE_GAME = "game"
        self.current_state = self.STATE_MENU

        # Components
        self.menu = Menu(self.screen, self.menu_font, text_assets)
        self.game = Game(self.screen)
        self.scrolling_text = ScrollingText(self.screen, self.text_font, text_assets.SCROLLING_TEXT)

        # Timer for transitioning from menu to game
        self.menu_start_time = pygame.time.get_ticks()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Check if 5 seconds have passed to transition to the game screen
            if self.current_state == self.STATE_MENU:
                elapsed_time = pygame.time.get_ticks() - self.menu_start_time
                if elapsed_time >= 5000:  # 5000 milliseconds = 5 seconds
                    self.current_state = self.STATE_GAME

            # Render based on the current state
            if self.current_state == self.STATE_MENU:
                self.menu.render()
            elif self.current_state == self.STATE_GAME:
                self.scrolling_text.render(0.7)

            # Update the display
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = HeroesOfParaisopolis()
    game.run()