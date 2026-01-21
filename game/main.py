from tkinter import *
#from tkinter import messagebox
from utils.ResourseManager import ResourseManager, Resourses
from entities.Food import Food
from entities.Snake import Snake
from utils.Move import move


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
                    bg='black'
                    )
    canvas.pack()

    #отрисовка змеи
    snake = Snake(canvas)

    #Отрисовка еды
    food = Food(canvas)

    #движение змеи
    move(window=window, canvas=canvas, snake=snake, food=food, direction='down')
    window.mainloop()

    window.mainloop()


if __name__ == '__main__':
    main()