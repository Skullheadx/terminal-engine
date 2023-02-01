from terminalengine import TerminalEngine


def update(terminal_engine, dt):
    terminal_engine.draw.rect(10, 2, 10, 10, terminal_engine.color.RED)
    terminal_engine.draw.rect(8, 4, 2, 6, terminal_engine.color.RED)
    terminal_engine.draw.rect(16, 3, 4, 2, terminal_engine.color.WHITE)


def main():
    engine = TerminalEngine(update)


if __name__ == "__main__":
    main()
