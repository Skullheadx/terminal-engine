from terminalengine import TerminalEngine


def update(terminal_engine, dt):
    terminal_engine.draw.rect(10, 2, 10, 10, terminal_engine.color.RED)


def main():
    engine = TerminalEngine(update)


if __name__ == "__main__":
    main()
