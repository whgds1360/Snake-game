from game.utils.ResourseManager import Resourses


def move(window, canvas, snake, food, direction: str) -> None:
    # Получаем текущие координаты головы
    x, y = snake.coord[0]

    # Обновляем координаты в зависимости от направления
    if direction == 'down':
        y += Resourses.space_size or 20
    elif direction == 'up':
        y -= Resourses.space_size or 20
    elif direction == 'left':
        x -= Resourses.space_size or 20
    elif direction == 'right':
        x += Resourses.space_size or 20

    # Добавляем новую голову
    snake.coord.insert(0, [x, y])

    # Рисуем новый сегмент
    square = canvas.create_rectangle(
        x, y,
        x + Resourses.space_size,
        y + Resourses.space_size,
        fill="green"
    )
    snake.squares.insert(0, square)

    # Удаляем хвост
    del snake.coord[-1]
    canvas.delete(snake.squares[-1])
    del snake.squares[-1]

    #Задержка игры
    window.after(100, move, window, canvas, snake, food, direction)
