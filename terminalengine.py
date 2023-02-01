import curses
import time
import random
import sys
import os
import math
import threading


class TerminalEngine:

    def __init__(self):
        pass

    def update(self, stdscr):
        stdscr.clear()

    def render(self, stdscr):
        stdscr.addstr(0, 0, "Hello World!")

        stdscr.refresh()

    def run(self, update):
        try:
            stdscr = curses.initscr()

            curses.noecho()
            curses.cbreak()

            stdscr.keypad(True)

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
                update(delta_time)
                self.update(stdscr)
                self.render(stdscr)

        finally:
            if 'stdscr' in locals():
                stdscr.keypad(False)
                curses.echo()
                curses.nocbreak()
                curses.endwin()
