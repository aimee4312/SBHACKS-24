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

# ------------- SCENE MANAGEMENT-------------
main_scene_info = pygame.display.Info()
display_width = main_scene_info.current_w
display_height = main_scene_info.current_h

main_scene_WIDTH = display_width
main_scene_HEIGHT = display_height
main_scene = pygame.display.set_mode((main_scene_WIDTH, main_scene_HEIGHT))
background = pygame.image.load("assets/background/background.jpeg")
pygame.display.set_caption("ShootOut", "ShootOut")
background = pygame.image.load("assets/background/background.jpeg")
background = pygame.transform.scale(background, (main_scene_WIDTH, main_scene_HEIGHT))
main_scene.blit(background, (0, 0))
clock = pygame.time.Clock()

# ------------- STATES -------------
running = True
tutorial_state = False
menu_state = True
tutorial_state = False
game_state = False
game_over_state = False
wins = 0
losses = 0
# ------------- TEXT PLACEMENT -------------
# Tutorial
font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)
temp_start_text_percentage_x = 0.5
temp_start_text_percentage_y = 0.8 
temp_start_text_x = int(display_width * temp_start_text_percentage_x)
temp_start_text_y = int(display_height * temp_start_text_percentage_y)

tutorial_text_percentage_x = 0.5
tutorial_text_percentage_y = 0.1 
tutorial_text_x = int(display_width * tutorial_text_percentage_x)
tutorial_text_y = int(display_height * tutorial_text_percentage_y)

instruction_text_percentage_x = 0.4
instruction_text_percentage_y = 0.6 
instruction_text_x = int(display_width * instruction_text_percentage_x)
instruction_text_y = int(display_height * instruction_text_percentage_y)

instruction_lines = [
    "Shoot: Attempt to shoot the opponent",
    "Shield: Protect yourself from an opponent's shot",
    "Reload: Prepare the shotgun for the next shot"
]

outcome_lines = [
    "1. If both players choose to reload,",
    "   nothing happens; both players reload",
    "   2. If one player chooses to reload and the other chooses",
    "   to shoot, the shot player loses a shield",
    "3. If one player chooses to shield and the other ",
    "   chooses to shoot, the shooting player's shot is blocked",
    "4. If both players choose to shield,",
    "   nothing happens; both players are protected"
]

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

temp_start_text = font.render("Start", True, text_color)
temp_start_rect = temp_start_text.get_rect(center=(temp_start_text_x, temp_start_text_y))
main_scene.blit(temp_start_text, temp_start_rect)
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

# MENU
menu_font = pygame.font.Font('freesansbold.ttf', 84)
menu_text = menu_font.render("Welcome to ShootOut", True, (222, 169, 169))
menu_text_outline = menu_font.render("Welcome to ShootOut", True, (0, 0, 0))
menu_text_percentage_x = 0.2
menu_text_percentage_y = 0.3 
menu_text_x = int(display_width * menu_text_percentage_x)
menu_text_y = int(display_height * menu_text_percentage_y)

help_font = pygame.font.Font('freesansbold.ttf', 36)
help_text = help_font.render("Raise your open hand for the tutorial", True, (255, 255, 255))
help_text_outline = help_font.render("Raise your open hand for the tutorial", True, (0, 0, 0))
help_text_percentage_x = 0.3
help_text_percentage_y = 0.45 
help_text_x = int(display_width * help_text_percentage_x)
help_text_y = int(display_height * help_text_percentage_y)

start_font = pygame.font.Font('freesansbold.ttf', 36)
start_text = start_font.render("Give a thumbs up to start the game", True, (222, 169, 169))
start_text_outline = start_font.render("Give a thumbs up to start the game", True, (0, 0, 0))
start_text_percentage_x = 0.3
start_text_percentage_y = 0.5 
start_text_x = int(display_width * start_text_percentage_x)
start_text_y = int(display_height * start_text_percentage_y)

