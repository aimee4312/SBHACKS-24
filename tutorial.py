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