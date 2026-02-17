from __future__ import annotations
from tkinter import Canvas
from game.entities.Food import Food
from game.entities.Snake import Snake
from game.utils.Move import Move
from PIL import Image, ImageTk
from pathlib import Path
from typing import Final, final


@final
class Game:
    # Путь до картинки
    IMAGE_PATH: Final[Path] = Path("assets", "scenes", "BackGroundGame.jpg")


    @classmethod
    def game_rendering(cls, window, settings)->None:
        """
        Рендер самой игры
        """
        # Загружаем изображение
        image = Image.open(cls.IMAGE_PATH)
        # Изменяем размер под холст
        image = image.resize((settings.width, settings.height), Image.Resampling.LANCZOS)
        background_image_game = ImageTk.PhotoImage(image)

        # Создаем холст (Игровое поле)
        canvas = Canvas(
            master=window,
            width=settings.width,
            height=settings.height,
            bg="black"  #Временный фон
        )
        canvas.pack()

        canvas.create_image(0, 0, image=background_image_game, anchor="nw", tag="background")

        canvas.background_image = background_image_game

        # Отрисовка змеи
        snake: Snake = Snake(canvas=canvas, settings=settings)

        # Отрисовка еды
        food: Food = Food(canvas=canvas, settings=settings, snake=snake)

        # Привязка обработчика к основному окну
        window.bind(sequence="<Key>", func=Move.button_handler)

        # Движение змеи
        Move.move(window=window, canvas=canvas, snake=snake, settings=settings, food=food)

        canvas.create_rectangle(192, 96, #TODO условная сетка потом убери
                                832, 736,
                                outline="pink",
                                width=3
                                )
