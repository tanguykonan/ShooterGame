import pygame
pygame.init()

class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.health = 100
        self.max_health = 100

        self.attack_points = 10

        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 550
        self.rect.y = 240

        self.velocity = 1
    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity