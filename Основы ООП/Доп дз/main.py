"""# Стандартный уровень

Описать с помощью ООП любую геометрическиую фигуру.

Установку значений производить или при инициализации экземпляра (через конструктор) или через
специальные методы (сеттеры). Предусмотреть возможность получения различных
параметров фигуры (периметр, площадь, радиус, длина сектора окружности и т.д)
через методы (геттеры).

Все типы устанавливаемых значений должны проверяться.

Для класса реализовать метод __repr__.

Создать несколько экземпляров класса вашей фигуры и напечатать их repr."""
import math
from typing import Optional, Union
import matplotlib.patches
import matplotlib.path
import matplotlib.pyplot as plt


class Circle:
    def __init__(self, radius: Optional[Union[int, float]] = None, diametr: Optional[Union[int, float]] = None):
        if radius is None:
            if diametr is None:
                raise ValueError("Недостаточно аргументов")
            self.diametr = diametr
            self.radius = diametr / 2
        else:
            self.diametr = radius * 2
            self.radius = radius
        self.__set_len_circle()
        self.__set_square()

    def __repr__(self):
        return f"Circle({self.radius}, {self.square})"

    def __set_len_circle(self):
        self.len_circle = round(2 * math.pi * self.radius, 2)

    def __set_square(self):
        self.square = round(math.pi * self.radius ** 2)

    def get_len_circle(self):
        return self.len_circle

    def get_square(self):
        return self.square

    def get_length_circles_arc(self, n: Union[int, float]) -> Union[int, float]:
        return round(math.pi * self.radius * n / 180)

    def get_square_circles_arc(self, n: Union[int, float]) -> Union[int, float]:
        return round(math.pi * self.radius ** 2 * n / 360)

    def drawCircles(self, _color: Union[str, tuple] = '#181513', _fill: bool = False):
        if isinstance(_color, tuple):
            _color = '#' + str(hex(_color[0] * 65536 + _color[1] * 256 + _color[2])[2:])
        """ Рисование окружностей """
        cord = self.radius + 1
        plt.xlim(-cord, cord)
        plt.ylim(-cord, cord)
        plt.grid()
        axes = plt.gca()
        axes.set_aspect("equal")
        circle2 = matplotlib.patches.Circle((0, 0), radius=self.radius, fill=_fill, color=_color)
        axes.add_patch(circle2)
        plt.show()


if __name__ == "__main__":
    circle_1 = Circle(radius=10)
    circle_1.drawCircles(_color="#ff0000")
