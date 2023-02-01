import curses
import time
import random
import sys
import os
import math
import threading

from framebuffer import FrameBuffer

class TerminalEngine:
    terminal_size = [os.get_terminal_size().columns, os.get_terminal_size().lines - 1]

    frame = FrameBuffer(terminal_size[0], terminal_size[1])
    def __init__(self, update, width=80, height=24):
        self.event = self.Event()
        self.draw = self.Draw(self.frame)

        self.run(update)

    def update(self, stdscr):
        # stdscr.clear()
        pass

    def render(self, stdscr):
        for i in range(len(self.frame.frame_buffer)):
            for j in range(len(self.frame.frame_buffer[i])):
                stdscr.addstr(i, j, str(self.frame.frame_buffer[i][j]))

        stdscr.refresh()

    def run(self, update):
        try:
            stdscr = curses.initscr()

            curses.noecho()
            curses.cbreak()

            stdscr.keypad(True)

            stdscr.nodelay(True)

            try:
                curses.start_color()
            except:
                pass

            color = self.Color()


            is_running = True
            prev_time = time.time()
            delta_time = time.time()
            while is_running:
                delta_time = time.time() - prev_time
                prev_time = time.time()

                self.event.update(stdscr)
                for event in self.event.get():
                    if event == 'q':
                        is_running = False
                        break
                update(self, delta_time)
                self.update(stdscr)
                self.render(stdscr)

        finally:
            if 'stdscr' in locals():
                stdscr.keypad(False)
                curses.echo()
                curses.nocbreak()
                curses.endwin()

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

        def __init__(self, frame):
            self.frame = frame
        def rect(self, x, y, width, height, color):
            for i in range(height):
                for j in range(width):
                    self.frame.set_pixel(x+j, y+i, color)
