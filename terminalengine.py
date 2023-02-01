import curses
import time
import random
import sys
import os
import math
import threading


class TerminalEngine:

    def __init__(self):
        self.event = self.Event()

    def update(self, stdscr):
        # stdscr.clear()
        pass

    def render(self, stdscr):
        stdscr.addstr(0, 0, "Hello World!")

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
                    stdscr.addstr(2, 0, event)
                    stdscr.refresh()
                    if event == 'q':
                        stdscr.addstr(1, 0, "Quitting... ")
                        stdscr.refresh()
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