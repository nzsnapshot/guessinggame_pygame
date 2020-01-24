import pygame.font
from settings import Settings

class Lowerthird:
    """A class to report chances remaining and hints"""
    def __init__(self, ai_game):
        super().__init__()
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.settings = Settings()
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        # Font colors
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 100)
        self.hint_font = pygame.font.SysFont(None, 48)


        # Prepare the initial score images..
        self.prep_chances
        # self.prep_hint
        # self.prep_help
        # self.prep_letters

    def prep_hint(self):
        """Turns the hint into a rendered image."""
        self.hint = 'A type of animal'
        annoying_people = str(self.hint)
        self.hint_image = self.hint_font.render(annoying_people, True, self.text_color)
        # Displays the hint in the lower third

        self.hint_rect = self.hint_image.get_rect()
        self.hint_rect.right = self.screen_rect.right - 580
        self.hint_rect.top = 660
        self.screen.blit(self.hint_image, self.hint_rect)

    def prep_chances(self):
        """Turn the chances into a rendered image."""
        rounded_chance = str(self.settings.chances)
        self.chance_image = self.font.render(rounded_chance, True, self.text_color)

        # Displays the chances in the lower third
        self.chance_rect = self.chance_image.get_rect()
        self.chance_rect.right = self.screen_rect.right - 1065
        self.chance_rect.top = 660

        self.screen.blit(self.chance_image, self.chance_rect)

