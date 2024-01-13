import pygame
import tutorial
import computer
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
screen_info = pygame.display.Info()
display_width = screen_info.current_w
display_height = screen_info.current_h

SCREEN_WIDTH = display_width
SCREEN_HEIGHT = display_height
main_scene = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
main_scene.fill((0, 0, 0))
clock = pygame.time.Clock()

# ------------- BOOLS -------------
running = True
tutorial_state = False
# ------------- TEXT BUTTONS -------------
font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)
start_text_percentage_x = 0.5
start_text_percentage_y = 0.8 
start_text_x = int(display_width * start_text_percentage_x)
start_text_y = int(display_height * start_text_percentage_y)

tutorial_text_percentage_x = 0.485
tutorial_text_percentage_y = 0.1 
tutorial_text_x = int(display_width * tutorial_text_percentage_x)
tutorial_text_y = int(display_height * tutorial_text_percentage_y)

shoot_text_percentage_x = 0.2
shoot_text_percentage_y = 0.2 
shoot_text_x = int(display_width * shoot_text_percentage_x)
shoot_text_y = int(display_height * shoot_text_percentage_y)

shield_text_percentage_x = 0.5
shield_text_percentage_y = 0.2 
shield_text_x = int(display_width * shield_text_percentage_x)
shield_text_y = int(display_height * shield_text_percentage_y)

reload_text_percentage_x = 0.8
reload_text_percentage_y = 0.2 
reload_text_x = int(display_width * reload_text_percentage_x)
reload_text_y = int(display_height * reload_text_percentage_y)

start_text = font.render("Start", True, text_color)
start_rect = start_text.get_rect(center=(start_text_x, start_text_y))
main_scene.blit(start_text, start_rect)
pygame.display.update()

shoot_anim_percentage_x = -0.073
shoot_anim_percentage_y = 0.1 
shoot_anim_x = int(display_width * shoot_anim_percentage_x)
shoot_anim_y = int(display_height * shoot_anim_percentage_y)

shield_anim_percentage_x = 0.32
shield_anim_percentage_y = -0.15
shield_anim_x = int(display_width * shield_anim_percentage_x)
shield_anim_y = int(display_height * shield_anim_percentage_y)

reload_anim_percentage_x = 0.7
reload_anim_percentage_y = 0.1 
reload_anim_x = int(display_width * reload_anim_percentage_x)
reload_anim_y = int(display_height * reload_anim_percentage_y)

choices = {"shield": 2, "shoot": 0}

def start_tutorial():
    shoot_anim = tutorial.tutorial_animations(tutorial_shoot)
    shield_anim = tutorial.tutorial_animations(tutorial_shield)
    reload_anim = tutorial.tutorial_animations(tutorial_reload)
    shoot_anim.start()
    shield_anim.start()
    reload_anim.start()
    return shoot_anim, shield_anim, reload_anim

def update_tutorial(shoot_anim, shield_anim, reload_anim):
    shoot_anim.update(clock.tick(60) / 1000.0)
    shield_anim.update(clock.tick(60) / 1000.0)
    reload_anim.update(clock.tick(60) / 1000.0)

    main_scene.blit(shoot_anim.current_frame, (shoot_anim_x, shoot_anim_y))
    main_scene.blit(shield_anim.current_frame, (shield_anim_x, shield_anim_y))
    main_scene.blit(reload_anim.current_frame, (reload_anim_x, reload_anim_y))
    pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(event.pos):
                tutorial_state = True
                main_scene.fill((0, 0, 0))
                pygame.display.update()
                shoot_anim, shield_anim, reload_anim = start_tutorial()
        if event.type == pygame.QUIT:
                running = False
            
    if tutorial_state:
        shoot_text = font.render("Tutorial", True, text_color)
        shoot_rect = start_text.get_rect(center=(tutorial_text_x, tutorial_text_y))
        main_scene.blit(shoot_text, shoot_rect)

        shoot_text = font.render("Shoot", True, text_color)
        shoot_rect = start_text.get_rect(center=(shoot_text_x, shoot_text_y))
        main_scene.blit(shoot_text, shoot_rect)

        shield_text = font.render("Shield", True, text_color)
        shield_rect = shield_text.get_rect(center=(shield_text_x, shield_text_y))
        main_scene.blit(shield_text, shield_rect)

        reload_text = font.render("Reload", True, text_color)
        reload_rect = reload_text.get_rect(center=(reload_text_x, reload_text_y))
        main_scene.blit(reload_text, reload_rect)
        
        update_tutorial(shoot_anim, shield_anim, reload_anim)
        main_scene.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    tut_run = False
            if event.type == pygame.QUIT:
                running = False