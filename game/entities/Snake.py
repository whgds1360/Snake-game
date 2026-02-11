class Snake:
    def __init__(self, canvas, settings)->None:
        #Для выравнивания змейки по центру окна (уже адаптивно)
        width = settings.width // 2
        height = settings.height // 2

        self.canvas = canvas
        self.coord = [[width, height],
                      [width, height],
                      [width, height]]
        self.squares = []

        for x, y in self.coord:
            square = canvas.create_rectangle(x, y, x+settings.space_size, y+settings.space_size, fill=settings.snake_color)
            self.squares.append(square)
