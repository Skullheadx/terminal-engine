import time

from engine import Engine


def main():
    engine = Engine()

    is_running = True

    while is_running:
        for event, key in engine.Event().get():
            if event == engine.Event.QUIT:
                is_running = False
                break

        engine.update()
        time.sleep(0.1)


if __name__ == "__main__":
    main()
