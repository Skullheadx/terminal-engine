from terminalengine import TerminalEngine


def update(terminal_engine, dt):
    terminal_engine.draw.ellipse(10, 15, 10, 10, terminal_engine.color.BLUE)
    
    # NETHER PORTAL
    r = terminal_engine.Rect(3, 5, 10, 10, terminal_engine.color.MAGENTA)
    terminal_engine.draw.rect2(r, thickness=2)

    # CREEPER
    terminal_engine.draw.rect(25, 5, 11, 10, terminal_engine.color.GREEN)
    terminal_engine.draw.rect(27, 7, 2, 2, terminal_engine.color.BLACK)
    terminal_engine.draw.rect(32, 7, 2, 2, terminal_engine.color.BLACK)
    terminal_engine.draw.rect(29, 9, 3, 2, terminal_engine.color.BLACK)
    terminal_engine.draw.rect(27, 10, 3, 2, terminal_engine.color.BLACK)
    terminal_engine.draw.rect(29, 10, 3, 2, terminal_engine.color.BLACK)
    terminal_engine.draw.rect(32, 10, 2, 2, terminal_engine.color.BLACK)
    terminal_engine.draw.rect(27, 13, 2, 1, terminal_engine.color.BLACK)
    terminal_engine.draw.rect(32, 13, 2, 1, terminal_engine.color.BLACK)



    terminal_engine.draw.rect(15, 5, 10, 10, terminal_engine.color.RED)
    terminal_engine.draw.rect(13, 7, 2, 6, terminal_engine.color.RED)
    terminal_engine.draw.rect(21, 6, 4, 2, terminal_engine.color.WHITE)


def main():
    engine = TerminalEngine(update, 50, 25)


if __name__ == "__main__":
    main()
