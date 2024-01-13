import main
import pygame

x = 200
y = 150
def hands(selected_choice):
    index = 0
    if selected_choice == "shoot":
        while index < 4:
            main.clock.tick(4)
            if index >= len(main.shoot_sprite):
                index = 0

            main.window.blit(main.shoot_sprite[index], (x, y))
            main.pygame.display.update()
            main.window.fill((0, 0, 0))
            index += 1
    elif selected_choice == "shield":
            main.clock.tick(1)
            if index >= len(main.shield_sprite):
                index = 0

            main.window.blit(main.shield_sprite[index], (x, y))
            main.pygame.display.update()
    elif selected_choice == "reload":
        while index < 3:
            main.clock.tick(3)
            if index >= len(main.reload_sprite):
                index = 0

            main.window.blit(main.reload_sprite[index], (x, y))
            main.pygame.display.update()
            main.window.fill((0, 0, 0))
            index += 1