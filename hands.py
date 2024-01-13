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
    value = 0
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                while value < 4:
                    clock.tick(4)

                    if value >= len(shoot_sprite):
                        value = 0

                    image = shoot_sprite[value]

                    window.blit(image, (x, y))

                    pygame.display.update()

                    window.fill((0, 0, 0))

                    value += 1
            if event.key == pygame.K_s:
                    clock.tick(1)

                    if value >= len(shield_sprite):
                        value = 0

                    image = shield_sprite[value]

                    window.blit(image, (x, y))

                    pygame.display.update()

                    window.fill((0, 0, 0))

            if event.key == pygame.K_r:
                while value < 3:
                    clock.tick(3)

                    if value >= len(reload_sprite):
                        value = 0

                    image = reload_sprite[value]

                    window.blit(image, (x, y))

                    pygame.display.update()

                    window.fill((0, 0, 0))

                    value += 1
        elif event.type == pygame.QUIT:
            running = False