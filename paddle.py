import pygame
black = (0, 0, 0)


class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        # Calling the parent class (pygame.Sprite) constructor
        super().__init__()

        # Surface to draw on (X and Y pos)
        self.image = pygame.Surface([width, height])
        # Making sprites' background transparent
        self.image.fill(black)
        self.image.set_colorkey(black)

        # Drawing paddle itself
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Returns a hitbox (x, y)
        self.rect = self.image.get_rect()

    def move_up(self, pixels):
        if self.rect.y > pixels:
            self.rect.y -= pixels

    def move_down(self, pixels, y_res):
        if self.rect.y < y_res - pixels - 100:  # Checking for out-of-bounds
            self.rect.y += pixels
