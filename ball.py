import pygame
from random import randint, choice
black = (255, 0, 0)


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, center, radius):
        # Calling the parent class (pygame.Sprite) constructor
        super().__init__()

        # Surface to draw on (X and Y pos)
        self.image = pygame.Surface((2*radius, 2*radius))
        self.image.fill(black)
        self.image.set_colorkey(black)

        # Drawing a ball
        pygame.draw.circle(self.image, color, (radius, radius), radius)

        # Randomise ball velocity
        self.velocity = [choice((-1, 1)) * randint(4, 5), randint(-6, 6)]

        # Bool for collisions with paddles (BUG FIX)
        self.isBouncing = False

        # Returns a rectangle covering ball's sprite, also puts it in center
        self.rect = self.image.get_rect(center=(center[0], center[1]))

    def bounce(self):  # Bouncing of paddles
        if self.velocity[0] > 0:
            self.velocity[0] = randint(-8, -5)
        else:
            self.velocity[0] = randint(5, 8)
        self.velocity[1] = randint(-6, 6)

    def replay(self, center):  # Re-throws a ball
        self.rect.x = center[0]
        self.rect.y = center[1]
        self.velocity = [choice((-1, 1)) * randint(4, 5), randint(-6, 6)]

    def run(self):  # Ball motion-loop
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
