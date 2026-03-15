from __future__ import annotations
from configparser import ConfigParser
from pathlib import Path
from typing import Dict, Final, final, List, Optional
from loguru import logger
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


@final
class Resources(BaseModel):
    """
    Получение базовых настроек
    """

    model_config = ConfigDict(
        extra="ignore",  # действие при передаче лишних полей
        frozen=True,  # Запрет на изменение экземлпяра
        validate_default=True,  # Валидация дефолтных значений
    )

    # Константы
    DEFAULT_CONFIG_NAME: Final[str] = "Config.ini"

    # Базовые настройки окна
    width: int = Field(default=1024, repr=True, init=True)
    height: int = Field(default=768, repr=True, init=True)
    resizable: bool = Field(default=False, repr=True, init=True)
    title: str = Field(default="Snake Game", repr=True, init=True)
    icon_path: Path = Field(
        default=Path("assets", "icon", "app_icon.ico"), repr=True, init=True
    )

    # Базовые настройки игры
    snake_color: str = Field(default="green", repr=True, init=True)
    food_color: str = Field(default="red", repr=True, init=True)
    delay: int = Field(default=200, repr=True, init=True)

    # Настройки игрового поля
    space_size: int = Field(default=32, repr=True, init=True)
    width_game_place: int = Field(default=640, repr=True, init=True)
    height_game_place: int = Field(default=640, repr=True, init=True)
    color_field_game_place: str = Field(default="pink", repr=True, init=True)

    # Прочие настройки
    snake_facts: Optional[List[str]] = Field(default=[], repr=True, init=True)

    @field_validator("width")
    @classmethod
    def validate_width(cls, value: int) -> int:
        if value <= 0:
            raise ValueError("Ширина экрана должна быть положительным числом")
        if value % 2 != 0:
            raise ValueError(
                "Ширина экрана должна быть четной для корректного отображения"
            )
        return value

    @field_validator("height")
    @classmethod
    def validate_height(cls, value: int) -> int:
        if value <= 0:
            raise ValueError("Высота экрана должна быть положительным числом")
        if value % 2 != 0:
            raise ValueError(
                "Высота экрана должна быть четной для корректного отображения"
            )
        return value

    @model_validator(mode="after")
    def validate_space_size(self) -> Resources:
        if self.width % self.space_size != 0 or self.height % self.space_size != 0:
            raise ValueError(
                """                 Введен некорректный размер игрового поля!!!

                                                Обратите внимание!!!
                                Ширина и высота окна должны делиться на размер сетки!!!
                                        А также ширина и высота игрового поля!!!
            """
            )
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

    @field_validator("snake_facts", mode="before")
    @classmethod
    def parse_snake_facts(cls, value):
        """
        Превращаем строку из конфига в список строк.
        Если уже список, то оставляем как есть.
        """
        if isinstance(value, list):
            return value

        if isinstance(value, str):
            # Если строка не пришла из конфига
            if not value.strip():
                return []

            # Разделяем по запятым
            items = [item.strip() for item in value.split(";") if item.strip()]

            # Если после разделения ничего нет
            if not items:
                return []

            return items

        # На всякий случай если сверху пойдет что - то не так
        return []

    @classmethod
    def from_config_file(cls, config_file: str = DEFAULT_CONFIG_NAME) -> Resources:
        """Создать конфигурацию из файла"""
        config_parser: ConfigParser = ConfigParser()

        config_path: Path = Path(config_file)
        # Проверка существования файла
        if not config_path.exists():
            logger.error(f"Файл конфига {config_path} не найден")
            return cls()  # Возвращаем конфиг со значениями по умолчанию

        logger.debug("Начинаю чтение конфига")
        # Чтение конфига
        try:
            config_parser.read(config_file, encoding="utf-8")
        except UnicodeError:
            logger.exception("Ошибка кодировки при чтении конфига")
            config_parser.read(config_file)
        except PermissionError:
            logger.exception("Недостаточно прав для открытия конфигурационного файла!")
        except Exception as error:
            logger.exception(
                f"Возникла ошибка:{error} при работе с конфигурационным файлом!"
            )

        # Отладочная печать
        if "Settings window" in config_parser:
            logger.debug(
                f"📋 Найдены ключи: {list(config_parser['Settings window'].keys())}"
            )

        if "Gameplay settings" in config_parser:
            logger.debug(
                f"📋 Найдены ключи:, {list(config_parser['Gameplay settings'].keys())}"
            )

        if "Game place settings" in config_parser:
            logger.debug(
                f"📋 Найдены ключи:, {list(config_parser['Game place settings'].keys())}"
            )
        if "Other" in config_parser:
            logger.debug(f"📋 Найдены ключи:, {list(config_parser['Other'].keys())}")

        # Путь до иконки
        path_icon: Path = Path("assets", "icon", "app_icon.ico")
        if not path_icon.exists():
            logger.error("Иконка не найдена")
            logger.error(f"Путь поиска: {path_icon}")

        # Извлечение значений
        base_settings: Dict[str, str] = dict(
            config_parser.items("Settings window")
        )  # как словарь
        game_settings: Dict[str, str] = dict(
            config_parser.items("Gameplay settings")
        )  # как словарь
        place_settings: Dict[str, str] = dict(
            config_parser.items("Game place settings")
        )  # как словарь
        other_settings: Dict[str, str] = dict(
            config_parser.items("Other")
        )  # как словарь

        data = {**base_settings, **game_settings, **place_settings, **other_settings}

        return cls.model_validate(data)


@final
class ResourceManager:
    """
    Класс для подгрузки базовых настроек окна и настроек игрового поля
    """

    logger.debug("Начинаю подгрузку базовых настроек окна")

    @staticmethod
    def load_base_settings_for_window(window, base_settings) -> None:
        window.geometry(f"{base_settings.width}x{base_settings.height}")
        window.resizable(base_settings.resizable, base_settings.resizable)
        window.title(base_settings.title)
        window.iconbitmap(base_settings.icon_path)
