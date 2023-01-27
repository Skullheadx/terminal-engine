import os


class Renderer:

    def __init__(self):
        pass

    def render(self, grid):
        self.clear()  # clear the screen

        frame = "\n".join(["".join(tuple(map(str, i))) for i in grid.grid])  # create the frame
        print(frame, end='\r')  # print the frame

        # old code
        # for i in range(grid.screen_height):
        #     for j in range(grid.screen_width):
        #         print(grid.grid[i][j], end='')
        #     print()

    @staticmethod
    def clear():  # clear the screen (works on windows and linux)
        os.system('cls' if os.name == 'nt' else 'clear')  # clear the screen
