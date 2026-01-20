#from logging import exception
#from tkinter import *
from configparser import ConfigParser
import os


class ResourseManager:
    """
    Класс для подгрузки базовых настроек окна
    """

    @classmethod
    def __get_config_settings(cls) -> None:
        config = ConfigParser()

        #Логирование ошибки при отсутствии пути
        if not os.path.exists('config.ini'):
            print('Файл конфига config.ini не найден')
            print(f'Текущая директория {os.getcwd()}')

        #Решение проблемы с кодировкой
        try:
            config.read('config.ini', encoding='utf-8')
        except Exception:
            config.read('config.ini')

        #Отладочная печать
        if 'Base settings window' in config:
            print("📋 Найдены ключи:", list(config['Base settings window'].keys()))

        try:
            cls._width = int(config['Base settings window']['width'])
        except Exception as error:
            cls._width = 800  # Значение по умолчанию
            print(f"Возникла ошибка {error}")

        try:
            cls._height = int(config['Base settings window']['height'])
        except Exception as error:
            cls._height = 600  # Значение по умолчанию
            print(f"Возникла ошибка {error}")

        try:
            cls._resizable = bool(config['Base settings window']['resizable'])
        except Exception as error:
            cls._resizable = False
            print(f"Возникла ошибка {error}")

        try:
            cls._title = str(config['Base settings window']['title'])
        except Exception as error:
            cls._title = "Snake Game"
            print(f"Возникла ошибка {error}")

    @classmethod
    def load_base_settings_for_window(cls, window) -> None:
        cls.__get_config_settings()

        window.geometry(f"{cls._width}x{cls._height}")
        window.resizable(cls._resizable, cls._resizable)
        window.title(cls._title)

    @classmethod
    def get_window_geometry(cls, tag:str) -> int|None:
        match tag:
            case 'width': return cls._width
            case 'heigth': return cls._height
            case _ : return None