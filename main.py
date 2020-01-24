import sys
import random
import string
import sys
import pygame
import pygame.font
from settings import Settings
from lowerthird import Lowerthird
from button import Button
from button3 import Button1


class GGame:
    def __init__(self):
        super().__init__()
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Diggers")
        FONT = pygame.font.SysFont('Comic Sans MS', 32)
        self.lowerthird = Lowerthird(self)
        

    
    def increment_number(self):
        """Callback method to increment the number."""
        self.number += 1
        print(self.number)

       
    def run_game(self):
            """Start the main loop for the game."""
            while True:
                self._check_events()
                self._update_screen()
                # self.game.run()


    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
        
    def _create_fleet(self):
        print('FUCKWIT')


  

    def _check_keydown_events(self, event):
            """Respond to keypresses."""
            if event.key == pygame.K_RIGHT:
                self.settings.chances += -1
            # elif event.key == pygame.K_LEFT:
            #     self.ship.moving_left = True
            if event.key == pygame.K_q:
                sys.exit()
            # elif event.key == pygame.K_SPACE:
            #     self._fire_bullet(

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.blit(self.settings.bg_image,(0,0) )
        # self.buttons.draw(self.screen)
        # Draw the chances text
        self.lowerthird.prep_hint()
        self.lowerthird.prep_chances()
        #


        pygame.display.flip()

if __name__ == '__main__':
    ss = GGame()
    ss.run_game()
    
















#