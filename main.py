import pygame

# initialize game
pygame.init()

# screen settings
screen_info = pygame.display.Info()
display_width = screen_info.current_w
display_height = screen_info.current_h
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("ShootOut", "ShootOut")

# background
background = pygame.image.load("assets/background/background.jpeg")

# game clock
clock = pygame.time.Clock()

# state handling
menu_state = True
tutorial_state = False
game_state = False
game_over_state = False
wins = 0
losses = 0

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

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if menu_state:
        screen.blit(menu_text_outline, (menu_x-2, menu_y-2))
        screen.blit(menu_text_outline, (menu_x-2, menu_y))
        screen.blit(menu_text_outline, (menu_x, menu_y-2))
        screen.blit(menu_text_outline, (menu_x, menu_y+2))
        screen.blit(menu_text_outline, (menu_x+2, menu_y))
        screen.blit(menu_text_outline, (menu_x+2, menu_y+2))
        screen.blit(menu_text, (menu_x, menu_y))

        screen.blit(help_text_outline, (help_x-2, help_y-2))
        screen.blit(help_text_outline, (help_x-2, help_y))
        screen.blit(help_text_outline, (help_x, help_y-2))
        screen.blit(help_text_outline, (help_x, help_y+2))
        screen.blit(help_text_outline, (help_x+2, help_y))
        screen.blit(help_text_outline, (help_x+2, help_y+2))
        screen.blit(help_text, (help_x, help_y))

        screen.blit(start_text_outline, (start_x-2, start_y-2))
        screen.blit(start_text_outline, (start_x-2, start_y))
        screen.blit(start_text_outline, (start_x, start_y-2))
        screen.blit(start_text_outline, (start_x, start_y+2))
        screen.blit(start_text_outline, (start_x+2, start_y))
        screen.blit(start_text_outline, (start_x+2, start_y+2))
        screen.blit(start_text, (start_x, start_y))

    if game_state:
        screen.blit(wins_text_outline, (wins_x-2, wins_y-2))
        screen.blit(wins_text_outline, (wins_x-2, wins_y))
        screen.blit(wins_text_outline, (wins_x, wins_y-2))
        screen.blit(wins_text_outline, (wins_x, wins_y+2))
        screen.blit(wins_text_outline, (wins_x+2, wins_y))
        screen.blit(wins_text_outline, (wins_x+2, wins_y+2))
        screen.blit(wins_text, (wins_x, wins_y))

        screen.blit(losses_text_outline, (losses_x-2, losses_y-2))
        screen.blit(losses_text_outline, (losses_x-2, losses_y))
        screen.blit(losses_text_outline, (losses_x, losses_y-2))
        screen.blit(losses_text_outline, (losses_x, losses_y+2))
        screen.blit(losses_text_outline, (losses_x+2, losses_y))
        screen.blit(losses_text_outline, (losses_x+2, losses_y+2))
        screen.blit(losses_text, (losses_x, losses_y))

    pygame.display.update()