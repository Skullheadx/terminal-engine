from grid import Grid
from renderer import Renderer


class Engine:
    def __init__(self):
        self.grid = Grid()
        self.renderer = Renderer()
        self.renderer.render(self.grid)

    def update(self):
        self.renderer.render(self.grid)
        self.grid.update()

