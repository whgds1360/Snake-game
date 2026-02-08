from game.utils.ResourseManager import Resourses
from typing import Optional


class Move:

    current_direction:Optional[str] = 'Down'

    @classmethod
    def button_handler(cls, event) -> None:
        """
        Метод меняет направление змеи взависимости от нажатой кнопки
        """
        #Отладочная печать
        print(f'Нажата клавиша: {event.keysym}')


        if event.keysym == 'Right':
            cls.current_direction = 'Right'
        elif event.keysym == 'Left':
            cls.current_direction = 'Left'
        elif event.keysym == 'Up':
            cls.current_direction = 'Up'
        elif event.keysym == 'Down':
            cls.current_direction = 'Down'



    @classmethod
    def move(cls, window, canvas, snake) -> None:
        """
        Основной метод движения змеи
        """
        direction = cls.current_direction

        # Получаем текущие координаты головы
        x, y = snake.coord[0]

        # Обновляем координаты в зависимости от направления
        if direction == 'Down':
            y += Resourses.space_size
        elif direction == 'Up':
            y -= Resourses.space_size
        elif direction == 'Left':
            x -= Resourses.space_size
        elif direction == 'Right':
            x += Resourses.space_size

        snake.coord.insert(0, [x, y])

        # Рисуем новый сегмент
        square = canvas.create_rectangle(
            x, y,
            x + Resourses.space_size,
            y + Resourses.space_size,
            fill="green" #убрать литерал
        )
        snake.squares.insert(0, square)

        # Удаляем хвост
        del snake.coord[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

        window.after(200, Move.move, window, canvas, snake) #переделать без литерала