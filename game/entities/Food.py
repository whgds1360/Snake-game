from typing import final, List
from random import randint


@final
class Food:
    def __init__(self, canvas, settings, snake) -> None:
        self.width: int = settings.width
        self.height: int = settings.height

        self.space_size: int = settings.space_size
        self.canvas = canvas
        self.food_color = settings.food_color

        #Игровой счет
        self.eat_count = 0

        # Список координат еды
        self.coord: List[List[int]] = []
        # Список ID объектов на canvas
        self.squares: List[int] = []
        # Создаем первую еду
        self.spawn_food(snake=snake)


    def spawn_food(self, snake) -> None:
        """
        Создает новую еду в случайном месте
        """
        x = randint(0, (self.width // self.space_size - 1)) * self.space_size
        y = randint(0, (self.height // self.space_size - 1)) * self.space_size

        # Проверка, что еда не появляется ни на одной части змейки
        while [x, y] in snake.coord:  # проверяем все координаты змейки
            x = randint(0, (self.width // self.space_size - 1)) * self.space_size
            y = randint(0, (self.height // self.space_size - 1)) * self.space_size

        self.coord.append([x, y])

        square = self.canvas.create_rectangle(
            x, y,
            x + self.space_size,
            y + self.space_size,
            fill=self.food_color
        )
        self.squares.append(square)
