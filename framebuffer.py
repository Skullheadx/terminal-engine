from math import ceil


class FrameBuffer:

    def __init__(self, terminal_width, terminal_height, screen_width, screen_height, ):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.terminal_width = terminal_width
        self.terminal_height = terminal_height

        self.frame_buffer = [[0 for i in range(self.terminal_width)] for j in range(self.terminal_height)]

        self.x_scale = self.terminal_width / self.screen_width
        self.y_scale = self.terminal_height / self.screen_height

    def set_pixel(self, x, y, color):
        display_x = int(x * self.x_scale)
        display_y = int(y * self.y_scale)
        if display_x < 0 or display_x >= self.terminal_width or display_y < 0 or display_y >= self.terminal_height:  # Out of bounds
            return

        next_display_x = int((x + 1) * self.x_scale)
        next_display_y = int((y + 1) * self.y_scale)

        for i in range(next_display_y - display_y):
            for j in range(next_display_x - display_x):
                self.frame_buffer[display_y + i][display_x + j] = color
        # self.frame_buffer[display_y][display_x] = color

