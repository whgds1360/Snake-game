from typing import Optional, ClassVar, final


@final
class Move:

    current_direction:ClassVar[Optional[str]] = "Down"

    @classmethod
    def button_handler(cls, event) -> None:
        """
        Метод меняет направление змеи в зависимости от нажатой кнопки
        """
        #Отладочная печать
        print(f"Нажата клавиша: {event.keysym}")

        if event.keysym == "Right":
            cls.current_direction = "Right"
        elif event.keysym == "Left":
            cls.current_direction = "Left"
        elif event.keysym == "Up":
            cls.current_direction = "Up"
        elif event.keysym == "Down":
            cls.current_direction = "Down"


    @classmethod
    def move(cls, window, canvas, snake, settings) -> None:
        """
        Основной метод движения змеи, который занимается отрисовкой новых сегментов
        """
        direction:Optional[str] = cls.current_direction

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

        snake.coord.insert(0, [x, y])

        # Рисуем новый сегмент
        square = canvas.create_rectangle(
            x, y,
            x + settings.space_size,
            y + settings.space_size,
            fill=settings.snake_color
        )
        snake.squares.insert(0, square)

        # Удаляем хвост
        del snake.coord[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

        window.after(settings.delay, Move.move, window, canvas, snake, settings)
