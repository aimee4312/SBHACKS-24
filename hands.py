import main
import pygame
shoot_sprite = [main.pygame.image.load("sprites/shoot1.png"),
                main.pygame.image.load("sprites/shoot2.png"),
                main.pygame.image.load("sprites/shoot3.png"),
                main.pygame.image.load("sprites/shoot1.png")]
reload_sprite = [main.pygame.image.load("sprites/reload1.png"),
                main.pygame.image.load("sprites/reload2.png"),
                main.pygame.image.load("sprites/reload1.png")]
shield_sprite = [main.pygame.image.load("sprites/shield.png")]

x = 200
y = 150
def hands(selected_choice):
    index = 0
    if selected_choice == "shoot":
        while index < 4:
            main.clock.tick(4)
            if index >= len(shoot_sprite):
                index = 0

            image = shoot_sprite[index]
            main.window.blit(image, (x, y))
            main.pygame.display.update()
            main.window.fill((0, 0, 0))
            index += 1
    elif selected_choice == "shield":
            main.clock.tick(1)
            if index >= len(shield_sprite):
                index = 0

            image = shield_sprite[index]
            main.window.blit(image, (x, y))
            main.pygame.display.update()
    elif selected_choice == "reload":
        while index < 3:
            main.clock.tick(3)
            if index >= len(reload_sprite):
                index = 0

            image = reload_sprite[index]
            main.window.blit(image, (x, y))
            main.pygame.display.update()
            main.window.fill((0, 0, 0))
            index += 1