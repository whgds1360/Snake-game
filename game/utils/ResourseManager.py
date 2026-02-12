from configparser import ConfigParser
from dataclasses import dataclass, field
from typing import final, Final, ClassVar, Optional, Dict
from pathlib import Path


@final
@dataclass
class Resources:
    """Получение базовых настроек"""
    #Константы
    DEFAULT_CONFIG_NAME:ClassVar[Final[str]] = "Config.ini"

    # Базовые настройки окна
    width: int = field(default=1024, repr=True, init=True)
    height: int = field(default=768, repr=True, init=True)
    resizable: bool = field(default=False, repr=True, init=True)
    title: str = field(default="Snake Game", repr=True, init=True)
    icon_path: str = field(default=Path("assets", "icon", "app_icon.ico"), repr=True, init=True)

    # Базовые настройки игры
    snake_color: str = field(default="green", repr=True, init=True)
    food_color: str = field(default="red", repr=True, init=True)
    delay: int = field(default="200", repr=True, init=True)

    # Настройки игрового поля
    space_size: int = field(default=32, repr=True, init=True)

    @classmethod
    def from_config_file(cls, config_file: Optional[str] = DEFAULT_CONFIG_NAME) -> "Resources":
        """Создать конфигурацию из файла"""
        config_parser:"ConfigParser" = ConfigParser()

        config_path:"Path" = Path(config_file)
        # Проверка существования файла
        if not config_path.exists():
            print(f"Файл конфига {config_path} не найден")
            return cls()  # Возвращаем конфиг со значениями по умолчанию

        # Чтение конфига
        try:
            config_parser.read(config_file, encoding="utf-8")
        except UnicodeError:
            config_parser.read(config_file)
        except PermissionError:
            print(f"Недостаточно прав для открытия конфигурационного файла!")
        except Exception as error:
            print(f"Возникла ошибка:{error} при работе с конфигурационным файлом!")


        # Отладочная печать
        if "Settings window" in config_parser:
            print("📋 Найдены ключи:", list(config_parser["Settings window"].keys()))

        if "Gameplay settings" in config_parser:
            print("📋 Найдены ключи:", list(config_parser["Gameplay settings"].keys()))

        if "Game place settings" in config_parser:
            print("📋 Найдены ключи:", list(config_parser["Game place settings"].keys()))

        # Путь до иконки
        path_icon:"Path" = Path("assets", "icon", "app_icon.ico")
        if not path_icon.exists():
            print("Иконка не найдена")
            print(f"Путь поиска: {path_icon}")

        # Извлечение значений
        base_settings:Dict[str, str] = dict(config_parser.items("Settings window"))  # как словарь
        game_settings:Dict[str, str] = dict(config_parser.items("Gameplay settings")) # как словарь
        place_settings:Dict[str, str] = dict(config_parser.items("Game place settings"))  # как словарь

        return cls(
            # Базовые настройки окна
            width=int(base_settings.get("width", 1024)),
            height=int(base_settings.get("height", 768)),
            resizable=base_settings.get("resizable", "False") == "True",
            title=base_settings.get("title", "Snake Game"),
            icon_path=place_settings.get("path_icon", path_icon),

            # Базовые настройки игры
            delay=int(game_settings.get("delay", 200)),
            snake_color=game_settings.get("snake_color_default", "green"),
            food_color=game_settings.get("food_color_default", "red"),

            # Настройки игрового поля
            space_size = int(place_settings.get("space_size", 25))
        )


@final
class ResourcesManager:
    """
    Класс для подгрузки базовых настроек окна и настроек игрового поля
    """
    @staticmethod
    def load_base_settings_for_window(window, base_settings) -> None:
        window.geometry(f"{base_settings.width}x{base_settings.height}")
        window.resizable(base_settings.resizable, base_settings.resizable)
        window.title(base_settings.title)
        window.iconbitmap(base_settings.icon_path)
