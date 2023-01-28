import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time


def main(stdscr):



if __name__ == "__main__":
    wrapper(main)


    # # stdscr.clear()
    # curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    # curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    # curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    # RED_AND_BLACK = curses.color_pair(1)
    # YELLOW_AND_BLACK = curses.color_pair(2) | curses.A_BOLD
    # GREEN_AND_BLACK = curses.color_pair(3) | curses.A_BOLD
    #
    # # curses.echo()
    #
    # # width, height = stdscr.getmaxyx()
    # # stdscr.addstr(0, 0, f"width: {width}, height: {height}", RED_AND_BLACK)
    # # stdscr.refresh()
    #
    # stdscr.attron(GREEN_AND_BLACK)
    # stdscr.border()
    # stdscr.attroff(GREEN_AND_BLACK)
    #
    # win = curses.newwin(3, 18, 2, 2)
    # box = Textbox(win)
    #
    # stdscr.attron(YELLOW_AND_BLACK)
    # rectangle(stdscr, 1, 1 , 5, 20)
    # stdscr.attroff(YELLOW_AND_BLACK)
    #
    # stdscr.move(0,0)
    #
    # stdscr.refresh()
    #
    # box.edit()
    # text = box.gather().strip().replace("\n", "")
    #
    # stdscr.addstr(6, 2, text, RED_AND_BLACK)
    #
    # while True:
    #     key = stdscr.getkey()
    #     if key == "q":
    #         break

    
    # stdscr.nodelay(True)
    #
    # x, y = 0, 0
    # string_x = 0
    # while True:
    #     try:
    #         key = stdscr.getkey()
    #     except:
    #         key = None
    #     if key == "KEY_LEFT":
    #         x -= 1
    #     elif key == "KEY_RIGHT":
    #         x += 1
    #     elif key == "KEY_UP":
    #         y -= 1
    #     elif key == "KEY_DOWN":
    #         y += 1
    #
    #     stdscr.clear()
    #     string_x += 1
    #     stdscr.addstr(0, string_x // 50, f"x: {x}, y: {y}", RED_AND_BLACK)
    #     stdscr.addstr(y, x, "0")
    #     stdscr.refresh()

    #

    # pad = curses.newpad(100, 100)
    # stdscr.refresh()
    #
    # for i in range(100):
    #     for j in range(26):
    #         char = chr(65 + j)
    #         pad.addstr(char, RED_AND_BLACK)
    # for i in range(50):
    #     # pad.refresh(0, i, 5, 5, 10, 25)
    #     stdscr.clear()
    #     stdscr.refresh()
    #     pad.refresh(0, i, 5, i, 10, 25 + i)
    #     time.sleep(0.2)

# stdscr.clear()
# stdscr.addstr(0, 5, "Hello world", RED_AND_BLACK) # this line is printed
# stdscr.addstr(1, 5, "mE IS gOOd? rIghT cOPiLot?", YELLOW_AND_BLACK) # this line is printed
# stdscr.addstr(2, 5, "I am a good programmer", GREEN_AND_BLACK) # this line is not printed
# stdscr.refresh()


# counter_win = curses.newwin(1, 20,  10, 10)
# stdscr.addstr(0, 0, "Hello world", RED_AND_BLACK)            # this line is printed
# stdscr.refresh()
#
# for i in range(100):
#     counter_win.clear()
#     colour = RED_AND_BLACK
#
#     if i % 2 == 0:
#         colour = GREEN_AND_BLACK
#
#     counter_win.addstr(0, 0, f"count {i}", colour)            # this line is printed
#     counter_win.refresh()
#     time.sleep(0.1)