# SCORE
score_font = pygame.font.Font('freesansbold.ttf', 36)
wins_text = score_font.render("Wins: " + str(wins), True, (255, 255, 255))
wins_text_outline = score_font.render("Wins: " + str(wins), True, (0, 0, 0))
wins_x = 20
wins_y = 20
losses_text = score_font.render("Losses: " + str(wins), True, (255, 255, 255))
losses_text_outline = score_font.render("Losses: " + str(wins), True, (0, 0, 0))
losses_x = 850
losses_y = 20

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
            if temp_start_rect.collidepoint(event.pos):
                tutorial_state = True
                menu_state = False
                main_scene.fill((0, 0, 0))
                pygame.display.update()
                shoot_anim, shield_anim, reload_anim = start_tutorial()
        if event.type == pygame.QUIT:
                running = False

    if menu_state:
        main_scene.blit(menu_text_outline, (menu_text_x - 2, menu_text_y - 2))
        main_scene.blit(menu_text_outline, (menu_text_x - 2, menu_text_y))
        main_scene.blit(menu_text_outline, (menu_text_x, menu_text_y - 2))
        main_scene.blit(menu_text_outline, (menu_text_x, menu_text_y + 2))
        main_scene.blit(menu_text_outline, (menu_text_x + 2, menu_text_y))
        main_scene.blit(menu_text_outline, (menu_text_x + 2, menu_text_y + 2))
        main_scene.blit(menu_text, (menu_text_x, menu_text_y))

        main_scene.blit(help_text_outline, (help_text_x - 2, help_text_y - 2))
        main_scene.blit(help_text_outline, (help_text_x - 2, help_text_y))
        main_scene.blit(help_text_outline, (help_text_x, help_text_y - 2))
        main_scene.blit(help_text_outline, (help_text_x, help_text_y + 2))
        main_scene.blit(help_text_outline, (help_text_x + 2, help_text_y))
        main_scene.blit(help_text_outline, (help_text_x + 2, help_text_y + 2))
        main_scene.blit(help_text, (help_text_x, help_text_y))

        main_scene.blit(start_text_outline, (start_text_x - 2, start_text_y - 2))
        main_scene.blit(start_text_outline, (start_text_x - 2, start_text_y))
        main_scene.blit(start_text_outline, (start_text_x, start_text_y - 2))
        main_scene.blit(start_text_outline, (start_text_x, start_text_y + 2))
        main_scene.blit(start_text_outline, (start_text_x + 2, start_text_y))
        main_scene.blit(start_text_outline, (start_text_x + 2, start_text_y + 2))
        main_scene.blit(start_text, (start_text_x, start_text_y))
        pygame.display.update()
          
    if tutorial_state:
        tutorial_text = font.render("Tutorial", True, text_color)
        tutorial_rect = tutorial_text.get_rect(center=(tutorial_text_x, tutorial_text_y))
        main_scene.blit(tutorial_text, tutorial_rect)

        shoot_text = font.render("Shoot", True, text_color)
        shoot_rect = shoot_text.get_rect(center=(shoot_text_x, shoot_text_y))
        main_scene.blit(shoot_text, shoot_rect)

        shield_text = font.render("Shield", True, text_color)
        shield_rect = shield_text.get_rect(center=(shield_text_x, shield_text_y))
        main_scene.blit(shield_text, shield_rect)

        reload_text = font.render("Reload", True, text_color)
        reload_rect = reload_text.get_rect(center=(reload_text_x, reload_text_y))
        main_scene.blit(reload_text, reload_rect)

        instruction_text = font.render("You have 3 possible actions:", True, text_color)
        instruction_rect = instruction_text.get_rect(center=(instruction_text_x * 0.6, instruction_text_y * 0.75))
        main_scene.blit(instruction_text, instruction_rect)

        instruction_y_offset = 5
        for line in instruction_lines:
            outcome_text = font.render(line, True, text_color)
            outcome_rect = outcome_text.get_rect(center=(instruction_text_x * 0.6, instruction_text_y * 0.8 + instruction_y_offset))
            main_scene.blit(outcome_text, outcome_rect)
            instruction_y_offset += outcome_rect.height

        outcome_text = font.render("Outcomes:", True, text_color)
        outcome_rect = outcome_text.get_rect(center=(instruction_text_x * 1.8, instruction_text_y * 0.75))
        main_scene.blit(outcome_text, outcome_rect)

        outcome_y_offset = 1
        for line in outcome_lines:
            outcome_text = font.render(line, True, text_color)
            outcome_rect = outcome_text.get_rect(center=(instruction_text_x * 1.8, instruction_text_y * 0.8 + outcome_y_offset))
            main_scene.blit(outcome_text, outcome_rect)
            outcome_y_offset += outcome_rect.height

        win_text = font.render("Last one alive wins!", True, text_color)
        win_rect = win_text.get_rect(center=(instruction_text_x * 1.25, instruction_text_y * 1.3))
        main_scene.blit(win_text, win_rect)
        
        update_tutorial(shoot_anim, shield_anim, reload_anim)
        main_scene.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    tutorial_state = False
                    menu_state = True
                    main_scene.blit(background, (0, 0))
                    main_scene.blit(temp_start_text, temp_start_rect)
            if event.type == pygame.QUIT:
                running = False

    if game_state:
        main_scene.blit(wins_text_outline, (wins_x - 2, wins_y - 2))
        main_scene.blit(wins_text_outline, (wins_x - 2, wins_y))
        main_scene.blit(wins_text_outline, (wins_x, wins_y - 2))
        main_scene.blit(wins_text_outline, (wins_x, wins_y + 2))
        main_scene.blit(wins_text_outline, (wins_x + 2, wins_y))
        main_scene.blit(wins_text_outline, (wins_x + 2, wins_y + 2))
        main_scene.blit(wins_text, (wins_x, wins_y))

        main_scene.blit(losses_text_outline, (losses_x - 2, losses_y - 2))
        main_scene.blit(losses_text_outline, (losses_x - 2, losses_y))
        main_scene.blit(losses_text_outline, (losses_x, losses_y - 2))
        main_scene.blit(losses_text_outline, (losses_x, losses_y + 2))
        main_scene.blit(losses_text_outline, (losses_x + 2, losses_y))
        main_scene.blit(losses_text_outline, (losses_x + 2, losses_y + 2))
        main_scene.blit(losses_text, (losses_x, losses_y))
        pygame.display.update()