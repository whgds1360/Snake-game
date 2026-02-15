from typing import final, List
from random import randint


@final
class Food:
    def __init__(self, canvas, settings) -> None:
        self.width: int = settings.width
        self.height: int = settings.height
        self.space_size: int = settings.space_size
        self.canvas = canvas
        self.settings = settings

        # Список координат еды
        self.coord: List[List[int]] = []
        # Список ID объектов на canvas
        self.squares: List[int] = []

        # Создаем первую еду
        self.spawn_food()


    def spawn_food(self) -> None:
        """
        Создает новую еду в случайном месте
        """
        x = randint(0, (self.width // self.space_size)) * self.space_size
        y = randint(0, (self.height // self.space_size)) * self.space_size

        self.coord.append([x, y])

        square = self.canvas.create_rectangle(
            x, y,
            x + self.space_size,
            y + self.space_size,
            fill=self.settings.food_color
        )
        self.squares.append(square)
