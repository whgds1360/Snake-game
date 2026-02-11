from tkinter import Tk, Canvas #messagebox
#from tkinter import Label, Button
from utils.ResourseManager import ResourcesManager, Resources
from entities.Food import Food
from entities.Snake import Snake
from utils.Move import Move


def main():
    #Создаем окно
    window = Tk()

    #Подгрузка настроек для змеи и еды
    settings = Resources.from_config_file()

    #Подгрузка базовых настроек
    ResourcesManager.load_base_settings_for_window(window=window, base_settings=settings)

    #Создаем холст (Игровое поле)
    canvas = Canvas(
                    window,
                    width=settings.width,
                    height=settings.height,
                    bg="black" #TODO: убрать литерал!!!
                    )
    canvas.pack()

    #Отрисовка змеи
    snake = Snake(canvas=canvas, settings=settings)

    #Отрисовка еды
    food = Food(canvas=canvas, settings=settings)

    #Привязка обработчика к основному окну
    window.bind(sequence="<Key>", func=Move.button_handler)

    #Движение змеи
    Move.move(window=window, canvas=canvas, snake=snake, settings=settings)


    window.mainloop()


if __name__ == "__main__":
    main()
