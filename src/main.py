import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, TEXT_PATH
from title import Title
from opening import Opening

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
        self.title_font = pygame.font.Font(None, 80)
        self.opening_font = pygame.font.Font(None, 40)

        # Game states
        self.STATE_OPENING = "opening"
        self.STATE_TITLE = "title"
        self.current_state = self.STATE_OPENING

        # Components
        self.opening = Title(self.screen, self.title_font, text_assets)
        self.scrolling_text = Opening(self.screen, self.opening_font, text_assets.SCROLLING_TEXT)

        # Timer for transitioning from menu to game
        self.menu_start_time = pygame.time.get_ticks()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Render based on the current state
            if self.current_state == self.STATE_OPENING:
                self.scrolling_text.render(0.7)
                print(f"Current state: {self.current_state}")  # Debugging log
                print(f"Text Y position: {self.scrolling_text.text_y}")  # Debugging log
                if self.scrolling_text.out_of_bounds():
                    print("Text is out of bounds. Changing state to TITLE.")  # Debugging log
                    self.current_state = self.STATE_TITLE
                     # Change state to TITLE
            elif self.current_state == self.STATE_TITLE:
                self.opening.render()  # Render the title screen

            # Update the display
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = HeroesOfParaisopolis()
    game.run()