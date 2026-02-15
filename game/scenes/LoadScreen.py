from __future__ import annotations
from tkinter import Canvas
from PIL import Image, ImageTk
from pathlib import Path
from typing import Final, final
from game.scenes.Menu import Menu


@final
class LoadScreen:
    # Пути к изображениям
    IMAGE_LOAD_SCREEN: Final[Path] = Path("assets", "scenes", "LoadScreen.png")

    @classmethod
    def load_screen_rendering(cls, window, settings)->None:
        """
        Метод просто отрисовывает меню с кнопками
        """
        # Загружаем фоновое изображение
        background_image_menu = Image.open(cls.IMAGE_LOAD_SCREEN)
        background_image_menu = background_image_menu.resize((settings.width, settings.height))
        background_image_menu = ImageTk.PhotoImage(background_image_menu)

        # Создаем холст
        canvas = Canvas(
            master=window,
            width=settings.width,
            height=settings.height,
            bg="black"
        )
        canvas.pack()

        # Устанавливаем фон
        canvas.create_image(0, 0, image=background_image_menu, anchor="nw", tag="background")
        canvas.background_image = background_image_menu  # сохраняем ссылку

        window.after(6000, lambda: cls.menu_render(window, settings))


    @classmethod
    def menu_render(cls, window, settings)->None:

        #Очищаем экран для заставки
        for widget in window.winfo_children():
            widget.destroy()

        Menu.menu_rendering(window, settings)

