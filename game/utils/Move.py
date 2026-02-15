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


    @classmethod
    def check_eating(cls, snake, food) -> bool:
        """
        Метод проверяет съедена ли еда
        """
        return snake.coord[0] == food.coord[0]


    @classmethod
    def move(cls, window, canvas, snake, settings, food) -> None:
        """
        Основной метод движения змеи, который занимается отрисовкой новых сегментов
        """
        direction:str = cls.current_direction

        snake.draw_new_segment(canvas=canvas, snake=snake, direction=direction, settings=settings)

        if not cls.check_eating(snake, food):
            del snake.coord[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]

        else:
            del food.coord[-1]
            canvas.delete(food.squares[-1])
            del food.squares[-1]
            # Рисуем новую еду
            food.spawn_food()

            #Добавляем в счетчик отрисованную еду
            food.eat_count += 1

            # Отладочная печать
            print(f"Съедено: {food.eat_count}")

        window.after(settings.delay, Move.move, window, canvas, snake, settings, food)
