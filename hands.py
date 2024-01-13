import pygame

pygame.init()

window = pygame.display.set_mode((1000, 800))
shoot_sprite = [pygame.image.load("sprites/shoot1.png"),
                pygame.image.load("sprites/shoot2.png"),
                pygame.image.load("sprites/shoot3.png"),
                pygame.image.load("sprites/shoot1.png")]
reload_sprite = [pygame.image.load("sprites/reload1.png"),
                pygame.image.load("sprites/reload2.png"),
                pygame.image.load("sprites/reload1.png")]
shield_sprite = [pygame.image.load("sprites/shield.png")]

clock = pygame.time.Clock()
x = 200
y = 150
running = True
while running:
    index = 0
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:  
                while index < 4:
                    clock.tick(4)
                    if index >= len(shoot_sprite):
                        index = 0

                    image = shoot_sprite[index]
                    window.blit(image, (x, y))
                    pygame.display.update()
                    window.fill((0, 0, 0))
                    index += 1
            if event.key == pygame.K_s:
                    clock.tick(1)
                    if index >= len(shield_sprite):
                        index = 0

                    image = shield_sprite[index]
                    window.blit(image, (x, y))
                    pygame.display.update()
            if event.key == pygame.K_r:
                while index < 3:
                    clock.tick(3)
                    if index >= len(reload_sprite):
                        index = 0

                    image = reload_sprite[index]
                    window.blit(image, (x, y))
                    pygame.display.update()
                    window.fill((0, 0, 0))
                    index += 1
        elif event.type == pygame.QUIT:
            running = False

# function version
""" def hands(selected_choice):
    index = 0
    if selected_choice == "shoot":
        while index < 4:
            clock.tick(4)
            if index >= len(shoot_sprite):
                index = 0

            image = shoot_sprite[index]
            window.blit(image, (x, y))
            pygame.display.update()
            window.fill((0, 0, 0))
            index += 1
    elif selected_choice == "shield":
            clock.tick(1)
            if index >= len(shield_sprite):
                index = 0

            image = shield_sprite[index]
            window.blit(image, (x, y))
            pygame.display.update()
    elif selected_choice == "reload":
        while index < 3:
            clock.tick(3)
            if index >= len(reload_sprite):
                index = 0

            image = reload_sprite[index]
            window.blit(image, (x, y))
            pygame.display.update()
            window.fill((0, 0, 0))
            index += 1 """