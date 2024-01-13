import pygame

x = 200
y = 150
def hands(selected_choice, window, clock, shoot_sprite, shield_sprite, reload_sprite):
    index = 0
    if selected_choice == "shoot":
        while index < 4:
            clock.tick(4)
            if index >= len(shoot_sprite):
                index = 0

            window.blit(shoot_sprite[index], (x, y))
            pygame.display.update()
            window.fill((0, 0, 0))
            index += 1
    elif selected_choice == "shield":
            clock.tick(1)
            if index >= len(shield_sprite):
                index = 0

            window.blit(shield_sprite[index], (x, y))
            pygame.display.update()
    elif selected_choice == "reload":
        while index < 3:
            clock.tick(3)
            if index >= len(reload_sprite):
                index = 0

            window.blit(reload_sprite[index], (x, y))
            pygame.display.update()
            window.fill((0, 0, 0))
            index += 1