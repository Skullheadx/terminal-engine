from engine import Engine
import time


def main():
    engine = Engine()

    is_running = True

    while is_running:
        engine.update()
        time.sleep(0.1)


if __name__ == "__main__":
    main()
