from terminalengine import TerminalEngine


def update(terminal_engine, dt):
    r = terminal_engine.Rect(10, 5, 10, 10, terminal_engine.color.GREEN)
    terminal_engine.draw.rect2(r, thickness=2)
    terminal_engine.draw.rect(25, 5, 10, 10, terminal_engine.color.GREEN)
    terminal_engine.draw.line(0, 0, 50, 25, terminal_engine.color.RED)
    #
    # terminal_engine.draw.rect(10, 2, 10, 10, terminal_engine.color.RED)
    # terminal_engine.draw.rect(8, 4, 2, 6, terminal_engine.color.RED)
    # terminal_engine.draw.rect(16, 3, 4, 2, terminal_engine.color.WHITE)


def main():
    engine = TerminalEngine(update, 50, 25)


if __name__ == "__main__":
    main()
