class FrameBuffer:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.frame_buffer = [[0 for i in range(self.screen_width)] for j in range(self.screen_height)]

    def update(self):
        pass

    def set_pixel(self, x, y, color):
        self.frame_buffer[y][x] = 1
