from typing import List, final


@final
class Snake:
    def __init__(self, canvas, settings)->None:
        #Для выравнивания змейки по центру окна
        width:int = settings.width // 2
        height:int = settings.height // 2

        self.coord:List[List] = [[width, height+ settings.space_size*2],
                      [width, height + settings.space_size],
                      [width, height]]
        self.squares:List = []

        for x, y in self.coord:
            square = canvas.create_rectangle(
                x, y,
                x+settings.space_size,
                y+settings.space_size,
                fill=settings.snake_color
            )

            self.squares.append(square)


    def check_self_collision(self) -> bool:
        """
        Проверка столкновения с собой
        """
        if len(self.coord) < 4:  # Для 3 и менее сегментов столкновение невозможно
            return False

        # Проверяем, не врезалась ли голова в тело
        # Пропускаем первый сегмент после головы (шею), так как он всегда рядом
        head = self.coord[0]
        body_without_neck = self.coord[2:]  # пропускаем голову и шею

        return head in body_without_neck
