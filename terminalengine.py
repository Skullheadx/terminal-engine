import curses
import time
import random
import sys
import os
import math
import threading

from framebuffer import FrameBuffer


class TerminalEngine:
    char = '█'

    def __init__(self, update, width=80, height=24):
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

        self.TERMINAL_SIZE = [math.floor(os.get_terminal_size().columns/2), os.get_terminal_size().lines - 1]
        self.frame = FrameBuffer(self.TERMINAL_SIZE[0], self.TERMINAL_SIZE[1], self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

        self.event = self.Event()
        self.draw = self.Draw(self.frame)
        self.color = self.Color()
        self.run(update)

    def update(self, stdscr):
        # stdscr.clear()
        pass

    def render(self, stdscr):
        for i in range(len(self.frame.frame_buffer)):
            for j in range(len(self.frame.frame_buffer[i])):
                if self.frame.frame_buffer[i][j] is not None:
                    stdscr.addstr(i, j*2, self.char, self.frame.frame_buffer[i][j])
                    if(j*2+1 < self.TERMINAL_SIZE[0]*2):
                        stdscr.addstr(i, j*2+1, self.char, self.frame.frame_buffer[i][j])

        stdscr.refresh()

    def run(self, update):
        is_running = True
        prev_time = time.time()
        while is_running:
            delta_time = time.time() - prev_time
            prev_time = time.time()

            self.event.update(self.stdscr)
            for event in self.event.get():
                if event == 'q':
                    is_running = False
                    break
            update(self, delta_time)
            self.update(self.stdscr)
            self.render(self.stdscr)

    class Event:

        def __init__(self):
            self.events = []

        def update(self, stdscr):
            try:
                key = stdscr.getkey()
            except:
                key = None
            if key is not None:
                self.events.append(key)

        def get(self):
            output = self.events.copy()
            self.events.clear()
            return output

    class Color:
        RED = None
        GREEN = None
        YELLOW = None
        BLUE = None
        WHITE = None
        BLACK = None
        CYAN = None
        MAGENTA = None

        def __init__(self):
            curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLUE)
            curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
            curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
            curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
            curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)
            curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_WHITE)
            curses.init_pair(7, curses.COLOR_CYAN, curses.COLOR_BLACK)
            curses.init_pair(8, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
            self.RED = curses.color_pair(1)
            self.GREEN = curses.color_pair(2)
            self.YELLOW = curses.color_pair(3)
            self.BLUE = curses.color_pair(4)
            self.WHITE = curses.color_pair(5)
            self.BLACK = curses.color_pair(6)
            self.CYAN = curses.color_pair(7)
            self.MAGENTA = curses.color_pair(8)

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
            return (pow((x - h), 2) / pow(a, 2)) + (pow((y - k), 2) / pow(b, 2));
        
        def ellipse(self, x, y, width, height, color):
            for i in range(1, height*2):
                for j in range(1, width*2):
                    check = self.check_point(width, height, j, i, width, height)
                    if(check <= 1):
                        self.frame.set_pixel(x + j - 1 - width, y + i - 1 - height, color)

    class Rect:
        def __init__(self, x, y, width, height, color):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.color = color

        def get_area(self):
            return self.width * self.height

        def collide_rect(self, rect):
            if self.x < rect.x + rect.width and self.x + self.width > rect.x and self.y < rect.y + rect.height and self.y + self.height > rect.y:
                return True
            return False
