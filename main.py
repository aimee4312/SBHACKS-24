import pygame
import sys
import tutorial

pygame.init()

# background
background = pygame.image.load("assets/background/background.jpeg")

# ------------- SPRITES -------------
shoot_sprite = [pygame.image.load("assets/sprites/shoot1.png"),
                pygame.image.load("assets/sprites/shoot2.png"),
                pygame.image.load("assets/sprites/shoot3.png"),
                pygame.image.load("assets/sprites/shoot1.png")]
reload_sprite = [pygame.image.load("assets/sprites/reload1.png"),
                pygame.image.load("assets/sprites/reload2.png"),
                pygame.image.load("assets/sprites/reload1.png")]
shield_sprite = [pygame.image.load("assets/sprites/shield.png")]

tutorial_shoot = [pygame.image.load("assets/sprites/tutorial/tutorial_s1.png"),
              pygame.image.load("assets/sprites/tutorial/tutorial_s2.png"),
              pygame.image.load("assets/sprites/tutorial/tutorial_s3.png"),
              pygame.image.load("assets/sprites/tutorial/tutorial_s1.png")]
tutorial_shield = [pygame.image.load("assets/sprites/tutorial/tutorial_sh.png")]
tutorial_reload = [pygame.image.load("assets/sprites/tutorial/tutorial_r1.png"),
              pygame.image.load("assets/sprites/tutorial/tutorial_r2.png"),
              pygame.image.load("assets/sprites/tutorial/tutorial_r1.png")]

# ------------- SCENE -------------
width = 1000
height = 800
clock = pygame.time.Clock()
wins = 0
losses = 0
# ------------- BOOLS -------------

# ------------- TEXT BUTTONS -------------
font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)

start_text = font.render("Start", True, text_color)
start_rect = start_text.get_rect(center=(width // 2, height - 50)) 

# menu text
menu_font = pygame.font.Font('freesansbold.ttf', 84)
menu_text = menu_font.render("Welcome to ShootOut", True, (222, 169, 169))
menu_text_outline = menu_font.render("Welcome to ShootOut", True, (0, 0, 0))
menu_x = 60
menu_y = 200
help_font = pygame.font.Font('freesansbold.ttf', 36)
help_text = help_font.render("Raise your open hand for the tutorial", True, (255, 255, 255))
help_text_outline = help_font.render("Raise your open hand for the tutorial", True, (0, 0, 0))
help_x = 150
help_y = 600
start_font = pygame.font.Font('freesansbold.ttf', 36)
start_text = start_font.render("Give a thumbs up to start the game", True, (222, 169, 169))
start_text_outline = start_font.render("Give a thumbs up to start the game", True, (0, 0, 0))
start_x = 160
start_y = 650

# score text
score_font = pygame.font.Font('freesansbold.ttf', 36)
wins_text = score_font.render("Wins: " + str(wins), True, (255, 255, 255))
wins_text_outline = score_font.render("Wins: " + str(wins), True, (0, 0, 0))
wins_x = 20
wins_y = 20
losses_text = score_font.render("Losses: " + str(wins), True, (255, 255, 255))
losses_text_outline = score_font.render("Losses: " + str(wins), True, (0, 0, 0))
losses_x = 850
losses_y = 20


class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("ShootOut", "ShootOut")
        self.background = pygame.image.load("assets/background/background.jpeg")
        self.gameStateManager = GameStateManager('menu')
        self.window.fill((0, 0, 0))
        self.window.blit(background, (0, 0))

        self.window.blit(start_text, start_rect)
        self.menu = Menu(self.window, self.gameStateManager)
        self.tutorial = Tutorial(self.window, self.gameStateManager)

        self.states = {'menu': self.menu, 'tutorial': self.tutorial}
        pygame.display.update()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        tut_run = True
                        self.window.fill((0, 0, 0))
                        pygame.display.update()
                        self.gameStateManager.set_state('tutorial')
                        self.tutorial = Tutorial(self.window, self.gameStateManager)

            self.states[self.gameStateManager.get_state()].run()
            


    
class Menu:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.display.blit(background, (0, 0))
        self.display.blit(menu_text_outline, (menu_x-2, menu_y-2))
        self.display.blit(menu_text_outline, (menu_x-2, menu_y))
        self.display.blit(menu_text_outline, (menu_x, menu_y-2))
        self.display.blit(menu_text_outline, (menu_x, menu_y+2))
        self.display.blit(menu_text_outline, (menu_x+2, menu_y))
        self.display.blit(menu_text_outline, (menu_x+2, menu_y+2))
        self.display.blit(menu_text, (menu_x, menu_y))

        self.display.blit(help_text_outline, (help_x-2, help_y-2))
        self.display.blit(help_text_outline, (help_x-2, help_y))
        self.display.blit(help_text_outline, (help_x, help_y-2))
        self.display.blit(help_text_outline, (help_x, help_y+2))
        self.display.blit(help_text_outline, (help_x+2, help_y))
        self.display.blit(help_text_outline, (help_x+2, help_y+2))
        self.display.blit(help_text, (help_x, help_y))

        self.display.blit(start_text_outline, (start_x-2, start_y-2))
        self.display.blit(start_text_outline, (start_x-2, start_y))
        self.display.blit(start_text_outline, (start_x, start_y-2))
        self.display.blit(start_text_outline, (start_x, start_y+2))
        self.display.blit(start_text_outline, (start_x+2, start_y))
        self.display.blit(start_text_outline, (start_x+2, start_y+2))
        self.display.blit(start_text, (start_x, start_y))
        pygame.display.update()
    def run(self):
        pygame.display.update()

class Tutorial:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.display.blit(background, (0, 0))
        self.shoot_anim = tutorial.tutorial_animations(tutorial_shoot)
        self.shield_anim = tutorial.tutorial_animations(tutorial_shield)
        self.reload_anim = tutorial.tutorial_animations(tutorial_reload)
        self.shoot_anim.start()
        self.shield_anim.start()
        self.reload_anim.start()
        
    def run(self):
        self.display.blit(background, (0, 0))
        shoot_text = font.render("Tutorial", True, text_color)
        shoot_rect = start_text.get_rect(center=(width - 530 , height - 750))
        self.display.blit(shoot_text, shoot_rect)

        shoot_text = font.render("Shoot", True, text_color)
        shoot_rect = start_text.get_rect(center=(width - 305, height - 650))
        self.display.blit(shoot_text, shoot_rect)

        shield_text = font.render("Shield", True, text_color)
        shield_rect = shield_text.get_rect(center=(width - 525, height - 400))
        self.display.blit(shield_text, shield_rect)

        reload_text = font.render("Reload", True, text_color)
        reload_rect = reload_text.get_rect(center=(width - 750, height - 650))
        self.display.blit(reload_text, reload_rect)
        self.shoot_anim.update(clock.tick(60) / 1000.0)
        self.shield_anim.update(clock.tick(60) / 1000.0)
        self.reload_anim.update(clock.tick(60) / 1000.0)

        self.display.blit(self.shoot_anim.current_frame, (300, 50))
        self.display.blit(self.shield_anim.current_frame, (200, 50))
        self.display.blit(self.reload_anim.current_frame, (100, 50))
        pygame.display.update()
        self.display.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m: #m for menu
                    self.gameStateManager.set_state('menu')
                    self.menu = Menu(self.display, self.gameStateManager)
            if event.type == pygame.QUIT:
                running = False

class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState
    def get_state(self):
        return self.currentState
    def set_state(self, state):
        self.currentState = state

if __name__ == '__main__':
    game = Game()
    game.run()