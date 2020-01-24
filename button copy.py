import pygame as pg
import string
import random
import sys
from settings import Settings

pg.init()
screen = pg.display.set_mode((800, 600))
FONT = pg.font.SysFont('Comic Sans MS', 32)
# Default button images/pygame.Surfaces.

colors = {"black":(0,0,0), "darkgray":(70,70,70), "gray":(128,128,128), "lightgray":(200,200,200), "white":(255,255,255), "red":(255,0,0),
          "darkred":(128,0,0),"green":(0,255,0),"darkgreen":(0,128,0), "blue":(0,0,255), "navy":(0,0,128), "darkblue":(0,0,128),
          "yellow":(255,255,0), "gold":(255,215,0), "orange":(255,165,0), "lilac":(229,204,255),"lightblue":(135,206,250),"teal":(0,128,128),
          "cyan":(0,255,255), "purple":(150,0,150), "pink":(238,130,238), "brown":(139,69,19), "lightbrown":(222,184,135),"lightgreen":(144,238,144),
          "turquoise":(64,224,208),"beige":(245,245,220),"honeydew":(240,255,240),"lavender":(230,230,250),"crimson":(220,20,60)}

# Button is a sprite subclass, that means it can be added to a sprite group.
# You can draw and update all sprites in a group by
# calling `group.update()` and `group.draw(screen)`.
class Button(pg.sprite.Sprite):
    def __init__(self, color, pos, width, height, letter, active = False, type = 1, size = 40):
        self.type = type 
        self.active = active   
        self.clicked = False   
        self.rollOver = False  
        self.size = size
        self.font = pg.font.SysFont(None, self.size)
        self.color = color
        self.letter = letter
        self.pos = pos
        self.width = width
        self.height = height
        self.rect = pg.Surface((self.width, self.height))         # CREATING A rect TO
        self.rect.fill(self.color)                                # GET A RECT (FOR COLLISION)
        self.image = self.font.render(self.letter, True, colors["white"])

    def handle_event(self, surface):
        if self.type == 1:
            if self.rollOver:                   # IF A TYPE 1 BUTTON IS UNDER
                self.rect.set_alpha(200)  # THE MOUSE, MAKE IT LESS VIBRANT
            else:
                self.rect.set_alpha(255)
            if not self.clicked:
                surface.blit(self.rect, self.pos)
                self.rect.blit(self.image, (self.width/4,self.height/5))
        if self.type == 2:
            if self.active:                     # IF A TYPE 2 BUTTON IS ACTIVE
                self.rect.set_alpha(255)  # MAKE IT'S COLOR MORE VIBRANT
            else:
                self.rect.set_alpha(100)
            surface.blit(self.rect, self.pos)
            self.rect.blit(self.image, (self.width / 4, self.height / 5))


    # def __init__(self, x, y, width, height, callback,
    #              font=FONT, text='', text_color=(0, 0, 0),
    #              image_normal=IMAGE_NORMAL, image_hover=IMAGE_HOVER,
    #              image_down=IMAGE_DOWN):
    #     super().__init__()
    #     # Scale the images to the desired size (doesn't modify the originals).
    #     self.image_normal = pg.transform.scale(image_normal, (width, height))
    #     self.image_hover = pg.transform.scale(image_hover, (width, height))
    #     self.image_down = pg.transform.scale(image_down, (width, height))

    #     self.image = self.image_normal  # The currently active image.
    #     self.rect = self.image.get_rect(topleft=(x, y))
        
    #     # To center the text rect.
    #     image_center = self.image.get_rect().center
    #     text_surf = font.render(text, True, text_color)
    #     text_rect = text_surf.get_rect(center=image_center)
    #     # Blit the text onto the images.
    #     for image in (self.image_normal, self.image_hover, self.image_down):
    #         image.blit(text_surf, text_rect)

    #     # This function will be called when the button gets pressed.
    #     self.callback = callback
    # #     self.button_down = False

    # def handle_event(self, event):
    #     if event.type == pg.MOUSEBUTTONDOWN:
    #         if self.rect.collidepoint(event.pos):
    #             self.image = self.image_down
    #             self.button_down = True
    #     elif event.type == pg.MOUSEBUTTONUP:
    #         # If the rect collides with the mouse pos.
    #         if self.rect.collidepoint(event.pos) and self.button_down:
    #             self.callback()  # Call the function.
    #             self.image = self.image_hover
    #         self.button_down = False
    #     elif event.type == pg.MOUSEMOTION:
    #         collided = self.rect.collidepoint(event.pos)
    #         if collided and not self.button_down:
    #             self.image = self.image_hover
    #         elif not collided:
    #             self.image = self.image_normal


class Game:
    def __init__(self, ai_game):
        self.settings = Settings()

        self.done = False
        self.clock = pg.time.Clock()
        self.screen = screen
        self.sw = self.settings.screen_width
 
        # Contains all sprites. Also put the button sprites into a
        # separate group in your own game.
        self.all_sprites = pg.sprite.Group()
        alphabet = list(string.ascii_uppercase) # Getting all the letters in the latin alphabet

        letters = []
        j = 0   # TO ALIGN THE LETTERS ON THE SCREEN ( VERTICALLY )
        for number, letter in enumerate(alphabet):
            if number > 12: # TO ALIGN THE LETTERS ON THE SCREEN ( HORIZONTALLY )
                number = number - 13
                j = 1
            letters.append(Button(colors["gray"], (70+number*90,440+j*20), 50, 50, letter))
        # self.number = 0
        # # Create the button instances. You can pass your own images here.
        # self.start_button = Button(
        #     320, 70, 30, 30, self.increment_number,
        #     FONT, 'A', (255, 255, 255),
        #     IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # # If you don't pass images, the default images will be used.
        # self.quit_button = Button(
        #     320, 240, 30, 30, self.quit_game,
        #     FONT, 'B', (255, 255, 255))
        # # Add the button sprites to the sprite group.
            self.all_sprites.add(letters)

    def quit_game(self):
        """Callback method to quit the game."""
        self.done = True

    def increment_number(self):
        """Callback method to increment the number."""
        self.number += 1
        print(self.number)

    def run(self):
        while not self.done:
            self.dt = self.clock.tick(30) / 1000
            self.handle_events()
            self.run_logic()
            self.draw()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            # for button in self.all_sprites:
            #     button.handle_event(event)

    def run_logic(self):
        self.all_sprites.update(self.dt)

    def draw(self):
        self.all_sprites.draw(self.screen)
        pg.display.flip()

            # def alphabet(self):
    #     self.letters = []
    #     self.align = 0
    #     self.alphabet = list(string.ascii_uppercase) # Getting all the letters in the latin alphabet
    #     for self.number, self.letter in enumerate(self.alphabet):
    #         if self.number > 12:
    #             self.number = self.number - 13
    #             self.align = 1
    #             print(self.number)
    #         self.letters.append(Button(320, 70, 30, 30, self.increment_number, FONT, self.letter, (255,255,255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN))
    #     print(self.letters)


if __name__ == '__main__':
    pg.init()
    Game(screen).run()
    pg.quit()