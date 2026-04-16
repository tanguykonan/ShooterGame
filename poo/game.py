import pygame

from poo.player import Player
from poo.monster import Monster

"""Class qui représente notre jeux (Génère le joueur et +)"""
class Game(Player, Monster):
    def __init__(self):

        # Déclencheur du jeu
        self.is_playing = False

        Player.__init__(self, game=True)
        Monster.__init__(self, game=True)

        """Générer le joueur"""
        self.all_players = pygame.sprite.Group()
        self.player = Player(game=self)
        self.all_players.add(self.player) #type:ignore
        self.pressed_keys = {}

        """Groupe de montres"""
        self.all_monsters = pygame.sprite.Group()


    # ======================================================================================
    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()


    def game_over(self):
        self.all_monsters = pygame.sprite.Group() #ECrasser les monstres déjà présents
        self.player.health = self.player.max_health
        self.is_playing = False

    # ======================================================================================

    def update(self, screen):

        screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
        self.player.update_health_bar(screen)

        """Recuperation de toutes les attacks dans le panier du joueur"""
        for attack in self.player.all_projectile:
            attack.switch()
        """Afficher les attacks du joueur"""
        self.player.all_projectile.draw(screen)

        """Récupérer les monstres du joueur"""
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
        """Affiche les images du groupe de monstre"""
        self.all_monsters.draw(screen)

        """Vérification de la position voulue par le joueur"""
        left_possible = self.player.rect.x > 0
        right_possible = self.player.rect.x + self.player.rect.width < screen.get_width()

        if self.pressed_keys.get(pygame.K_LEFT) and left_possible:
            self.player.move_left()
        elif self.pressed_keys.get(pygame.K_RIGHT) and right_possible:
            self.player.move_right()

    #======================================================================================
    #======================================================================================
    @staticmethod
    def check_collision(sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask) # type:ignore

    def spawn_monster(self):
        monster = Monster(game=self)
        self.all_monsters.add(monster) #type:ignore
