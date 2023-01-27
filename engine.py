from grid import Grid
from renderer import Renderer
import time


class Engine:
    def __init__(self):
        self.grid = Grid()
        self.renderer = Renderer()
        self.renderer.render(self.grid)

    def run(self):
        while True:
            self.renderer.render(self.grid)
            self.grid.update()
            time.sleep(1)

