from typing import List, final


@final
class Snake:
    def __init__(self, canvas, settings)->None:
        #Для выравнивания змейки по центру окна
        width:int = settings.width // 2
        height:int = settings.height // 2

        self.coord:List[List] = [[width, height],
                      [width, height],
                      [width, height]]
        self.squares:List = []

        for x, y in self.coord:
            square = canvas.create_rectangle(
                x, y,
                x+settings.space_size,
                y+settings.space_size,
                fill=settings.snake_color,
                outline="green",
                width = 3
            )

            self.squares.append(square)


    def draw_new_segment(self, canvas, snake, direction, settings) -> None:
        """
        Рисует новый сегмент змеи
        """
        # Получаем текущие координаты головы
        x, y = self.coord[0]

        # Обновляем координаты в зависимости от направления
        if direction == "Down":
            y += settings.space_size
        elif direction == "Up":
            y -= settings.space_size
        elif direction == "Left":
            x -= settings.space_size
        elif direction == "Right":
            x += settings.space_size

        # Вставляем новые координаты головы в начало списка
        self.coord.insert(0, [x, y])

        # Рисуем новый сегмент головы
        snake_square = canvas.create_rectangle(
            x, y,
            x + settings.space_size,
            y + settings.space_size,
            fill=settings.snake_color,
            outline="green",
            width=3
        )

        # Вставляем новый сегмент в начало списка squares
        snake.squares.insert(0, snake_square)
