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
    if selected_choice != "reload":
        choices[selected_choice] -= 1
        
    else:
        if choices["shoot"] < 2:
            choices["shoot"] += 1
    
    return selected_choice

def computer_choice_anim(choice):
    if choice == "shoot":
        pass
    elif choice == "shield":
        pass
    else:
        pass

def update_idle(idle_anim, clock, main_scene, idle_anim_x, idle_anim_y):
    idle_anim.update(clock.tick(60) / 1000.0)
    main_scene.blit(idle_anim.current_frame, (idle_anim_x, idle_anim_y))
    pygame.display.update()

def start_idle_display(idle):
    idle_anim = tutorial.tutorial_animations(idle)
    idle_anim.start(3)
    return idle_anim