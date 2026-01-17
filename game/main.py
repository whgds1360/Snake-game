from tkinter import *
#from tkinter import messagebox
from utils.ResourseManager import ResourseManager


def main():
    #Создаем окно
    window = Tk()

    #Подгрузка базовых настроек
    ResourseManager.load_base_settings_for_window(window)

    #Создаем холст
    canvas = Canvas(window, width=800, height=600, bg='black')#Переделать по нормальному
    canvas.pack()

    window.mainloop()


if __name__ == '__main__':
    main()