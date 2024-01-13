import pygame
import tutorial
import ai
import hands

pygame.init()

# ------------- SPRITES -------------
shoot_sprite = [pygame.image.load("sprites/computer/shoot1.png"),
                pygame.image.load("sprites/computer/shoot2.png"),
                pygame.image.load("sprites/computer/shoot3.png"),
                pygame.image.load("sprites/computer/shoot1.png")]
reload_sprite = [pygame.image.load("sprites/computer/reload1.png"),
                pygame.image.load("sprites/computer/reload2.png"),
                pygame.image.load("sprites/computer/reload1.png")]
shield_sprite = [pygame.image.load("sprites/computer/shield.png")]

tutorial_shoot = [pygame.image.load("sprites/tutorial/tutorial_s1.png"),
              pygame.image.load("sprites/tutorial/tutorial_s2.png"),
              pygame.image.load("sprites/tutorial/tutorial_s3.png"),
              pygame.image.load("sprites/tutorial/tutorial_s1.png")]
tutorial_shield = [pygame.image.load("sprites/tutorial/tutorial_sh.png")]
tutorial_reload = [pygame.image.load("sprites/tutorial/tutorial_r1.png"),
              pygame.image.load("sprites/tutorial/tutorial_r2.png"),
              pygame.image.load("sprites/tutorial/tutorial_r1.png")]

# ------------- SCENE -------------
width = 1000
height = 800
main_scene = pygame.display.set_mode((width, height))
main_scene.fill((0, 0, 0))
clock = pygame.time.Clock()

# ------------- BOOLS -------------
running = True
tut_run = False
# ------------- TEXT BUTTONS -------------
font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)

start_text = font.render("Start", True, text_color)
start_rect = start_text.get_rect(center=(width // 2, height - 50))
main_scene.blit(start_text, start_rect)
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(event.pos):
                tut_run = True
                main_scene.fill((0, 0, 0))
                pygame.display.update()
                shoot_anim = tutorial.tutorial_animations(tutorial_shoot)
                shield_anim = tutorial.tutorial_animations(tutorial_shield)
                reload_anim = tutorial.tutorial_animations(tutorial_reload)
                shoot_anim.start()
                shield_anim.start()
                reload_anim.start()
        if event.type == pygame.QUIT:
                running = False
            
    if tut_run:
        shoot_anim.update(clock.tick(60) / 1000.0)
        shield_anim.update(clock.tick(60) / 1000.0)
        reload_anim.update(clock.tick(60) / 1000.0)

        main_scene.blit(shoot_anim.current_frame, (300, 50))
        main_scene.blit(shield_anim.current_frame, (200, 50))
        main_scene.blit(reload_anim.current_frame, (100, 50))
        pygame.display.update()
        main_scene.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    tut_run = False
            if event.type == pygame.QUIT:
                running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    