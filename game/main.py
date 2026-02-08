from tkinter import *
#from tkinter import messagebox
from utils.ResourseManager import ResourseManager, Resourses
from entities.Food import Food
from entities.Snake import Snake
from utils.Move import Move


def main():
    #Создаем окно
    window = Tk()

    #Подгрузка базовых настроек
    ResourseManager.load_base_settings_for_window(window)

    #Создаем холст (Игровое поле)
    canvas = Canvas(
                    window,
                    width=Resourses.width,
                    height=Resourses.height,
                    bg='black' #Убрать литерал
                    )
    canvas.pack()

    #отрисовка змеи
    snake = Snake(canvas)

    #Отрисовка еды
    food = Food(canvas)

    #Привязка обработчика к основному окну
    window.bind('<Key>', Move.button_handler)

    #Движение змеи
    Move.move(window=window, canvas=canvas, snake=snake)


    window.mainloop()


if __name__ == '__main__':
    main()