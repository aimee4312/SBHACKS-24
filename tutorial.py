import pygame
class tutorial_animations:
    def __init__(self, animation, looping=True) -> None:
        self.speed = 1.0
        self.speed_factor = 1.0
        self.looping = looping
        self.frames = animation
        self.current_frame = self.frames[0]
        self.frame_index = 0
        self.next_frame_acc = 0.0
        self.running = True

    def start(self, speed_factor = 10.0):
        self.speed_factor = speed_factor
        self.frame_index = 0
        self.next_frame_acc = 0.0
        self.running = True
        self.current_frame = self.frames[0]

    def update(self, time_delta):
        if self.running:
            self.next_frame_acc += time_delta * self.speed * self.speed_factor
            if self.next_frame_acc > 1.0:
                self.next_frame_acc = 0.0
                self.frame_index += 1
                if self.frame_index >= len(self.frames):
                    if not self.looping:
                        self.frame_index -= 1
                        self.running = False
                    else:
                        self.frame_index = 0
                self.current_frame = self.frames[self.frame_index]

def start_tutorial(tutorial_shoot, tutorial_shield, tutorial_reload):
    shoot_anim = tutorial_animations(tutorial_shoot)
    shield_anim = tutorial_animations(tutorial_shield)
    reload_anim = tutorial_animations(tutorial_reload)
    shoot_anim.start()
    shield_anim.start()
    reload_anim.start()
    return shoot_anim, shield_anim, reload_anim

def update_tutorial(shoot_anim, shield_anim, reload_anim, clock, main_scene, shoot_anim_x, shoot_anim_y, shield_anim_x, shield_anim_y, reload_anim_x, reload_anim_y):
    shoot_anim.update(clock.tick(60) / 1000.0)
    shield_anim.update(clock.tick(60) / 1000.0)
    reload_anim.update(clock.tick(60) / 1000.0)

    main_scene.blit(shoot_anim.current_frame, (shoot_anim_x, shoot_anim_y))
    main_scene.blit(shield_anim.current_frame, (shield_anim_x, shield_anim_y))
    main_scene.blit(reload_anim.current_frame, (reload_anim_x, reload_anim_y))
    pygame.display.update()