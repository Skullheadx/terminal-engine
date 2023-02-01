class FrameBuffer:
    char = '█'


    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.frame_buffer = [[0 for i in range(self.screen_width)] for j in range(self.screen_height)]

    def update(self):
        pass

    def set_pixel(self, x, y, color):
        if x < 0 or x >= self.screen_width or y < 0 or y >= self.screen_height: # Out of bounds
            return
        self.frame_buffer[y][x] = color
