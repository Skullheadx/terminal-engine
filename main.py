import time

from terminalengine import TerminalEngine


def main():  # main function
    window = TerminalEngine()  # create the window

    is_running = True
    while is_running:  # main loop
        for event, key in window.event.get():  # event loop
            if event == window.Event.QUIT:  # quit event
                is_running = False  # quit
                break

        window.update()  # update the window
        time.sleep(0.1)  # sleep for 0.1 seconds


if __name__ == "__main__":  # if the file is being run directly
    main()  # run the main function
