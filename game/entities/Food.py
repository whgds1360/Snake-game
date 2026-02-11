from random import randint


class Food:
    def __init__(self, canvas, settings)->None:
        #Получение информации о размере поля
        self.width = settings.width
        self.height = settings.height

        # Получение информации о размере клетки
        self.space_size = settings.space_size

        #Получение информации о еде
        self.color_food = settings.food_color


        self.begin_x = randint(0, (self.width // self.space_size)) * self.space_size
        self.begin_y = randint(0, (self.height // self.space_size)) * self.space_size

        canvas.create_rectangle(self.begin_x, #Начальные координаты
                                self.begin_y, #Начальные координаты
                                self.begin_x + self.space_size, #Конечные координаты
                                self.begin_y + self.space_size, #Конечные координаты
                                fill=self.color_food) #Закраска
