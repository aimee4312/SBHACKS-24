import pygame
import tutorial
import computer

import mediapipe as mp
import cv2
import numpy as np

# initializing hand recognition stuff in mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# initializing video capture w/ opencv
cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"FPS: {fps}")
frame_count = 0

# Gesture Recognizer options (what trains the model)
BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode

# saves GestureRecognizer results here
prev_result = None

# Create a gesture recognizer instance with the live stream mode:
def save_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    global prev_result
    prev_result = result

# # recognizer options.
# # model saved in model_asset_path
# # running mode is set to live stream
# # print_result saves the result
# options = GestureRecognizerOptions(
#     base_options=BaseOptions(model_asset_path='models/gesture_recognizer_readd_thumb.task'),
#     running_mode=VisionRunningMode.LIVE_STREAM,
#     result_callback=save_result)   

pygame.init()
pygame.mixer.init()
#pygame.mixer.music.load("/Users/aimeemai/Documents/GitHub/SBHACKS-24/assets/music/yeehawww.mp3")
pygame.mixer.music.load("assets/music/yeehawww.mp3")
pygame.mixer.music.play(-1)

# ------------- SPRITES -------------
# shoot_sprite = [pygame.image.load("/Users/aimeemai/Documents/GitHub/SBHACKS-24/sprites/computer/shoot1.png"),
#                  pygame.image.load("/Users/aimeemai/Documents/GitHub/SBHACKS-24/sprites/computer/shoot2.png"),
#                  pygame.image.load("/Users/aimeemai/Documents/GitHub/SBHACKS-24/sprites/computer/shoot3.png"),
#                  pygame.image.load("/Users/aimeemai/Documents/GitHub/SBHACKS-24/sprites/computer/shoot1.png")]
# reload_sprite = [pygame.image.load("/Users/aimeemai/Documents/GitHub/SBHACKS-24/sprites/computer/reload1.png"),
#                  pygame.image.load("/Users/aimeemai/Documents/GitHub/SBHACKS-24/sprites/computer/reload2.png"),
#                  pygame.image.load("/Users/aimeemai/Documents/GitHub/SBHACKS-24/sprites/computer/reload1.png")]
# shield_sprite = [pygame.image.load("/Users/aimeemai/Documents/GitHub/SBHACKS-24/sprites/computer/shield.png")]

# tutorial_shoot = [pygame.image.load("/Users/aimeemai/Documents/GitHub/SBHACKS-24/sprites/tutorial/tutorial_s1.png"),
#                pygame.image.load("/Users/aimeemai/Documents/GitHub/SBHACKS-24/sprites/tutorial/tutorial_s2.png"),
#                pygame.image.load("/Users/aimeemai/Documents/GitHub/SBHACKS-24/sprites/tutorial/tutorial_s3.png"),
#                pygame.image.load("/Users/aimeemai/Documents/GitHub/SBHACKS-24/sprites/tutorial/tutorial_s1.png")]
# tutorial_shield = [pygame.image.load("/Users/aimeemai/Documents/GitHub/SBHACKS-24/sprites/tutorial/tutorial_sh.png")]
# tutorial_reload = [pygame.image.load("/Users/aimeemai/Documents/GitHub/SBHACKS-24/sprites/tutorial/tutorial_r1.png"),
#                pygame.image.load("/Users/aimeemai/Documents/GitHub/SBHACKS-24/sprites/tutorial/tutorial_r2.png"),
#                pygame.image.load("/Users/aimeemai/Documents/GitHub/SBHACKS-24/sprites/tutorial/tutorial_r1.png")]
# icon = pygame.image.load("/Users/aimeemai/Documents/GitHub/SBHACKS-24/sprites/icon.png")
# idle = [pygame.image.load("/Users/aimeemai/Documents/GitHub/SBHACKS-24/sprites/computer/idle1.PNG"),
#          pygame.image.load("/Users/aimeemai/Documents/GitHub/SBHACKS-24/sprites/computer/idle2.png")]

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
icon = pygame.image.load("sprites/icon.png")
idle = [pygame.image.load("sprites/computer/idle1.PNG"),
        pygame.image.load("sprites/computer/idle2.png")]
shield_icon = pygame.image.load("sprites/shield_icon.png")
bullet_icon = pygame.image.load("sprites/bullet_icon.png")
bullet_icon_outline = pygame.image.load("sprites/bullet_icon_outline.png")

