import pynput.keyboard as keyboard

from grid import Grid
from renderer import Renderer


class TerminalEngine:
    def __init__(self):
        self.grid = Grid()  # create the grid
        self.renderer = Renderer()  # create the renderer
        self.event = self.Event()  # create the event handler

    def update(self):  # update the grid and render it
        self.renderer.render(self.grid)
        self.grid.update()

    class Event:  # event handler
        events = []  # list of events
        keys = {}  # dictionary of keys

        # Key Codes
        KEYDOWN = 0  # keydown event
        KEYUP = 1  # keyup event
        QUIT = 2  # quit event

        def on_press(self, key):
            if key not in self.keys:  # if the key is not in the keys list, add it
                self.keys[key] = False

            if self.keys[key]:  # if the key is already pressed, return
                return
            self.keys[key] = True  # set the key to pressed

            if key == keyboard.Key.esc:  # if the key is the escape key, add the quit event to the events list
                self.events.append((self.QUIT, None))
            else:  # otherwise, add the keydown event to the events list
                self.events.append((self.KEYDOWN, key))

        def on_release(self, key):
            if not self.keys[key]:  # if the key is not pressed, return
                return
            self.keys[key] = False  # set the key to not pressed
            self.events.append((self.KEYUP, key))  # add the keyup event to the events list

        def __init__(self):
            self.listener = keyboard.Listener(  # create the listener
                on_press=self.on_press,
                on_release=self.on_release)  # set the listener to use the on_press and on_release functions
            self.listener.start()  # start the listener

        def get(self):
            output = self.events.copy()  # copy the events
            self.events.clear()  # clear the events
            return output  # return the events

        def __del__(self):  # destructor
            self.listener.stop()  # stop the listener
