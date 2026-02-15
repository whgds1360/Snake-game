from __future__ import annotations
from tkinter import Tk
from utils.ResourseManager import ResourcesManager, Resources
from scenes.LoadScreen import LoadScreen


def main():
    #Создаем окно
    window = Tk()

    #Подгрузка настроек
    settings:Resources = Resources.from_config_file()

    #Подгрузка базовых настроек окна
    ResourcesManager.load_base_settings_for_window(window=window, base_settings=settings)

    #Рендер загрузочного экрана
    LoadScreen.load_screen_rendering(window=window, settings=settings)


    window.mainloop()


if __name__ == "__main__":
    main()