# ------------- SCENE MANAGEMENT-------------
main_scene_info = pygame.display.Info()
display_width = main_scene_info.current_w
display_height = main_scene_info.current_h

main_scene_WIDTH = display_width
main_scene_HEIGHT = display_height
main_scene = pygame.display.set_mode((main_scene_WIDTH, main_scene_HEIGHT))
#background = pygame.image.load("/Users/aimeemai/Documents/GitHub/SBHACKS-24/assets/background/background.jpeg")
background = pygame.image.load("assets/background/background.jpeg")
pygame.display.set_caption("ShootOut", "ShootOut")
background = pygame.transform.scale(background, (main_scene_WIDTH, main_scene_HEIGHT))
pygame.display.set_icon(icon)
main_scene.blit(background, (0, 0))
clock = pygame.time.Clock()

# ------------- STATES & VARIABLES-------------
running = True
tutorial_state = False
menu_state = True
tutorial_state = False
game_state = False
game_over_state = False
player_can_make_move = False
recent_result = 0
result_win = 1
result_lose = 2
result_tie = 3
wins = 0
losses = 0
bullets = 0
shields = 2

# ------------- GESTURE EVENTS -------------
POINT_ONE_GEST = pygame.USEREVENT + 1
STOP_GEST = pygame.USEREVENT + 2
SHOOT_GEST = pygame.USEREVENT + 3
THUMBS_DOWN_GEST = pygame.USEREVENT + 4

# ------------- TEXT PLACEMENT -------------
# Tutorial
font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)

tutorial_text_percentage_x = 0.5
tutorial_text_percentage_y = 0.1 
tutorial_text_x = int(display_width * tutorial_text_percentage_x)
tutorial_text_y = int(display_height * tutorial_text_percentage_y)

instruction_text_percentage_x = 0.4
instruction_text_percentage_y = 0.6 
instruction_text_x = int(display_width * instruction_text_percentage_x)
instruction_text_y = int(display_height * instruction_text_percentage_y)

# ------------- SFX -------------
# gunshot_SFX = pygame.mixer.Sound("/Users/aimeemai/Documents/GitHub/SBHACKS-24/assets/sfx/gunshot.mp3")
# death_SFX = pygame.mixer.Sound("/Users/aimeemai/Documents/GitHub/SBHACKS-24/assets/sfx/death.mp3")
# gunblock_SFX = pygame.mixer.Sound("/Users/aimeemai/Documents/GitHub/SBHACKS-24/assets/sfx/gunblock.mp3")
# shield_SFX = pygame.mixer.Sound("/Users/aimeemai/Documents/GitHub/SBHACKS-24/assets/sfx/shield_questionmark.mp3")
# reload_SFX = pygame.mixer.Sound("/Users/aimeemai/Documents/GitHub/SBHACKS-24/assets/sfx/reload.mp3")

gunshot_SFX = pygame.mixer.Sound("assets/sfx/gunshot.mp3")
death_SFX = pygame.mixer.Sound("assets/sfx/death.mp3")
gunblock_SFX = pygame.mixer.Sound("assets/sfx/gunblock.mp3")
shield_SFX = pygame.mixer.Sound("assets/sfx/shield_questionmark.mp3")
reload_SFX = pygame.mixer.Sound("assets/sfx/reload.mp3")

instruction_lines = [
    "Shoot: Attempt to shoot the opponent",
    "Shield: Protect yourself from an opponent's shot",
    "Reload: Prepare the shotgun for the next shot",
    "Last one alive wins!"
]

