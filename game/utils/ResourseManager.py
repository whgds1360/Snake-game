from __future__ import annotations
from configparser import ConfigParser
from typing import final, Final, ClassVar, Dict
from pathlib import Path
from pydantic import BaseModel, field_validator, Field, model_validator


@final
class Resources(BaseModel):
    """
    Получение базовых настроек
    """
    #Константы
    DEFAULT_CONFIG_NAME:ClassVar[Final[str]] = "Config.ini"

    # Базовые настройки окна
    width: int = Field(default=1024, repr=True, init=True)
    height: int = Field(default=768, repr=True, init=True)
    resizable: bool = Field(default=False, repr=True, init=True)
    title: str = Field(default="Snake Game", repr=True, init=True)
    icon_path: str = Field(default=Path("assets", "icon", "app_icon.ico"), repr=True, init=True)

    # Базовые настройки игры
    snake_color: str = Field(default="green", repr=True, init=True)
    food_color: str = Field(default="red", repr=True, init=True)
    delay: int = Field(default=200, repr=True, init=True)

    # Настройки игрового поля
    space_size: int = Field(default=32, repr=True, init=True)
    width_game_place: int = Field(default=640, repr=True, init=True)
    height_game_place: int = Field(default=640, repr=True, init=True)
    color_field_game_place: str = Field(default="pink", repr=True, init=True)


    @field_validator("width")
    @classmethod
    def validate_width(cls, value:int) -> int:
        if value <= 0:
            raise ValueError("Ширина экрана должна быть положительным числом")
        if value % 2 != 0:
            raise ValueError("Ширина экрана должна быть четной для корректного отображения")
        return value


    @field_validator("height")
    @classmethod
    def validate_height(cls, value: int) -> int:
        if value <= 0:
            raise ValueError("Высота экрана должна быть положительным числом")
        if value % 2 != 0:
            raise ValueError("Высота экрана должна быть четной для корректного отображения")
        return value


    @model_validator(mode="after")
    def validate_space_size(self) -> Resources:
        if self.width % self.space_size != 0 or self.height % self.space_size != 0:
            raise ValueError("""    Введен некорректный размер игрового поля!!!
            
                                                Обратите внимание!!!
                                Ширина и высота окна должны делиться на размер сетки!!!
                                        А также ширина и высота игрового поля!!!
            """)
        return self


    @model_validator(mode="after")
    def validate_width_game_place(self) -> Resources:
        if self.width <= self.width_game_place:
            raise ValueError("Ширина игрового поля превышает размеры окна!")
        return self


    @model_validator(mode="after")
    def validate_height_game_place(self) -> Resources:
        if self.height <= self.height_game_place:
            raise ValueError("Высота игрового поля превышает размеры окна!")
        return self


    @classmethod
    def from_config_file(cls, config_file: str = DEFAULT_CONFIG_NAME) -> Resources:
        """Создать конфигурацию из файла"""
        config_parser:ConfigParser = ConfigParser()

        config_path:Path = Path(config_file)
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
        path_icon:Path = Path("assets", "icon", "app_icon.ico")
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
            title=str(base_settings.get("title", "Snake Game")),
            icon_path=str(place_settings.get("path_icon", path_icon)),

            # Базовые настройки игры
            delay=int(game_settings.get("delay", 200)),
            snake_color=str(game_settings.get("snake_color", "green")),
            food_color=str(game_settings.get("food_color", "red")),

            # Настройки игрового поля
            space_size = int(place_settings.get("space_size", 32)),
            width_game_place = int(place_settings.get("width_game_place", 640)),
            height_game_place = int(place_settings.get("height_game_place", 640)),
            color_field_game_place =str(place_settings.get("color_field_game_place", "pink")),
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
