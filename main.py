from terminalengine import TerminalEngine



class Game:
    def __init__(self):
        self.engine = TerminalEngine(50, 25)
        self.time = 0
        self.engine.run(self.update)


    def update(self, terminal_engine, dt):
        terminal_engine.draw.ellipse(10, 15, 10, 10, terminal_engine.color.BLUE)

        # NETHER PORTAL
        r = terminal_engine.Rect(3, 5, 10, 10, terminal_engine.color.MAGENTA)
        terminal_engine.draw.rect2(r, thickness=2)

        # CREEPER
        terminal_engine.draw.rect(25, 5, 10, 10, terminal_engine.color.GREEN)
        terminal_engine.draw.rect(27, -1 + 7, 2, 2 , terminal_engine.color.BLACK)
        terminal_engine.draw.rect(31, -1 + 7, 2, 2 , terminal_engine.color.BLACK)
        terminal_engine.draw.rect(29, -1 + 9, 2, 2 , terminal_engine.color.BLACK)
        terminal_engine.draw.rect(27, -1 + 10, 2, 2 +1 , terminal_engine.color.BLACK)
        terminal_engine.draw.rect(29, -1 + 10, 2, 2 +1 , terminal_engine.color.BLACK)
        terminal_engine.draw.rect(31, -1 + 10, 2, 2 +1, terminal_engine.color.BLACK)
        terminal_engine.draw.rect(27, -1 + 11, 2, 2 + 1 , terminal_engine.color.BLACK)
        terminal_engine.draw.rect(31, -1 + 11, 2, 2   + 1, terminal_engine.color.BLACK)

        for event in terminal_engine.event.get():
            if event == "s":
                self.time = 250


        if self.time > 0:
            # SUS
            terminal_engine.draw.rect(15, 5, 10, 10, terminal_engine.color.RED)
            terminal_engine.draw.rect(13, 7, 2, 6, terminal_engine.color.RED)
            terminal_engine.draw.rect(21, 6, 4, 2, terminal_engine.color.WHITE)
            terminal_engine.draw.rect(19, 12, 2, 4, terminal_engine.color.WHITE)
            self.time -= dt





def main():
    game = Game()



if __name__ == "__main__":
    main()
