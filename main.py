import pygame
import math
from poo.game import Game
pygame.init()

"""Class de gestion de la fenêtre de notre jeu"""
class Window(Game):
    def __init__(self):
        Game.__init__(self)
        pygame.display.set_caption("Shooter Game")
        self.screen_size = (720, 380)
        self.screen = pygame.display.set_mode(self.screen_size)

        self.background = pygame.image.load("assets/bg.jpg")

        self.banner = pygame.image.load("assets/banner.png")
        self.banner = pygame.transform.scale(self.banner, (300, 300))
        self.banner_rect = self.banner.get_rect()
        self.banner_rect.x = math.ceil(self.screen.get_width() / 4)

        self.play_button = pygame.image.load("assets/button.png")
        self.play_button = pygame.transform.scale(self.play_button, (200, 100))
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x = math.ceil(self.screen.get_width() / 3)
        self.play_button_rect.y = math.ceil(self.screen.get_height() / 1.8)

        self.running = True
        self.game = Game()
        self.clock = pygame.time.Clock()
        self.FPS = 60

    def show(self):
        while self.running:

            self.screen.blit(self.background, (-100, -500))

            #verify
            if self.game.is_playing:
                self.game.update(self.screen)
            else:
                self.screen.blit(self.play_button, self.play_button_rect)
                self.screen.blit(self.banner, self.banner_rect)
            self.clock.tick(self.FPS)

            pygame.display.flip()
            self.clock.tick(self.FPS)

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

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button_rect.collidepoint(event.pos):
                        self.game.is_playing = True
                        self.game.start()


app = Window()
app.show()