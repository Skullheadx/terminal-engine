from terminalengine import TerminalEngine


class Game:
    def __init__(self):
        self.engine = TerminalEngine(50, 25)
        self.time = 0
        self.p = Player(self.engine, 10, 10)
        self.img = self.engine.Image("Untitled.png")
        self.img.resize(15, 15)
        
        self.engine.run(self.update)
    def update(self, tengine, dt):
        test = tengine.LargeText("abcdefghij")
        test.draw(tengine, 0, 0, tengine.color.RED)
        test2 = tengine.LargeText("klmnopqrst")
        test2.draw(tengine, 0, 8, tengine.color.BLUE)
        test3 = tengine.LargeText("uvwxyz")
        test3.draw(tengine, 0, 16, tengine.color.GREEN)

        tengine.draw.ellipse(10, 15, 10, 10, tengine.color.BLUE)

        # NETHER PORTAL
        r = tengine.Rect(3, 5, 10, 10, tengine.color.MAGENTA)
        tengine.draw.rect2(r, thickness=2)

        # CREEPER
        tengine.draw.rect(25, 5, 10, 10, tengine.color.GREEN)
        tengine.draw.rect(27, -1 + 7, 2, 2, tengine.color.BLACK)
        tengine.draw.rect(31, -1 + 7, 2, 2, tengine.color.BLACK)
        tengine.draw.rect(29, -1 + 9, 2, 2, tengine.color.BLACK)
        tengine.draw.rect(27, -1 + 10, 2, 2 + 1, tengine.color.BLACK)
        tengine.draw.rect(29, -1 + 10, 2, 2 + 1, tengine.color.BLACK)
        tengine.draw.rect(31, -1 + 10, 2, 2 + 1, tengine.color.BLACK)
        tengine.draw.rect(27, -1 + 11, 2, 2 + 1, tengine.color.BLACK)
        tengine.draw.rect(31, -1 + 11, 2, 2 + 1, tengine.color.BLACK)

        for event in tengine.event.get(key='s', clear=False):
            if event == "s":
                self.time = 250

        if self.time > 0:
            # SUS
            tengine.draw.rect(15, 5, 10, 10, tengine.color.RED)
            tengine.draw.rect(13, 7, 2, 6, tengine.color.RED)
            tengine.draw.rect(21, 6, 4, 2, tengine.color.WHITE)
            tengine.draw.rect(19, 12, 2, 4, tengine.color.WHITE)
            self.time -= dt

        r2 = tengine.CollisionRect(37, 5, 10, 10, tengine.color.MAGENTA, collision_layer=0)
        tengine.draw.rect2(r2)

        self.p.update(tengine, dt)
        self.p.draw(tengine)


        self.img.draw(tengine, 15, 15)



class Player:

    def __init__(self, tengine, x, y):
        self.player = tengine.Sprite(x, y, 5, 5, tengine.Color.YELLOW)

    def update(self, tengine, dt):
        for event in tengine.event.get():
            if event == "w":
                self.player.move(0, -1)
            elif event == "a":
                self.player.move(-1, 0)
            elif event == "s":
                self.player.move(0, 1)
            elif event == "d":
                self.player.move(1, 0)

    def draw(self, tengine):
        self.player.draw(tengine)
