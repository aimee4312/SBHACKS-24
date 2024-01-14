if game_state:
        delay_duration = 3000
        start_time = pygame.time.get_ticks()
        clock = pygame.time.Clock()

        main_scene.blit(background, (0, 0))

        while pygame.time.get_ticks() - start_time < delay_duration:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        computer_choice = computer.computer_choice(choices)

        if computer_choice == "shoot":
            computer.update_idle(cp_shoot, clock, main_scene, cp_shoot_x, cp_shoot_y)
        elif computer_choice == "shield":
            computer.update_idle(cp_shield, clock, main_scene, cp_shield_x, cp_shield_y)
        elif computer_choice == "reload":
            computer.update_idle(cp_reload, clock, main_scene, cp_reload_x, cp_reload_y)
        else:
            computer.update_idle(idle_anim, clock, main_scene, idle_anim_x, idle_anim_y)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False