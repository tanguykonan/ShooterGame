import pygame
from poo.game import Game
pygame.init()

"""Class de gestion de la fenêtre de notre jeu"""
class Window(Game):
    def __init__(self):
        Game.__init__(self)
        pygame.display.set_caption("Shooter Game")
        self.screen_size = (620, 380)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.background = pygame.image.load("assets/bg.jpg")
        self.running = True
        self.game = Game()

    def show(self):
        while self.running:

            self.screen.blit(self.background, (-100, -500))
            self.screen.blit(self.game.player.image, (self.game.player.rect.x, self.game.player.rect.y))

            """Recuperation de toutes les attacks dans le panier du joueur"""
            for attack in self.game.player.all_projectile:
                attack.switch()
            """Afficher les attacks du joueur"""
            self.game.player.all_projectile.draw(self.screen)


            """Récupérer les monstres du joueur"""
            for monster in self.game.all_monsters:
                monster.forward()
            """Affiche les images du groupe de monstre"""
            self.game.all_monsters.draw(self.screen)


            """Vérification de la position voulue par le joueur"""
            left_possible = self.game.player.rect.x > 0
            right_possible = self.game.player.rect.x + self.game.player.rect.width < self.screen.get_width()

            if self.game.pressed_keys.get(pygame.K_LEFT) and left_possible:
                self.game.player.move_left()
            elif self.game.pressed_keys.get(pygame.K_RIGHT) and right_possible:
                self.game.player.move_right()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

                elif event.type == pygame.KEYDOWN:
                    """Activation des touches du clavier"""
                    self.game.pressed_keys[event.key] = True

                    # Détecter si la touche de tire appéllée
                    if event.key == pygame.K_SPACE:
                        self.game.player.launch_attack()

                    elif event.key == pygame.K_UP:
                        self.game.player.move_up()

                elif event.type == pygame.KEYUP:
                    """Désactivation des touches du clavier"""
                    self.game.pressed_keys[event.key] = False


app = Window()
app.show()