outcome_lines = [
    "1. If both players choose to reload,",
    "   nothing happens; both players reload",
    "   2. If one player chooses to reload and the other chooses",
    "   to shoot, the shot player loses",
    "3. If one player chooses to shield and the other ",
    "   chooses to shoot, the shooting player's shot is blocked",
    "4. If both players choose to shield,",
    "   nothing happens; both players are protected",
    "5. If both players choose to shoot,",
    "   both players lose"
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

idle_anim_percentage_x = 0.3
idle_anim_percentage_y = 0.1 
idle_anim_x = int(display_width * idle_anim_percentage_x)
idle_anim_y = int(display_height * idle_anim_percentage_y)

cp_shoot_percentage_x = 0.3
cp_shoot_percentage_y = 0.1 
cp_shoot_x = int(display_width * cp_shoot_percentage_x)
cp_shoot_y = int(display_height * cp_shoot_percentage_y)

cp_shield_percentage_x = 0.3
cp_shield_percentage_y = 0.1 
cp_shield_x = int(display_width * cp_shield_percentage_x)
cp_shield_y = int(display_height * cp_shield_percentage_y)

cp_reload_percentage_x = 0.3
cp_reload_percentage_y = 0.1 
cp_reload_x = int(display_width * cp_reload_percentage_x)
cp_reload_y = int(display_height * cp_reload_percentage_y)

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
start_text = start_font.render("Shoot to start the game", True, (222, 169, 169))
start_text_outline = start_font.render("Shoot to start the game", True, (0, 0, 0))
start_text_percentage_x = 0.4
start_text_percentage_y = 0.5 
start_text_x = int(display_width * start_text_percentage_x)
start_text_y = int(display_height * start_text_percentage_y)

# SCORE
score_font = pygame.font.Font('freesansbold.ttf', 36)
wins_text = score_font.render("Wins: " + str(wins), True, (255, 255, 255))
wins_text_outline = score_font.render("Wins: " + str(wins), True, (0, 0, 0))
wins_x = 20
wins_y = 20
losses_text = score_font.render("Losses: " + str(losses), True, (255, 255, 255))
losses_text_outline = score_font.render("Losses: " + str(losses), True, (0, 0, 0))
losses_x = 20
losses_y = 20

# bullets_text = score_font.render("Bullets: " + str(bullets), True, (255, 255, 255))
# bullets_text_outline = score_font.render("Bullets: " + str(bullets), True, (0, 0, 0))
# bullets_x = 20
# bullets_y = 20
# shields_text = score_font.render("Shields: " + str(shields), True, (255, 255, 255))
# shields_text_outline = score_font.render("Shields: " + str(shields), True, (0, 0, 0))
# shields_x = 850
# shields_y = 20

# COUNTDOWN
countdown_time = 1000
current_countdown_int = 4
countdown_font = pygame.font.Font('freesansbold.ttf', 72)
countdown_text = countdown_font.render(str(current_countdown_int), True, (222, 169, 169))
countdown_text_outline = countdown_font.render(str(current_countdown_int), True, (0, 0, 0))
countdown_text_percentage_x = .5
countdown_text_percentage_y = .15
countdown_text_x = int(display_width * countdown_text_percentage_x)
countdown_text_y = int(display_height * countdown_text_percentage_y)

# END SCREEN
game_over_font = pygame.font.Font('freesansbold.ttf', 84)
winner_text = game_over_font.render("You Win!", True, (222, 169, 169))
winner_text_outline = game_over_font.render("You Win!", True, (0, 0, 0))
draw_text = game_over_font.render("It's a Draw", True, (222, 169, 169))
draw_text_outline = game_over_font.render("It's a Draw", True, (0, 0, 0))
loser_text = game_over_font.render("You Lose!", True, (222, 169, 169))
loser_text_outline = game_over_font.render("You Lose!", True, (0, 0, 0))
game_over_text_percentage_x = 0.39
game_over_text_percentage_y = 0.65
game_over_text_x = int(display_width * game_over_text_percentage_x)
game_over_text_y = int(display_height * game_over_text_percentage_y)


quit_font = pygame.font.Font('freesansbold.ttf', 36)
quit_text = quit_font.render("Point your thumb down to quit", True, (255, 255, 255))
quit_text_outline = quit_font.render("Point your thumb down to quit", True, (0, 0, 0))
quit_text_percentage_x = 0.34
quit_text_percentage_y = 0.75
quit_text_x = int(display_width * quit_text_percentage_x)
quit_text_y = int(display_height * quit_text_percentage_y)

replay_font = pygame.font.Font('freesansbold.ttf', 36)
replay_text = replay_font.render("Shoot to replay the game", True, (222, 169, 169))
replay_text_outline = replay_font.render("Shoot to replay the game", True, (0, 0, 0))
replay_text_percentage_x = 0.37
replay_text_percentage_y = 0.8 
replay_text_x = int(display_width * replay_text_percentage_x)
replay_text_y = int(display_height * replay_text_percentage_y)

choices = {"shield": 2, "shoot": 0}

def update_results():
    global wins_text, wins_text_outline, wins_x, wins_y, losses_text, losses_text_outline, losses_x, losses_y
    wins_text = score_font.render("Wins: " + str(wins), True, (255, 255, 255))
    wins_text_outline = score_font.render("Wins: " + str(wins), True, (0, 0, 0))
    wins_x = 20
    wins_y = 20
    losses_text = score_font.render("Losses: " + str(losses), True, (255, 255, 255))
    losses_text_outline = score_font.render("Losses: " + str(losses), True, (0, 0, 0))
    losses_x = 850
    losses_y = 20

# def update_stats(bullet = 0, shield = 0):
#     global bullets_text, bullets_text_outline, bullets_x, bullets_y, shields_text, shields_text_outline, shields_x, shields_y
#     if bullet:
#         bullets_text = score_font.render("Bullets: " + str(bullets), True, (255, 255, 255))
#         bullets_text_outline = score_font.render("Bullets: " + str(bullets), True, (0, 0, 0))
#         bullets_x = 20
#         bullets_y = 20

#     if shield:
#         shields_text = score_font.render("Shields: " + str(shields), True, (255, 255, 255))
#         shields_text_outline = score_font.render("Shields: " + str(shields), True, (0, 0, 0))
#         shields_x = 850
#         shields_y = 20
#     stats_display()

def stats_display():
    # main_scene.blit(bullets_text_outline, (bullets_x - 2, bullets_y - 2))
    # main_scene.blit(bullets_text_outline, (bullets_x - 2, bullets_y))
    # main_scene.blit(bullets_text_outline, (bullets_x, bullets_y - 2))
    # main_scene.blit(bullets_text_outline, (bullets_x, bullets_y + 2))
    # main_scene.blit(bullets_text_outline, (bullets_x + 2, bullets_y))
    # main_scene.blit(bullets_text_outline, (bullets_x + 2, bullets_y + 2))
    # main_scene.blit(bullets_text, (bullets_x, bullets_y))

    # main_scene.blit(shields_text_outline, (shields_x - 2, shields_y - 2))
    # main_scene.blit(shields_text_outline, (shields_x - 2, shields_y))
    # main_scene.blit(shields_text_outline, (shields_x, shields_y - 2))
    # main_scene.blit(shields_text_outline, (shields_x, shields_y + 2))e
    # main_scene.blit(shields_text_outline, (shields_x + 2, shields_y))
    # main_scene.blit(shields_text_outline, (shields_x + 2, shields_y + 2))
    # main_scene.blit(shields_text, (shields_x, shields_y))
    global bullets, shields
    stats_y = int(display_height * .85)
    bullet_x1 = int(display_width * .05)
    bullet_x2 = int(display_width * .1)
    shields_x1 = int(display_width * .83)
    shields_x2 = int(display_width * .9)
    
    main_scene.blit(bullet_icon_outline, (bullet_x1, stats_y))
    main_scene.blit(bullet_icon_outline, (bullet_x2, stats_y))
    if bullets >= 1:
        main_scene.blit(bullet_icon, (bullet_x1, stats_y))
    if bullets == 2:
        main_scene.blit(bullet_icon, (bullet_x2, stats_y))
    
    if shields >= 1:
        main_scene.blit(shield_icon, (shields_x1, stats_y))
    if shields == 2:
        main_scene.blit(shield_icon, (shields_x2, stats_y))

def end_game_display(result):
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

    main_scene.blit(replay_text_outline, (replay_text_x - 2, replay_text_y - 2))
    main_scene.blit(replay_text_outline, (replay_text_x - 2, replay_text_y))
    main_scene.blit(replay_text_outline, (replay_text_x, replay_text_y - 2))
    main_scene.blit(replay_text_outline, (replay_text_x, replay_text_y + 2))
    main_scene.blit(replay_text_outline, (replay_text_x + 2, replay_text_y))
    main_scene.blit(replay_text_outline, (replay_text_x + 2, replay_text_y + 2))
    main_scene.blit(replay_text, (replay_text_x, replay_text_y))

    main_scene.blit(quit_text_outline, (quit_text_x - 2, quit_text_y - 2))
    main_scene.blit(quit_text_outline, (quit_text_x - 2, quit_text_y))
    main_scene.blit(quit_text_outline, (quit_text_x, quit_text_y - 2))
    main_scene.blit(quit_text_outline, (quit_text_x, quit_text_y + 2))
    main_scene.blit(quit_text_outline, (quit_text_x + 2, quit_text_y))
    main_scene.blit(quit_text_outline, (quit_text_x + 2, quit_text_y + 2))
    main_scene.blit(quit_text, (quit_text_x, quit_text_y))

    if result == 1:
        x, y = winner_text, winner_text_outline
    elif result == 3:
        x, y = draw_text, draw_text_outline
    elif result == 2:
        x, y = loser_text, loser_text_outline
    else:
        return
    
    main_scene.blit(y, (game_over_text_x - 2, game_over_text_y - 2))
    main_scene.blit(y, (game_over_text_x - 2, game_over_text_y))
    main_scene.blit(y, (game_over_text_x, game_over_text_y - 2))
    main_scene.blit(y, (game_over_text_x, game_over_text_y + 2))
    main_scene.blit(y, (game_over_text_x + 2, game_over_text_y))
    main_scene.blit(y, (game_over_text_x + 2, game_over_text_y + 2))
    main_scene.blit(x, (game_over_text_x, game_over_text_y))

    pygame.display.update()

def menu_display():
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
    
def countdown_display():
    if current_countdown_int > 0:
        main_scene.blit(countdown_text_outline, (countdown_text_x - 2, countdown_text_y - 2))
        main_scene.blit(countdown_text_outline, (countdown_text_x - 2, countdown_text_y))
        main_scene.blit(countdown_text_outline, (countdown_text_x, countdown_text_y - 2))
        main_scene.blit(countdown_text_outline, (countdown_text_x - 2, countdown_text_y + 2))
        main_scene.blit(countdown_text_outline, (countdown_text_x + 2, countdown_text_y))
        main_scene.blit(countdown_text_outline, (countdown_text_x + 2, countdown_text_y + 2))
        main_scene.blit(countdown_text, (countdown_text_x, countdown_text_y))

def game_results(result):
    global game_state, game_over_state, wins, losses
    game_state = False
    game_over_state = True
    if result == result_win:
        wins += 1
    elif result == result_lose:
        losses += 1
    update_results()
    
def convert_gesture_name(gest_name):
    match gest_name:
        case "none":
            return "None"
        case "one":
            return "Reload"
        case "thumbsdown":
            return "Thumbs Down"
        case "stop":
            return "Shield"
        case "shoot":
            return "Shoot"

# recognizer options.
# model saved in model_asset_path
# running mode is set to live stream
# print_result saves the result
options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path='models/gesture_recognizer_readd_thumb.task'),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=save_result)   
with GestureRecognizer.create_from_options(options) as recognizer:
    # The detector is initialized. Use it here.
    with mp_hands.Hands(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
            while running and cap.isOpened():
                success, img = cap.read()
                img = cv2.resize(img, (360, 270))
                frame_count += 1
                image = img.copy()
                if not success:
                    print("Ignoring empty camera frame.")
                    continue
                
                image.flags.writeable = False
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = hands.process(image)
                
                # Drawing hand annotations on image
                image.flags.writeable = True
                # changing color output?
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                
                # # creating image in pygame to draw hands onto
                # screen = pygame.display.get_surface()

                # capture = pygame.surfarray.pixels3d(screen)
                # capture = capture.transpose([1, 0, 2])
                # capture_bgr = cv2.cvtColor(capture, cv2.COLOR_RGB2BGR)
                
                hand_img = np.empty(image.shape)
                hand_img.fill(255)
                
                # collection of detected hands
                if results.multi_hand_landmarks:
                    # for each hand, draw the landmarks
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(
                            image,
                            #hand_img,
                            hand_landmarks,
                            mp_hands.HAND_CONNECTIONS,
                            mp_drawing_styles.get_default_hand_landmarks_style(),
                            mp_drawing_styles.get_default_hand_connections_style())
                # Flipping image for selfie display
                
                # Processing result
                top_gesture = ""
                #print(prev_result)
                if prev_result is not None and len(prev_result.gestures) > 0:
                    top_gesture = prev_result.gestures[0][0].category_name
                    print(f"top_gesture: {top_gesture}")
                    #print(f"type: {type(top_gesture)}")
                    match top_gesture:
                        case "stop":
                            pygame.event.post(pygame.event.Event(STOP_GEST))
                            print("Gesturing stop")
                        case "shoot":
                            pygame.event.post(pygame.event.Event(SHOOT_GEST))
                            print("Gesturing shoot")
                        case "thumbsdown":
                            pygame.event.post(pygame.event.Event(THUMBS_DOWN_GEST))
                            print("Gesturing thumbs down")
                        case "one":
                            pygame.event.post(pygame.event.Event(POINT_ONE_GEST))
                            print("Gesturing point/one")
                
                # Text to display hand value
                # cv_font = cv2.FONT_HERSHEY_DUPLEX
                # cv2.putText(image,  
                #     str(top_gesture),  
                #     (50, 50),
                #     cv_font, 1,  
                #     (0, 255, 255),  
                #     2,  
                #     cv2.LINE_4)
                
                
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image = np.rot90(image)
                image = pygame.surfarray.make_surface(image)
                main_scene.blit(image, (600,600))
                #pygame.display.update()
                # TODO: fix video display

                        
                # Displays video
                #cv2.imshow("MediaPipe Hands", cv2.flip(image, 1))
                #cv2.imshow("MediaPipe Hands", cv2.flip(hand_img, 1))
                            
                # recognition stuff
                mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img)
                     
                
                # timestamp is in milliseconds
                timestamp = frame_count * 1000/fps
                print(f"timestamp: {timestamp}")
                            
                recognizer.recognize_async(mp_image, int(timestamp))

                if cv2.waitKey(5) & 0xFF == 27:
                    break               
                
                
                # for event in pygame.event.get():
                #     if event.type == pygame.MOUSEBUTTONDOWN:
                #         if temp_start_rect.collidepoint(event.pos):
                #             tutorial_state = True
                #             menu_state = False
                #             main_scene.fill((0, 0, 0))
                #             pygame.display.update(idle_anim, clock, main_scene, idle_anim_x, idle_anim_y)
                #             shoot_anim, shield_anim, reload_anim = tutorial.start_tutorial(tutorial_shoot, tutorial_shield, tutorial_reload)
                #     if event.type == pygame.QUIT:
                #             running = False

                if menu_state:
                    menu_display()
                    for event in pygame.event.get():
                        # if event.type == pygame.KEYDOWN:
                        #     if event.key == pygame.K_h:
                        if (event.type == STOP_GEST) or (event.type == pygame.KEYDOWN and event.key == pygame.K_h):
                            tutorial_state = True
                            menu_state = False
                            main_scene.fill((0, 0, 0))
                            pygame.display.update()
                            shoot_anim, shield_anim, reload_anim = tutorial.start_tutorial(tutorial_shoot, tutorial_shield, tutorial_reload)
                            #if event.type == pygame.K_t:
                        if (event.type == SHOOT_GEST) or (event.type == pygame.KEYDOWN and event.key == pygame.K_t):
                            game_state = True
                            menu_state = False
                            idle_anim = computer.start_cp_anim(idle)
                            cp_shoot, cp_shield, cp_reload = tutorial.start_tutorial(shoot_sprite, shield_sprite, reload_sprite)
                            
                            main_scene.blit(background, (0, 0))
                        if event.type == pygame.QUIT:
                            running = False

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

                    cont_text = font.render("Shoot to continue or thumbs down to go back!", True, text_color)
                    cont_rect = cont_text.get_rect(center=(instruction_text_x * 1.3, instruction_text_y * 1.3))
                    main_scene.blit(cont_text, cont_rect)
                    
                    tutorial.update_tutorial(shoot_anim, shield_anim, reload_anim, clock, main_scene, shoot_anim_x, shoot_anim_y, shield_anim_x, shield_anim_y, reload_anim_x, reload_anim_y)
                    main_scene.fill((0, 0, 0))
                    for event in pygame.event.get():
                        # go back with thumbs down
                        if (event.type == THUMBS_DOWN_GEST) or (event.type == pygame.KEYDOWN and event.key == pygame.K_b):
                            tutorial_state = False
                            menu_state = True
                            main_scene.blit(background, (0, 0))
                                # shoot to continue to game
                        if (event.type == SHOOT_GEST) or (event.type == pygame.KEYDOWN and event.key == pygame.K_t):
                            game_state = True
                            tutorial_state = False
                            idle_anim = computer.start_cp_anim(idle)
                            cp_shoot, cp_shield, cp_reload = tutorial.start_tutorial(shoot_sprite, shield_sprite, reload_sprite)
                            main_scene.blit(background, (0, 0))
                        if event.type == pygame.QUIT:
                            running = False

                if game_state:
                    main_scene.blit(background, (0, 0))
                    main_scene.blit(image, (600,600))
                    countdown_display()
                    stats_display()
                    # display top_gesture
                    user_gest_name = convert_gesture_name(top_gesture)
                    top_gest_text = font.render(user_gest_name, True, (0, 0, 0))
                    main_scene.blit(top_gest_text, (600, 600))
                    computer.update_cp_anim(idle_anim, clock, main_scene, idle_anim_x, idle_anim_y)
                    player_move = None
                    
                    if not player_can_make_move:
                        countdown_time -= clock.get_time()           
                        if countdown_time <= 0:
                            current_countdown_int-= 1
                            countdown_text = countdown_font.render(str(current_countdown_int), True, (222, 169, 169))
                            countdown_text_outline = countdown_font.render(str(current_countdown_int), True, (0, 0, 0))
                            countdown_time = 1000           
                        if current_countdown_int <= 0:
                            player_can_make_move = True
                    
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        if player_can_make_move:
                            if (event.type == SHOOT_GEST) or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                                player_move = "shoot"
                            elif (event.type == POINT_ONE_GEST) or (event.type == pygame.KEYDOWN and event.key == pygame.K_w):
                                player_move = "reload"
                            elif (event.type == STOP_GEST) or (event.type == pygame.KEYDOWN and event.key == pygame.K_e):
                                player_move = "shield"
                    
                    if player_move:
                        computer_move = computer.computer_choice(choices, bullets, shields)
                        if computer_move == "shoot":
                            gunshot_SFX.play()
                            computer.cp_move(shoot_sprite, clock, main_scene, cp_shoot_x, cp_shoot_y, background, cp_shoot)
                        elif computer_move == "shield":
                            shield_SFX.play()
                            computer.cp_move(shield_sprite, clock, main_scene, cp_shield_x, cp_shield_y, background, cp_shield)
                            pygame.display.update()
                        elif computer_move == "reload":
                            reload_SFX.play()
                            computer.cp_move(reload_sprite, clock, main_scene, cp_reload_x, cp_reload_y, background, cp_reload)
                        else:
                            computer.update_cp_anim(idle_anim, clock, main_scene, idle_anim_x, idle_anim_y)
                            pygame.display.update()
                            pygame.time.delay(300)

                        if player_move == "shoot" and bullets > 0:
                            if computer_move == "shoot": 
                                game_results(result_tie)
                                recent_result = result_tie
                                game_over_state = True
                                game_state = False
                            elif computer_move == "shield":
                                gunblock_SFX.play()
                                bullets -= 1
                                choices["shield"] -= 1
                            else:
                                game_results(result_win)
                                recent_result = result_win
                                game_over_state = True
                                game_state = False
                        elif player_move == "shoot" and bullets == 0:
                            if computer_move == "shoot":
                                game_results(result_lose)
                                recent_result = result_lose
                                game_over_state = True
                                game_state = False
                            elif computer_move == "shield":
                                choices["shield"] -= 1
                            else:
                                if choices["shoot"] < 2:
                                    choices["shoot"] += 1
                        elif player_move == "shield" and shields > 0:
                            shields -= 1
                            if computer_move == "shoot":
                                choices["shoot"] -= 1
                            elif computer_move == "shield":
                                choices["shield"] -= 1
                            else:
                                if choices["shoot"] < 2:
                                    choices["shoot"] += 1
                        elif player_move == "shield" and shields == 0:
                            if computer_move == "shoot":
                                game_results(result_lose)
                                recent_result = result_lose
                                game_over_state = True
                                game_state = False
                            elif computer_move == "shield":
                                shield_SFX.play()
                                choices["shield"] -= 1
                            else:
                                if choices["shoot"] < 2:
                                    choices["shoot"] += 1
                        else:
                            if computer_move == "shoot":
                                death_SFX.play()
                                game_results(result_lose)
                                recent_result = result_lose
                                game_over_state = True
                                game_state = False
                            elif computer_move == "shield":
                                reload_SFX.play()
                                shield_SFX.play()
                                choices["shield"] -= 1
                                if bullets < 2:
                                    bullets += 1
                            else:
                                reload_SFX.play()
                                if bullets < 2:
                                    bullets += 1
                                if choices["shoot"] < 2:
                                    choices["shoot"] += 1
                        player_can_make_move = False
                        current_countdown_int = 4
            
    if game_over_state:
        end_game_display(recent_result)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    bullets = 0
                    shields = 2
                    game_state = True
                    game_over_state = False
