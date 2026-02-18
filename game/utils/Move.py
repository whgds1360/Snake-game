from typing import ClassVar, final


@final
class Move:

    current_direction: ClassVar[str] = "Right"

    @classmethod
    def button_handler(cls, event) -> None:
        """
        Метод меняет направление змеи в зависимости от нажатой кнопки
        """
        # Отладочная печать
        print(f"Нажата клавиша: {event.keysym}")

        if event.keysym == "Right":
            if cls.current_direction == "Left":
                pass
            else:
                cls.current_direction = "Right"

        elif event.keysym == "Left":
            if cls.current_direction == "Right":
                pass
            else:
                cls.current_direction = "Left"

        elif event.keysym == "Up":
            if cls.current_direction == "Down":
                pass
            else:
                cls.current_direction = "Up"

        elif event.keysym == "Down":
            if cls.current_direction == "Up":
                pass
            else:
                cls.current_direction = "Down"

    @staticmethod
    def draw_new_segment(canvas, snake, direction, settings) -> None:
        """
        Рисует новый сегмент змеи
        """
        # Получаем текущие координаты головы
        x, y = snake.coord[0]

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
        snake.coord.insert(0, [x, y])

        # Рисуем новый сегмент головы
        snake_square = canvas.create_rectangle(
            x,
            y,
            x + settings.space_size,
            y + settings.space_size,
            fill=settings.snake_color,
        )

        # Вставляем новый сегмент в начало списка squares
        snake.squares.insert(0, snake_square)
