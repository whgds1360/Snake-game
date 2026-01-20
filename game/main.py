from tkinter import *
#from tkinter import messagebox
from utils.ResourseManager import ResourseManager
from entities.Food import Food


def main():
    #Создаем окно
    window = Tk()

    #Подгрузка базовых настроек
    ResourseManager.load_base_settings_for_window(window)

    #Создаем холст (Игровое поле)
    canvas = Canvas(
                    window,
                    width=ResourseManager.get_settings('width'),
                    height=ResourseManager.get_settings('height'),
                    bg='black'
                    )
    canvas.pack()

    #Отрисовка еды
    food = Food(canvas)

    window.mainloop()


if __name__ == '__main__':
    main()