import time

from terminalengine import TerminalEngine


def main():
    window = TerminalEngine()

    is_running = True

    while is_running:
        for event, key in window.Event().get():
            if event == window.Event.QUIT:
                is_running = False
                break

        window.update()
        time.sleep(0.1)


if __name__ == "__main__":
    main()
