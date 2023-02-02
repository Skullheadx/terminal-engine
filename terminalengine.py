import curses
import time
import random
import sys
import os
import math
import threading
from itertools import combinations

from framebuffer import FrameBuffer


class TerminalEngine:
    char = '█'
    TERMINAL_SIZE = [math.floor(os.get_terminal_size().columns / 2), os.get_terminal_size().lines - 1]

    def __init__(self, width=80, height=24):
        try:
            self.stdscr = curses.initscr()

            curses.noecho()
            curses.cbreak()

            self.stdscr.keypad(True)

            self.stdscr.nodelay(True)

            try:
                curses.start_color()
            except:
                pass

        finally:
            if 'self.stdscr' in locals():
                self.stdscr.keypad(False)
                curses.echo()
                curses.nocbreak()
                curses.endwin()

        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = width, height

        self.frame = FrameBuffer(self.TERMINAL_SIZE[0], self.TERMINAL_SIZE[1], self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

        self.event = self.Event()
        self.draw = self.Draw(self.frame)
        self.color = self.Color()

    def update(self, stdscr):
        self.frame.clear()
        # stdscr.clear()
        pass

    def render(self, stdscr):
        for i in range(len(self.frame.frame_buffer)):
            for j in range(len(self.frame.frame_buffer[i])):
                if self.frame.frame_buffer[i][j] is not None:
                    stdscr.addstr(i, j * 2, self.char, self.color.color_dict[self.frame.frame_buffer[i][j]])
                    if j * 2 + 1 < self.TERMINAL_SIZE[0] * 2:
                        stdscr.addstr(i, j * 2 + 1, self.char, self.color.color_dict[self.frame.frame_buffer[i][j]])
                else:
                    stdscr.addstr(i, j * 2, self.char, self.color.BLACK)
                    if j * 2 + 1 < self.TERMINAL_SIZE[0] * 2:
                        stdscr.addstr(i, j * 2 + 1, self.char, self.color.BLACK)

        stdscr.refresh()

    def run(self, update):
        is_running = True
        prev_time = time.time()
        while is_running:
            delta_time = (time.time() - prev_time) * 1000  # in milliseconds
            prev_time = time.time()

            self.event.update(self.stdscr)
            for event in self.event.get(key='q', clear=False):
                if event == 'q':
                    is_running = False
                    break
            self.update(self.stdscr)
            update(self, delta_time)
            self.render(self.stdscr)
            # time.sleep(0.16)

    class Event:

        def __init__(self):
            self.events = []

        def update(self, stdscr):
            try:
                key = stdscr.getkey()
            except:
                key = None
            if key is not None and (len(self.events) == 0 or key != self.events[-1] != key):
                self.events.append(key)

        def get(self, key=None, clear=True):
            if key is None:
                output = self.events.copy()
            else:
                output = []
                for event in self.events:
                    if event == key:
                        output.append(event)
            if clear:
                self.events.clear()
            return output

    class Color:
        DEFAULT = 0
        RED = 1
        GREEN = 2
        YELLOW = 3
        BLUE = 4
        WHITE = 5
        BLACK = 6
        CYAN = 7
        MAGENTA = 8

        def __init__(self):
            curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLUE)
            curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
            curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
            curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
            curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)
            curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_WHITE)
            curses.init_pair(7, curses.COLOR_CYAN, curses.COLOR_BLACK)
            curses.init_pair(8, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
            self.color_dict = {self.DEFAULT: curses.color_pair(5),
                               self.RED: curses.color_pair(1),
                               self.GREEN: curses.color_pair(2),
                               self.YELLOW: curses.color_pair(3),
                               self.BLUE: curses.color_pair(4),
                               self.WHITE: curses.color_pair(5),
                               self.BLACK: curses.color_pair(6),
                               self.CYAN: curses.color_pair(7),
                               self.MAGENTA: curses.color_pair(8)}

    class Draw:
        line_precision = 100

        def __init__(self, frame):
            self.frame = frame
            self.color = TerminalEngine.Color()

        def rect(self, x, y, width, height, color, thickness=0):
            if thickness <= 0:
                for i in range(height):
                    for j in range(width):
                        self.frame.set_pixel(x + j, y + i, color)
            else:
                for i in range(height):
                    for j in range(width):
                        if i < thickness or i >= height - thickness or j < thickness or j >= width - thickness:
                            self.frame.set_pixel(x + j, y + i, self.color.BLACK)
                        else:
                            self.frame.set_pixel(x + j, y + i, color)

        def rect2(self, rect, thickness=0):
            self.rect(rect.x, rect.y, rect.width, rect.height, rect.color, thickness)

        def line(self, x1, y1, x2, y2, color):
            if x1 == x2:
                for i in range(y1, y2):
                    self.frame.set_pixel(x1, i, color)
            elif y1 == y2:
                for i in range(x1, x2):
                    self.frame.set_pixel(i, y1, color)
            else:
                m = (y2 - y1) / (x2 - x1)
                b = y1 - m * x1
                for i in range((x2 - x1) * self.line_precision):
                    self.frame.set_pixel(x1 + i / self.line_precision, m * (x1 + i / self.line_precision) + b, color)

        def check_point(self, h, k, x, y, a, b):
            return (pow((x - h), 2) / pow(a, 2)) + (pow((y - k), 2) / pow(b, 2))

        def ellipse(self, x, y, width, height, color):
            for i in range(1, height * 2):
                for j in range(1, width * 2):
                    check = self.check_point(width, height, j, i, width, height)
                    if check <= 1:
                        self.frame.set_pixel(x + j - 1 - width, y + i - 1 - height, color)

    class Rect:
        def __init__(self, x, y, width, height, color):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.color = color

            self.left = self.x
            self.right = self.x + self.width
            self.top = self.y
            self.bottom = self.y + self.height

        def move(self, x, y):
            self.x += x
            self.y += y
            self.left = self.x
            self.right = self.x + self.width
            self.top = self.y
            self.bottom = self.y + self.height

        def get_area(self):
            return self.width * self.height

        def collide_rect(self, rect):
            if self.x < rect.x + rect.width and self.x + self.width > rect.x and \
                    self.y < rect.y + rect.height and self.y + self.height > rect.y:
                return True
            return False

    class Collision:
        TOTAL_COLLISION_LAYERS = 10
        collision_layers = {i: [] for i in range(TOTAL_COLLISION_LAYERS)}

        n = 25
        width, height = [math.floor(os.get_terminal_size().columns / 2), os.get_terminal_size().lines - 1]

        def update(self):
            for layer in self.collision_layers:
                self.check_sprite_collision_list(self.collision_layers[layer])

        def add_sprite(self, sprite):
            self.collision_layers[sprite.collision_layer].append(sprite)

        def remove_sprite(self, sprite):
            self.collision_layers[sprite.collision_layer].remove(sprite)

        def clear_layer(self, layer):
            self.collision_layers[layer].clear()

        def clear_all(self):
            for layer in self.collision_layers:
                self.collision_layers[layer].clear()

        @staticmethod
        def check_sprite_collision(sprite1, sprite2):
            if sprite1.collision_layer == sprite2.collision_layer:
                return sprite1.rect.collide_rect(sprite2.rect)
            return False

        # partition the screen into a grid and only check collision with sprites in the same grid
        def check_sprite_collision_list(self, sprite_list):
            for a, b in self.space_partition(sprite_list):
                if self.check_sprite_collision(a, b):
                    return True
            return False

        def space_partition(self, sprite_list):  # broad phase collision detection
            grid = [[[] for _ in range(self.n)] for _ in range(self.n)]
            for sprite in sprite_list:
                x1 = int(sprite.left // (self.width / self.n))
                x2 = int(sprite.right // (self.width / self.n))
                y1 = int(sprite.top // (self.height / self.n))
                y2 = int(sprite.bottom // (self.height / self.n))
                if x1 < 0:
                    x1 = 0
                if x2 < 0:
                    x2 = 0
                if y1 < 0:
                    y1 = 0
                if y2 < 0:
                    y2 = 0
                if x1 >= self.n:
                    x1 = self.n - 1
                if x2 >= self.n:
                    x2 = self.n - 1
                if y1 >= self.n:
                    y1 = self.n - 1
                if y2 >= self.n:
                    y2 = self.n - 1
                grid[y1][x1].append(sprite)
                grid[y1][x2].append(sprite)
                grid[y2][x1].append(sprite)
                grid[y2][x2].append(sprite)
            checks = []
            for i in range(self.n):
                for j in range(self.n):
                    checks.extend(tuple(combinations(grid[i][j], 2)))
            return list(set(checks))

    class Sprite:
        def __init__(self, x, y, width, height, color, collision_layer=0):
            self.rect = TerminalEngine.Rect(x, y, width, height, color)
            self.collision_layer = collision_layer
            TerminalEngine.Collision().add_sprite(self)

        def update(self, delta_time):
            pass

        def move(self, x=0, y=0):
            self.rect.move(x, y)

        def draw(self, tengine):
            tengine.draw.rect2(self.rect)
