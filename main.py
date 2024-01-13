import pygame
import sys
import tutorial

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

# ------------- BOOLS -------------
pygame.font.init()
# ------------- TEXT BUTTONS -------------
font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)

start_text = font.render("Start", True, text_color)
start_rect = start_text.get_rect(center=(width // 2, height - 50))  

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((width, height))
        self.gameStateManager = GameStateManager('menu')
        self.window.fill((0, 0, 0))

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
    def run(self):
        self.display.fill('blue')
        pygame.display.update()

class Tutorial:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.shoot_anim = tutorial.tutorial_animations(tutorial_shoot)
        self.shield_anim = tutorial.tutorial_animations(tutorial_shield)
        self.reload_anim = tutorial.tutorial_animations(tutorial_reload)
        self.shoot_anim.start()
        self.shield_anim.start()
        self.reload_anim.start()
        
    def run(self):
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