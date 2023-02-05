from framebuffer import FrameBuffer


class Renderer:
    char = '█'

    def __init__(self, current_frame, color, terminal_width, terminal_height, screen_width, screen_height):
        self.current_frame = current_frame
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.terminal_width = terminal_width
        self.terminal_height = terminal_height
        self.previous_frame = FrameBuffer(self.terminal_width, self.terminal_height, self.screen_width,
                                          self.screen_height)
        self.color = color

    def render(self, stdscr):
        for i in range(len(self.current_frame.frame_buffer)):
            for j in range(len(self.current_frame.frame_buffer[i])):
                if self.current_frame.frame_buffer[i][j] is not None:
                    if self.current_frame.frame_buffer[i][j] != self.previous_frame.frame_buffer[i][j]:
                        stdscr.addstr(i, j * 2, self.char, self.color.get_pair(self.current_frame.frame_buffer[i][j]))
                        if j * 2 + 1 < self.terminal_width * 2:
                            stdscr.addstr(i, j * 2 + 1, self.char,
                                          self.color.color_pair_dict[self.current_frame.frame_buffer[i][j]])
                else:
                    stdscr.addstr(i, j * 2, self.char, self.color.BLACK)
                    if j * 2 + 1 < self.terminal_width * 2:
                        stdscr.addstr(i, j * 2 + 1, self.char, self.color.BLACK)
        self.previous_frame = copy_frame(self.current_frame)
        stdscr.refresh()


def copy_frame(self):
    new_frame = FrameBuffer(self.terminal_width, self.terminal_height, self.screen_width, self.screen_height)
    for i in range(len(self.frame_buffer)):
        for j in range(len(self.frame_buffer[i])):
            new_frame.frame_buffer[i][j] = self.frame_buffer[i][j]
    return new_frame
