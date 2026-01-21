from configparser import ConfigParser
from os.path import exists, join
from os import getcwd
from dataclasses import dataclass, field
#from typing import Optional для совместимости со старыми версиями python


@dataclass
class Resourses:
    """Получение базовых настроек"""
    # Базовые настройки окна
    width: int = 1024
    height: int = 768
    resizable: bool = False
    title: str = "Snake Game"
    icon_path: str = join('assets', 'icon', 'app_icon.ico')

    # Настройки игрового поля
    space_size: int | None = 25
    food_color: str | None = 'red'

    # Служебные поля (не будут включаться в __init__)
    __name_config_file: str = field(default='config.ini', repr=False, init=False)

    @classmethod
    def from_config_file(cls, config_file: str = 'config.ini') -> 'Resourses':
        """Создать конфигурацию из файла"""
        config_parser = ConfigParser()

        # Проверка существования файла
        if not exists(config_file):
            print(f'Файл конфига {config_file} не найден')
            print(f'Текущая директория {getcwd()}')
            return cls()  # Возвращаем конфиг со значениями по умолчанию

        # Чтение конфига
        try:
            config_parser.read(config_file, encoding='utf-8')
        except Exception:
            config_parser.read(config_file)

        # Отладочная печать
        if 'Base settings window' in config_parser:
            print("📋 Найдены ключи:", list(config_parser['Base settings window'].keys()))

        if 'Game place settings' in config_parser:
            print("📋 Найдены ключи:", list(config_parser['Game place settings'].keys()))

        # Путь до иконки
        path_icon = join('assets', 'icon', 'app_icon.ico')
        if not exists(path_icon):
            print('Иконка не найдена')
            print(f'Путь поиска: {path_icon}')

        # Извлечение значений
        base_settings = dict(config_parser.items('Base settings window'))  # как словарь
        place_settings = dict(config_parser.items('Game place settings'))  # как словарь

        return cls(
            width=int(base_settings.get('width', 1280)),
            height=int(base_settings.get('height', 800)),
            resizable=base_settings.get('resizable', 'False') == 'True',
            title=base_settings.get('title', 'Snake Game'),
            space_size=int(place_settings.get('space_size', 25)),
            food_color=base_settings.get('food_color', 'red'),
            icon_path =place_settings.get('path_icon', path_icon)
        )


class ResourseManager:
    """
    Класс для подгрузки базовых настроек окна и настроек игрового поля
    """
    @staticmethod
    def load_base_settings_for_window(window) -> None:
        base_settings = Resourses.from_config_file()

        window.geometry(f"{base_settings.width}x{base_settings.height}")
        window.resizable(base_settings.resizable, base_settings.resizable)
        window.title(base_settings.title)
        window.iconbitmap(base_settings.icon_path)
