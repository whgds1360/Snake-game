from __future__ import annotations
from tkinter import Canvas
from entities.Food import Food
from entities.Snake import Snake
from utils.Move import Move
from PIL import Image, ImageTk
from pathlib import Path
from typing import Final, final, ClassVar


@final
class Game:
    # Константы и классовые переменные
    IMAGE_PATH: Final[Path] = Path("assets", "scenes", "BackGroundGame.jpg")

    # Размеры окна
    game_width: ClassVar[int]
    game_height: ClassVar[int]
    space_size: ClassVar[int]
    window_width: ClassVar[int]
    window_height: ClassVar[int]

    # Размеры поля в клетках
    game_width_in_cells: ClassVar[int]
    game_height_in_cells: ClassVar[int]

    # Отступы
    side_indent: ClassVar[int]
    vertical_indent: ClassVar[int]

    # Счет
    game_score: ClassVar[int]
    max_score: ClassVar[int]

    # Флаг для остановки игры
    game_active: ClassVar[bool] = True

    @classmethod
    def __initialize(cls, settings) -> None:
        """
        Инициализация размеров из настроек
        и просчет отступов и размеров в клетках
        """
        cls.window_width = settings.width
        cls.window_height = settings.height
        cls.game_width = settings.width_game_place
        cls.game_height = settings.height_game_place
        cls.space_size = settings.space_size
        cls.game_active = True
        cls.game_score = 0

        # Размеры в клетках
        cls.game_width_in_cells = cls.game_width // cls.space_size
        cls.game_height_in_cells = cls.game_height // cls.space_size

        # Максимальный счет
        cls.max_score = cls.game_width_in_cells * cls.game_height_in_cells - 3

        cls.side_indent = (cls.window_width - cls.game_width) // 2
        cls.vertical_indent = (cls.window_height - cls.game_height) // 2

    @classmethod
    def check_win(cls) -> bool:
        """
        Проверка условия победы
        """
        return cls.game_score >= cls.max_score

    @classmethod
    def check_lose(cls, snake) -> bool:
        """
        Проверка условия поражения
        """
        head_x, head_y = snake.coord[0]

        # Левая граница в пикселях
        left = cls.side_indent
        right = cls.side_indent + cls.game_width
        top = cls.vertical_indent
        bottom = cls.vertical_indent + cls.game_height

        # Проверка в пикселях
        if head_x < left or head_x >= right or head_y < top or head_y >= bottom:
            return True

        # Проверка столкновения с собственным телом
        if snake.check_self_collision():
            return True

        return False

    @classmethod
    def render_game_score(cls, canvas) -> None:
        # Игровой счет
        canvas.create_text(
            cls.side_indent + 95,  # X координата (слева с отступом)
            cls.vertical_indent - 20,  # Y координата (над игровым полем)
            text=f"SCORE: {cls.game_score}",
            fill="white",  # Цвет текста
            font=("Fixedsys", 34, "bold"),
            tag="score_text"  # Тег для возможности удаления/обновления
        )

    @classmethod
    def update_score(cls, canvas, food) -> None:
        """
        Обновляет счет игры
        """
        cls.game_score = food.eat_count


        # Удаляем старый текст счета, если он есть
        canvas.delete("score_text")

        cls.render_game_score(canvas=canvas)

    @classmethod
    def game_rendering(cls, window, settings) -> None:
        """
        Рендер самой игры
        """
        cls.__initialize(settings)

        # Загружаем изображение
        image = Image.open(cls.IMAGE_PATH)
        image = image.resize(
            (settings.width, settings.height), Image.Resampling.LANCZOS
        )
        background_image_game = ImageTk.PhotoImage(image)

        # Создаем холст (Игровое поле)
        canvas = Canvas(
            master=window, width=settings.width, height=settings.height, bg="black"
        )
        canvas.pack()

        canvas.create_image(
            0, 0, image=background_image_game, anchor="nw", tag="background"
        )
        canvas.background_image = background_image_game

        # Отрисовка змеи
        snake = Snake(canvas=canvas, settings=settings)

        # Отрисовка еды
        food = Food(canvas=canvas, settings=settings, snake=snake)

        # Привязка обработчика к основному окну
        window.bind(sequence="<Key>", func=Move.button_handler)

        # Рендеринг рамки игрового поля
        cls.game_place_rendering(canvas=canvas, settings=settings)


        # Игровой счет
        cls.render_game_score(canvas=canvas)

        # Запускаем игровой цикл
        cls.__game_loop(
            window=window, canvas=canvas, snake=snake, settings=settings, food=food
        )

    @classmethod
    def __game_loop(cls, window, canvas, snake, settings, food) -> None:
        """
        Игровой цикл с проверкой победы/поражения
        """
        from scenes.LoseScreen import LoseScreen
        from scenes.WinScreen import WinScreen

        # Проверка поражения
        if cls.check_lose(snake):
            cls.game_active = False

            # Удаляем все виджеты
            for widget in window.winfo_children():
                widget.destroy()

            LoseScreen.screen_rendering(window=window, settings=settings)
            return

        # Движение змеи
        direction: str = Move.current_direction
        Move.draw_new_segment(
            canvas=canvas, snake=snake, direction=direction, settings=settings
        )

        # Проверка съедения еды
        if snake.coord[0] == food.coord[0]:
            del food.coord[-1]
            canvas.delete(food.squares[-1])
            del food.squares[-1]

            food.spawn_food(snake=snake)
            food.eat_count += 1
            cls.update_score(canvas=canvas, food=food)

            # Проверка победы
            if cls.check_win():
                cls.game_active = False
                WinScreen.screen_rendering(window=window, settings=settings)
                return
        else:
            # Не съели - удаляем хвост
            del snake.coord[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]

        # Продолжаем цикл
        if cls.game_active:
            window.after(
                settings.delay, cls.__game_loop, window, canvas, snake, settings, food
            )

    @classmethod
    def game_place_rendering(cls, canvas, settings) -> None:
        """
        Отрисовка рамок игрового поля
        """
        canvas.create_rectangle(
            cls.side_indent,
            cls.vertical_indent,
            cls.game_width + cls.side_indent,
            cls.game_height + cls.vertical_indent,
            outline=settings.color_field_game_place,
            width=3,
        )
