import pygame
pygame.init()

"""Class de gestion des projectile du joueur"""
class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.velocity = 0.5
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.x = (self.player.rect.x + self.player.rect.width/2 + self.player.rect.height/2) - 60
        self.rect.y = self.player.rect.y + self.player.rect.height/2

        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 10
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectile.remove(self)

    def switch(self):
        self.rect.x += self.velocity
        self.rotate()

        if self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()

        if self.rect.x > 620:
            self.remove()


