import pygame
from colorama import  Fore, Style
from poo.projectile import Projectile
pygame.init()

"""Class qui représente notre joueur (Et ses capacités)"""
class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.health = 100
        self.max_health = 100

        self.attack = 50
        self.speed = 1
        self.jump = 100
        self.all_projectile = pygame.sprite.Group()

        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 90 # position gauche/droite (gauche:Min --> droite:Max)
        self.rect.y = 200  # position haut/bas (Bas:Min --> Haut:Max)

    def move_left(self):
        self.rect.x -= self.speed
        print(Fore.BLUE + '[]-> Déplacement du joueur vers la gauche' + Style.RESET_ALL)

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.speed
            print(Fore.YELLOW + '[]-> Déplacement du joueur vers la droite' + Style.RESET_ALL)

    def move_up(self):
        self.rect.y -= self.jump
        print(Fore.CYAN + '[]-> Saut du joueur' + Style.RESET_ALL)

    def launch_attack(self):
        self.all_projectile.add(Projectile(self)) # type:ignore
        print(Fore.RED + f'[]-> Attack lancé' + Style.RESET_ALL)

