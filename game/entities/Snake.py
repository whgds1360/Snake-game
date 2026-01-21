from game.utils.ResourseManager import Resourses

class Snake:
    def __init__(self, canvas):
        Resourses.from_config_file()

        self.canvas = canvas
        self.coord = [[0, 0],
                      [0, 0],
                      [0, 0]]
        self.squares = []

        for x, y in self.coord:
            square = canvas.create_rectangle(x, y, x+Resourses.space_size, y+Resourses.space_size, fill='green')
            self.squares.append(square)
