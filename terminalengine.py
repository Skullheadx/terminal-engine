import curses
import time
import random
import sys
import os
import math
import threading

from framebuffer import FrameBuffer

class TerminalEngine:

    def __init__(self, width=80, height=24):
        self.event = self.Event()
        terminal_size = [os.get_terminal_size().columns, os.get_terminal_size().lines-1]
        self.frame = FrameBuffer(terminal_size[0], terminal_size[1])

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
                update(delta_time)
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
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(7, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(8, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

        RED = curses.color_pair(1)
        GREEN = curses.color_pair(2)
        YELLOW = curses.color_pair(3)
        BLUE = curses.color_pair(4)
        WHITE = curses.color_pair(5)
        BLACK = curses.color_pair(6)
        CYAN = curses.color_pair(7)
        MAGENTA = curses.color_pair(8)
