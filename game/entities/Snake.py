from game.utils.ResourseManager import Resourses

class Snake:
    def __init__(self, canvas):
        Resourses.from_config_file()

        #Для выравнивания змейки по центру окна (уже адаптивно)
        width = Resourses.width // 2
        height = Resourses.height // 2

        self.canvas = canvas
        self.coord = [[width, height],
                      [width, height],
                      [width, height]]
        self.squares = []

        for x, y in self.coord:
            square = canvas.create_rectangle(x, y, x+Resourses.space_size, y+Resourses.space_size, fill='green')
            self.squares.append(square)
