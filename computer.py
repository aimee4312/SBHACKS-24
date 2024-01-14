import random
import tutorial
import pygame

def computer_choice(choices):
    possible_choices = ["reload"]
    if choices["shield"]:
        possible_choices.append("shield")
    if choices["shoot"]:
        possible_choices.append("shoot")
    
    selected_choice = random.choice(possible_choices)
    """ if selected_choice != "reload":
        choices[selected_choice] -= 1
        
    else:
        if choices["shoot"] < 2:
            choices["shoot"] += 1 """
    
    return selected_choice

def cp_move(cp_move, clock, main_scene, cp_x, cp_y, background, cp_anim):
    for frame in cp_move:
        main_scene.blit(background, (0, 0))
        update_cp_anim(cp_anim, clock, main_scene, cp_x, cp_y)
        pygame.time.delay(300)

def update_cp_anim(cp_anim, clock, main_scene, cp_anim_x, cp_anim_y):
    cp_anim.update(clock.tick(60) / 1000.0)
    main_scene.blit(cp_anim.current_frame, (cp_anim_x, cp_anim_y))
    pygame.display.update()

def start_cp_anim(idle):
    cp_anim = tutorial.tutorial_animations(idle)
    cp_anim.start(3)
    return cp_anim