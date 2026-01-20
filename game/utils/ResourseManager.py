from configparser import ConfigParser
from os.path import exists, join
from os import getcwd


class ResourseManager:
    """
    Класс для подгрузки базовых настроек окна и настроек игрового поля
    """


    @classmethod
    def __get_config_settings(cls) -> None:
        config = ConfigParser()

        #Логирование ошибки при отсутствии пути
        if not exists('config.ini'):
            print('Файл конфига config.ini не найден')
            print(f'Текущая директория {getcwd()}')

        #Решение проблемы с кодировкой
        try:
            config.read('config.ini', encoding='utf-8')
        except Exception:
            config.read('config.ini')

        #Отладочная печать
        if 'Base settings window' in config:
            print("📋 Найдены ключи:", list(config['Base settings window'].keys()))

        if 'Game place settings' in config:
            print("📋 Найдены ключи:", list(config['Game place settings'].keys()))

        try:
            cls._width = int(config['Base settings window']['width'])
        except Exception as error:
            cls._width = 1280  # Значение по умолчанию
            print(f"Возникла ошибка {error}")

        try:
            cls._height = int(config['Base settings window']['height'])
        except Exception as error:
            cls._height = 800  # Значение по умолчанию
            print(f"Возникла ошибка {error}")

        try:
            _resizable = str(config['Base settings window']['resizable'])
            cls._resizable = True if _resizable == 'True' else False
        except Exception as error:
            cls._resizable = False
            print(f"Возникла ошибка {error}")

        try:
            cls._title = str(config['Base settings window']['title'])
        except Exception as error:
            cls._title = "Snake Game"
            print(f"Возникла ошибка {error}")

        #Настройки для игрового поля
        try:
            cls._space_size = int(config['Game place settings']['space_size'])
        except Exception as error:
            print(f"Возникла ошибка {error}")

        #Цвет еды
        try:
            cls._food_color = str(config['Game place settings']['food_color'])
        except Exception as error:
            print(f"Возникла ошибка {error}")


    @classmethod
    def load_base_settings_for_window(cls, window) -> None:
        cls.__get_config_settings()

        #Путь до иконки
        path_icon = join('assets', 'icon', 'app_icon.ico')
        if not exists(path_icon):
            print('Иконка не найдена')
            print(f'Путь поиска: {path_icon}')


        window.geometry(f"{cls._width}x{cls._height}")
        window.resizable(cls._resizable, cls._resizable)
        window.title(cls._title)
        window.iconbitmap(path_icon)


    @classmethod
    def get_settings(cls, tag:str) -> int|str|None:
        cls.__get_config_settings()

        match tag:
            case 'width': return cls._width
            case 'height': return cls._height
            case 'space_size': return cls._space_size
            case 'food_color': return cls._food_color
            case _ : return None
