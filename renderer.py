import os
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time


class Renderer:

    def __init__(self):
        self.stdscr = None  # set the screen to None

    def create_window(self,stdscr, width, height):
        self.stdscr = stdscr  # set the screen

        self.stdscr.clear()  # clear the screen
        curses.resize_term(height, width + 5)  # resize the screen
        self.stdscr.refresh()  # refresh the screen


    def render(self, grid):
        self.stdscr.clear()  # clear the screen
        # frame = "\n".join(["".join(tuple(map(str, i))) for i in grid.grid])  # create the frame
        for i in range(len(grid.grid)):
            for j in range(len(grid.grid[i])):
                self.stdscr.addstr(i, j, str(grid.grid[i][j]))
        self.stdscr.refresh()  # refresh the screen


