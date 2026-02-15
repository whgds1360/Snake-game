from __future__ import annotations
from tkinter import Canvas, Button, Label
from PIL import Image, ImageTk
from pathlib import Path
from typing import Final, final
from game.scenes.Game import Game
from random import randint


@final
class Menu:
    # Пути к изображениям
    IMAGE_BACKGROUND: Final[Path] = Path("assets", "scenes", "BackGroundMenu.jpg")
    IMAGE_START: Final[Path] = Path("assets", "scenes", "Start.png")
    IMAGE_SETTINGS: Final[Path] = Path("assets", "scenes", "Settings.png")


    @classmethod
    def menu_rendering(cls, window, settings)->None:
        """
        Метод просто отрисовывает меню с кнопками
        """
        # Загружаем фоновое изображение
        background_image_menu = Image.open(cls.IMAGE_BACKGROUND)
        background_image_menu = background_image_menu.resize((settings.width, settings.height))
        background_image_menu = ImageTk.PhotoImage(background_image_menu)

        # Загружаем изображения кнопок
        start_image_menu = Image.open(cls.IMAGE_START)
        start_image_menu = start_image_menu.resize((200, 70))
        cls.ready_start_image_menu = ImageTk.PhotoImage(start_image_menu)

        settings_image_menu = Image.open(cls.IMAGE_SETTINGS)
        settings_image_menu = settings_image_menu.resize((200, 70))
        cls.ready_settings_image_menu = ImageTk.PhotoImage(settings_image_menu)

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

        # Создаем кнопки с правильной передачей параметров
        start_button = Button(
            master=canvas,
            image=cls.ready_start_image_menu,
            bd=0,
            command=lambda: cls.start_game(window, settings)  # ВАЖНО: передаем параметры через lambda
        )

        settings_button = Button(
            master=canvas,
            image=cls.ready_settings_image_menu,
            bd=0,
            command=lambda: cls.open_settings(window, settings)  # если нужны параметры
        )

        # Размещение кнопок
        start_button.place(
            x=settings.width // 2 - cls.ready_start_image_menu.width() // 2,
            y=400,
        )

        settings_button.place(
            x=settings.width // 2 - cls.ready_settings_image_menu.width() // 2,
            y=500,
        )


    @classmethod
    def start_game(cls, window, settings)->None:
        """
        Запускает игровой процесс
        """
        #Вода пока идет заставка
        snake_facts = [
            "🐍 Змеи не имеют век и спят с открытыми глазами!",
            "🐍 Самая длинная змея в мире - сетчатый питон (до 10 метров)",
            "🐍 Змеи чувствуют запахи языком, а не носом!",
            "🐍 В мире существует около 3000 видов змей",
            "🐍 Змеи могут есть только раз в несколько месяцев",
            "🐍 Самая быстрая змея - черная мамба (до 20 км/ч)",
            "🐍 Змеи глухие, но чувствуют вибрацию земли",
            "🐍 Кобра может плеваться ядом на расстояние до 3 метров"
        ]

        #Очищаем экран для заставки
        for widget in window.winfo_children():
            widget.destroy()

        #Заставка
        splash_label = Label(window, text=f"🎬 Игра начнется через 6 секунд 🎬\n\n\n\n\n Интересный факт: {snake_facts[randint(0, len(snake_facts)-1)]}",
                                font=("Courier", 12),
                                bg="black", fg="white")
        splash_label.pack(expand=True, fill="both")

        # Сохраняем ссылку на лейбл
        window.splash_label = splash_label

        window.after(6000, lambda:cls.after_splash(window, settings))


    @classmethod
    def after_splash(cls, window, settings)->None:
        """
        Что делать после заставки
        """
        # Удаляем все виджеты
        for widget in window.winfo_children():
            widget.destroy()

        # Запускаем игру
        Game.game_rendering(window=window, settings=settings)


    @classmethod
    def open_settings(cls, window, settings)->None:
        """
        Открывает настройки
        """
        pass
            # Здесь будет логика настроек
