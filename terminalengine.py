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