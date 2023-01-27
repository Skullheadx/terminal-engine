import pynput.keyboard as keyboard

from grid import Grid
from renderer import Renderer


class TerminalEngine:
    def __init__(self):
        self.grid = Grid()
        self.renderer = Renderer()
        self.renderer.render(self.grid)

    def update(self):
        self.renderer.render(self.grid)
        self.grid.update()

    class Event:
        events = []
        keys = {}

        KEYDOWN = 0
        KEYUP = 1
        QUIT = 2

        def on_press(self, key):
            if key not in self.keys:
                self.keys[key] = False
            if self.keys[key]:
                return
            self.keys[key] = True

            if key == keyboard.Key.esc:
                self.events.append((self.QUIT, None))
            else:
                self.events.append((self.KEYDOWN, key))

        def on_release(self, key):
            if not self.keys[key]:
                return
            self.keys[key] = False
            self.events.append((self.KEYUP, key))

        def __init__(self):
            listener = keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release)
            listener.start()

        def get(self):
            output = self.events.copy()
            self.events.clear()
            return output
