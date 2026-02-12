from random import randint
from typing import final


@final
class Food:
    def __init__(self, canvas, settings)->None:
        #Получение информации о размере поля
        self.width:int = settings.width
        self.height:int = settings.height

        # Получение информации о размере клетки
        self.space_size:int = settings.space_size

        #Получение информации о еде
        self.color_food:int = settings.food_color


        self.begin_x:int = randint(0, (self.width // self.space_size)) * self.space_size
        self.begin_y:int = randint(0, (self.height // self.space_size)) * self.space_size

        canvas.create_rectangle(self.begin_x, #Начальные координаты
                                self.begin_y, #Начальные координаты
                                self.begin_x + self.space_size, #Конечные координаты
                                self.begin_y + self.space_size, #Конечные координаты
                                fill=self.color_food) #Закраска
