from typing import final, List
from random import randint


@final
class Food:
    def __init__(self, canvas, settings, snake) -> None:
        self.width: int = settings.width
        self.height: int = settings.height

        self.space_size: int = settings.space_size
        self.canvas = canvas
        self.food_color: str = settings.food_color

        # Игровой счет
        self.eat_count: int = 0

        # Список координат еды
        self.coord: List[List[int]] = []
        # Список ID объектов на canvas
        self.squares: List[int] = []
        # Создаем первую еду
        self.spawn_food(snake=snake)

    def spawn_food(self, snake) -> None:
        """
        Создает новую еду в случайном месте внутри игрового поля
        """
        from scenes.Game import Game

        # Границы игрового поля в ПИКСЕЛЯХ
        left = Game.side_indent  # левая граница (например 192)
        right = Game.side_indent + Game.game_width  # правая граница (192 + 640 = 832)
        top = Game.vertical_indent  # верхняя граница (например 64)
        bottom = (
            Game.vertical_indent + Game.game_height
        )  # нижняя граница (64 + 640 = 704)

        while True:
            # Генерируем координаты ТОЛЬКО внутри игрового поля
            x = randint(left, right - self.space_size)  # от 192 до 800
            y = randint(top, bottom - self.space_size)  # от 64 до 672

            # Выравниваем по сетке!
            x = (x - left) // self.space_size * self.space_size + left
            y = (y - top) // self.space_size * self.space_size + top

            # Проверяем, не занята ли клетка змеей
            if [x, y] not in snake.coord:
                break

        # Удаление старой еду
        if self.coord:
            self.canvas.delete(self.squares[-1])
            self.coord.clear()
            self.squares.clear()

        # Добавление новой еду
        self.coord.append([x, y])

        square = self.canvas.create_rectangle(
            x, y, x + self.space_size, y + self.space_size, fill=self.food_color
        )
        self.squares.append(square)
