import pygame
import random
pygame.init()

class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.health = 100
        self.max_health = 100

        self.attack_points = 0.3

        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 300 + random.randint(0, 300)
        self.rect.y = 240

        self.velocity = 3

    def damage(self, points):
        self.health -= points
        if self.health <= 0:
            # faire re-apparaître
            self.rect.x = 300 + random.randint(0, 300)
            self.health = 100

    def update_health_bar(self, surface):
        bar_color = (111, 210, 46)
        back_bar_color = (60, 63, 60)

        bar_position = [self.rect.x+10 , self.rect.y-20, self.health, 3] #[x, y, w, h]
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]  # [x, y, w, h]

        #dessin
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)


    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack_points)