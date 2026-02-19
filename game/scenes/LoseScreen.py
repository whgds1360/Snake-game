from __future__ import annotations
from tkinter import Canvas, Button
from PIL import Image, ImageTk
from pathlib import Path
from typing import Final, final, ClassVar
from scenes.Menu import Menu


@final
class LoseScreen(Menu):
    # Пути к изображениям
    IMAGE_LOSE_SCREEN: Final[Path] = Path("assets", "scenes", "LoseScreen.jpg")
    IMAGE_TRY_AGAIN: Final[Path] = Path("assets", "scenes", "TryAgain.png")

    ready_lose_button_image: ClassVar

    @classmethod
    def screen_rendering(cls, window, settings) -> None:
        """
        Метод просто отрисовывает меню с кнопками
        """
        # Загружаем фоновое изображение
        lose_screen_image = Image.open(cls.IMAGE_LOSE_SCREEN)
        lose_screen_image = lose_screen_image.resize((settings.width, settings.height))
        lose_screen_image = ImageTk.PhotoImage(lose_screen_image)

        # Загружаем изображения кнопок
        lose_button_image = Image.open(cls.IMAGE_TRY_AGAIN)
        lose_button_image = lose_button_image.resize((200, 70))
        cls.ready_lose_button_image = ImageTk.PhotoImage(lose_button_image)

        # Создаем холст
        canvas = Canvas(
            master=window, width=settings.width, height=settings.height, bg="black"
        )
        canvas.pack()

        # Устанавливаем фон
        canvas.create_image(
            0, 0, image=lose_screen_image, anchor="nw", tag="background"
        )
        canvas.background_image = lose_screen_image  # сохраняем ссылку

        # Создаем кнопки
        try_again_button = Button(
            master=canvas,
            image=str(cls.ready_lose_button_image),
            bd=0,
            command=lambda: cls.start_game(window, settings),
        )

        # Размещение кнопок
        try_again_button.place(
            x=settings.width // 2 - cls.ready_lose_button_image.width() // 2,
            y=600,
        )
