import pygame as pg
import string
import random
import sys
from settings import Settings

pg.init()
screen = pg.display.set_mode((800, 600))
FONT = pg.font.SysFont('Comic Sans MS', 32)
# Default button images/pygame.Surfaces.
IMAGE_NORMAL = pg.Surface((100, 32))
IMAGE_NORMAL.fill(pg.Color('dodgerblue1'))
IMAGE_HOVER = pg.Surface((100, 32))
IMAGE_HOVER.fill(pg.Color('lightskyblue'))
IMAGE_DOWN = pg.Surface((100, 32))
IMAGE_DOWN.fill(pg.Color('aquamarine1'))


# Button is a sprite subclass, that means it can be added to a sprite group.
# You can draw and update all sprites in a group by
# calling `group.update()` and `group.draw(screen)`.
class Button(pg.sprite.Sprite):
    def __init__(self, pos, width, height, callback, font=FONT, text='', text_color=(0, 0, 0), image_normal=IMAGE_NORMAL, image_hover=IMAGE_HOVER, image_down=IMAGE_DOWN):
        super().__init__()

        # Scale the images to the desired size (doesn't modify the originals).
        self.image_normal = pg.transform.scale(image_normal, (width, height))
        self.image_hover = pg.transform.scale(image_hover, (width, height))
        self.image_down = pg.transform.scale(image_down, (width, height))
        self.callback = callback
        self.button_down = False
        self.pos = pos
        self.image = self.image_normal  # The currently active image.
        self.rect = self.image.get_rect()
        # To center the text rect.
        self.image_center = self.image.get_rect().center
        self.text_surf = font.render(text, True, text_color)
        self.text_rect = self.text_surf.get_rect(center=self.image_center)
        # Blit the text onto the images.
        for self.image in (self.image_normal, self.image_hover, self.image_down):
            self.image.blit(self.text_surf, self.text_rect)

        # This function will be called when the button gets pressed.

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.image = self.image_down
                self.button_down = True
        elif event.type == pg.MOUSEBUTTONUP:
            # If the rect collides with the mouse pos.
            if self.rect.collidepoint(event.pos) and self.button_down:
                self.callback()  # Call the function.
                self.image = self.image_hover
            self.button_down = False
        elif event.type == pg.MOUSEMOTION:
            collided = self.rect.collidepoint(event.pos)
            if collided and not self.button_down:
                self.image = self.image_hover
            elif not collided:
                self.image = self.image_normal


class Game:
    def __init__(self, ai_game):
        # self.rect = self.Button.image.get_rect()
        self.done = False

        self.clock = pg.time.Clock()
        self.screen = screen
        self.settings = Settings()
        self.width = self.settings.screen_width
        # Contains all sprites. Also put the button sprites into a
        # separate group in your own game.
        self.all_sprites = pg.sprite.Group()


#############################################################################################################################
#############################################################################################################################
# THIS IS WHAT I HAVE BEEN TRYING

        # self.number = 0
        # button = Button(self)
        # available_space_x = self.width - (2 * button_width)
        # number_buttons_x = available_space_x // (2 * button_width)
        alphabet = list(string.ascii_uppercase) # Getting all the letters in the latin alphabet
        letters = []
        j = 0  # TO ALIGN THE LETTERS ON THE SCREEN ( VERTICALLY )
        for number, letter in enumerate(alphabet):
            if number > 12:  # TO ALIGN THE LETTERS ON THE SCREEN ( HORIZONTALLY )
                number = number - 13
                j = 1
            letters.append(Button((70+number*90, 40+j*90), 30, 30, self.increment_number, FONT, letter, (255,255,255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN))

            print(self.all_sprites)
                # self, x, y, width, height, callback,
                #  font=FONT, text='', text_color=(0, 0, 0),
                #  image_normal=IMAGE_NORMAL, image_hover=IMAGE_HOVER,
                #  image_down=IMAGE_DOWN):
            self.all_sprites.add(letters)
        print(self.all_sprites)
        print(letters)


#############################################################################################################################
#############################################################################################################################
# THIS IS WHAT IM TRYING TO AVOID

        # Create the button instances. You can pass your own images here.
        # self.a = Button(10, 70, 30, 30, self.increment_number, FONT, 'A', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # self.b = Button(60, 70, 30, 30, self.increment_number, FONT, 'B', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # self.c = Button(120, 70, 30, 30, self.increment_number, FONT, 'C', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # self.d = Button(180, 70, 30, 30, self.increment_number, FONT, 'D', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # self.e = Button(240, 70, 30, 30, self.increment_number, FONT, 'E', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # self.f = Button(300, 70, 30, 30, self.increment_number, FONT, 'F', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # self.g = Button(360, 70, 30, 30, self.increment_number, FONT, 'G', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # self.h = Button(420, 70, 30, 30, self.increment_number, FONT, 'H', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # self.i = Button(480, 70, 30, 30, self.increment_number, FONT, 'I', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # self.j = Button(540, 70, 30, 30, self.increment_number, FONT, 'J', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # self.k = Button(600, 70, 30, 30, self.increment_number, FONT, 'K', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # self.l = Button(660, 70, 30, 30, self.increment_number, FONT, 'L', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # self.m = Button(720, 70, 30, 30, self.increment_number, FONT, 'M', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # # 13
        # self.n = Button(10, 120, 30, 30, self.increment_number, FONT, 'N', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # self.o = Button(60, 120, 30, 30, self.increment_number, FONT, 'O', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # self.p = Button(120, 120, 30, 30, self.increment_number, FONT, 'P', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # self.q = Button(180, 120, 30, 30, self.increment_number, FONT, 'Q', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # self.r = Button(240, 120, 30, 30, self.increment_number, FONT, 'R', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # self.s = Button(300, 120, 30, 30, self.increment_number, FONT, 'S', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # self.t = Button(360, 120, 30, 30, self.increment_number, FONT, 'T', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # self.u = Button(420, 120, 30, 30, self.increment_number, FONT, 'U', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # self.v = Button(480, 120, 30, 30, self.increment_number, FONT, 'V', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # self.w = Button(540, 120, 30, 30, self.increment_number, FONT, 'W', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # self.x = Button(600, 120, 30, 30, self.increment_number, FONT, 'X', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # self.y = Button(660, 120, 30, 30, self.increment_number, FONT, 'Y', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # self.z = Button(720, 120, 30, 30, self.increment_number, FONT, 'Z', (255, 255, 255), IMAGE_NORMAL, IMAGE_HOVER, IMAGE_DOWN)
        # Add the button sprites to the sprite group.
        # self.all_sprites.add(self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h, self.i, self.j, self.k, self.l, self.m, self.n, self.o, self.p, self.q, self.r, self.s, self.t, self.u, self.v, self.w, self.x, self.y, self.z)
        
# THIS IS WHAT IM TRYING TO AVOID
#############################################################################################################################
#############################################################################################################################
   
   
   
   
    def quit_game(self):
        """Callback method to quit the game."""
        self.done = True

    def increment_number(self):
        """Callback method to increment the number."""
        # self.number += 1
        print('fuckwit')
        # print(self.number)

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
            for button in self.all_sprites:
                button.handle_event(event)

    def run_logic(self):
        self.all_sprites.update(self.dt)

    def draw(self):
        self.all_sprites.draw(self.screen)
        pg.display.flip()



if __name__ == '__main__':
    pg.init()
    Game(screen).run()
    pg.quit()
