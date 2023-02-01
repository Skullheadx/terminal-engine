from terminalengine import TerminalEngine


def update(terminal_engine, dt):
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

    # SUS
    terminal_engine.draw.rect(15, 5, 10, 10, terminal_engine.color.RED)
    terminal_engine.draw.rect(13, 7, 2, 6, terminal_engine.color.RED)
    terminal_engine.draw.rect(21, 6, 4, 2, terminal_engine.color.WHITE)
    terminal_engine.draw.rect(19, 12, 2, 4, terminal_engine.color.WHITE)


def main():
    engine = TerminalEngine(update, 50, 25)


if __name__ == "__main__":
    main()
