class FrameBuffer:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.frameBuffer = [[0 for i in range(self.screen_width)] for j in range(self.screen_height)]
    def update(self):
        pass