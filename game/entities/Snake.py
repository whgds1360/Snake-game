from typing import List, final


@final
class Snake:
    def __init__(self, canvas, settings)->None:
        #Для выравнивания змейки по центру окна (уже адаптивно)
        width:int = settings.width // 2
        height:int = settings.height // 2

        self.canvas = canvas
        self.coord:List[List] = [[width, height],
                      [width, height],
                      [width, height]]
        self.squares:List = []

        for x, y in self.coord:
            square = canvas.create_rectangle(x, y, x+settings.space_size, y+settings.space_size, fill=settings.snake_color)
            self.squares.append(square)
