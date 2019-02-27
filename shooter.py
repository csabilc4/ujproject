#!/usr/bin/env python
# coding=utf-8

#Import Modules
import os, pygame
from pygame.locals import *
from pygame.compat import geterror


main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir)

#functions to create our resources
def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print ('Cannot load image:', fullname)
        raise SystemExit(str(geterror()))
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


#classes for our game objects
class Weapon(pygame.sprite.Sprite):
    """moves a clenched fist on the screen, following the mouse"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image, self.rect = load_image('crosshair.png', -1)
        self.shooting = 0

    def update(self):
        "move the fist based on the mouse position"
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        if self.shooting:
            self.rect.move_ip(5, 5)

    def shoot(self, target):
        "returns true if the fist collides with the target"
        if not self.shooting:
            self.shooting = 1
            hitbox = self.rect.inflate(-2, -2)
            return hitbox.colliderect(target.rect)

    def unshoot(self):
        "called to pull the fist back"
        self.shooting = 0

class Target(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        self.image, self.rect = load_image('targetRed.png', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 0, 0
        self.speed = 1
        self.moveX = 5 * self.speed
        self.moveY = 2 * self.speed
        self.dizzy = 0
        self.colour = "red"


    def _walk(self):
        "move the monkey across the screen, and turn at the ends"
        newpos = self.rect.move((self.moveX, self.moveY))
        attachWall = False

        if self.rect.left < self.area.left or \
                self.rect.right > self.area.right:
            self.moveX = -self.moveX
            newpos = self.rect.move((self.moveX, self.moveY))
            attachWall = True

        if self.rect.top < self.area.top or \
                self.rect.bottom > self.area.bottom:
            self.moveY = -self.moveY
            newpos = self.rect.move((self.moveX, self.moveY))
            attachWall = True

        # if attachWall:
            # self.image = pygame.transform.flip(self.image, 1, 0)éűöüó
            # if self.colour == "red":
        if self.dizzy == 1:
            self.image, self.rect = load_image('targetBlue.png', -1)
            self.colour = "blue"
        else:
            self.image, self.rect = load_image('targetRed.png', -1)
            self.colour = "red"

        self.rect = newpos
        self.dizzy = 0


    def update(self):
        "walk or spin, depending on the monkeys state"
        self._walk()

    def shooted(self):
        "this will cause the monkey to start spinning"
        if not self.dizzy:
            self.dizzy = 1
            self.original = self.image


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Talált!')
    pygame.mouse.set_visible(0)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

# Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()

    clock = pygame.time.Clock()
    target = Target()
    crosshair = Weapon()
    allsprites = pygame.sprite.RenderPlain((crosshair, target))

# Main Loop
    going = True
    while going:
        clock.tick(60)

        #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                going = False
            elif event.type == MOUSEBUTTONDOWN:
                if crosshair.shoot(target):
                    # punch_sound.play() #shoot
                    target.shooted()
                else:
                    pass
                    # whiff_sound.play() #miss
            elif event.type == MOUSEBUTTONUP:
                crosshair.unshoot()

        allsprites.update()

        #Draw Everything
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()



