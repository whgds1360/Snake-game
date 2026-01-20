from random import randint
from game.utils.ResourseManager import ResourseManager


class Food:

    def __init__(self, canvas)->None:

        #Получение информации о размере поля
        self.width = ResourseManager.get_settings('width')
        self.height = ResourseManager.get_settings('height')

        # Получение информации о размере клетки
        self.space_size = ResourseManager.get_settings('space_size')

        #Получение информации о еде
        self.color_food = ResourseManager.get_settings('food_color')


        self.begin_x = randint(0, (self.width // self.space_size) - 1) * self.space_size
        self.begin_y = randint(0, (self.height // self.space_size) - 1) * self.space_size

        canvas.create_rectangle(self.begin_x, #Начальные координаты
                                self.begin_y, #Начальные координаты
                                self.begin_x + self.space_size, #Конечные координаты
                                self.begin_y + self.space_size, #Конечные координаты
                                fill=self.color_food) #Закраска
