import pygame

from poo.player import Player
from poo.monster import Monster

"""Class qui représente notre jeux (Génère le joueur et +)"""
class Game(Player, Monster):
    def __init__(self):
        Player.__init__(self, game=True)
        Monster.__init__(self, game=True)

        """Générer le joueur"""
        self.all_players = pygame.sprite.Group()
        self.player = Player(game=self)
        self.all_players.add(self.player) #type:ignore
        self.pressed_keys = {}

        """Groupe de montres"""
        self.all_monsters = pygame.sprite.Group()
        self.spawn_monster() # spawn à l'initialisation de la classe

    @staticmethod
    def check_collision(sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask) # type:ignore

    def spawn_monster(self):
        monster = Monster(game=self)
        self.all_monsters.add(monster) #type:ignore
