from __future__ import annotations
from tkinter import Canvas, Button, Label
from PIL import Image, ImageTk
from pathlib import Path
from typing import Final, ClassVar
from random import randint
from abc import ABC, abstractmethod
from loguru import logger


class Menu(ABC):
    # Пути к изображениям
    IMAGE_BACKGROUND: Final[Path] = Path("assets", "scenes", "BackGroundMenu.jpg")
    IMAGE_START: Final[Path] = Path("assets", "scenes", "Start.png")
    IMAGE_SETTINGS: Final[Path] = Path("assets", "scenes", "Settings.png")

    ready_start_image_menu: ClassVar

    @classmethod
    @abstractmethod
    def screen_rendering(cls, window, settings) -> None:
        """
        Метод просто отрисовывает меню с кнопками
        """
        logger.debug("Рендерю меню")
        # Загружаем фоновое изображение
        background_image_menu = Image.open(cls.IMAGE_BACKGROUND)
        background_image_menu = background_image_menu.resize(
            (settings.width, settings.height)
        )
        background_image_menu = ImageTk.PhotoImage(background_image_menu)

        # Загружаем изображения кнопок
        start_image_menu = Image.open(cls.IMAGE_START)
        start_image_menu = start_image_menu.resize((200, 70))
        cls.ready_start_image_menu = ImageTk.PhotoImage(start_image_menu)

        # Создаем холст
        canvas = Canvas(
            master=window, width=settings.width, height=settings.height, bg="black"
        )
        canvas.pack()

        # Устанавливаем фон
        canvas.create_image(
            0, 0, image=background_image_menu, anchor="nw", tag="background"
        )
        canvas.background_image = background_image_menu  # сохраняем ссылку

        # Создаем кнопки
        start_button = Button(
            master=canvas,
            image=str(cls.ready_start_image_menu),
            bd=0,
            command=lambda: cls.start_game(window, settings),
        )

        # Размещение кнопок
        start_button.place(
            x=settings.width // 2 - cls.ready_start_image_menu.width() // 2,
            y=400,
        )

    @classmethod
    def start_game(cls, window, settings) -> None:
        """
        Запускает игровой процесс
        """
        # Вода пока идет заставка
        snake_facts = settings.snake_facts

        # Очищаем экран для заставки
        for widget in window.winfo_children():
            widget.destroy()

        # Заставка
        splash_label = Label(
            window,
            text=f"""
🎬 Игра начнется через 6 секунд 🎬\n\n\n\n\n Интересный факт: {snake_facts[randint(0, len(snake_facts)-1)]}
            """,
            font=("Courier", 12),
            bg="black",
            fg="white",
        )
        splash_label.pack(expand=True, fill="both")

        window.after(6000, lambda: cls.after_splash(window=window, settings=settings))

    @classmethod
    def after_splash(cls, window, settings) -> None:
        """
        Что делать после заставки
        """
        from scenes.Game import Game

        # Удаляем все виджеты
        for widget in window.winfo_children():
            widget.destroy()

        # Запускаем игру
        Game.game_rendering(window=window, settings=settings)
