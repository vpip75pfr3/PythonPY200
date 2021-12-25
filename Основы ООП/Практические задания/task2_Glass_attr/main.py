from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):

        self.__capacity_volume = self.__check_capacity_volume(capacity_volume)
        self.__occupied_volume = self.__check_occupied_volume(occupied_volume)

        # self.__check_overflow(self.capacity_volume, self.occupied_volume)
        self.__check_overflow(self.__capacity_volume, self.__occupied_volume)

    @staticmethod
    def __check_capacity_volume(value) -> Union[int, float]:
        """
        :param value:
        :return:
        """
        if not isinstance(value, (int, float)):
            raise TypeError
        if value <= 0:
            raise ValueError
        return value

    @staticmethod
    def __check_occupied_volume(value) -> Union[int, float]:
        if not isinstance(value, (int, float)):
            raise TypeError
        if value < 0:
            raise ValueError
        return value

    # @staticmethod
    # def __check_overflow(capacity, occupied):
    #     if capacity < occupied:
    #         raise OverflowError('Стакан не резиновый')
    @staticmethod
    def __check_overflow(capacity, occupied):
        if capacity < occupied:
            raise OverflowError('Стакан не резиновый')

    def get_capacity_volume(self) -> Union[int, float]:
        """Функция возвращает объем стакана"""
        return self.__capacity_volume

    def get_occupied_volume(self) -> Union[int, float]:
        """Функция возвращает занятый объем стакана"""
        return self.__occupied_volume

    def add_water(self, value: Union[int, float]) -> None:
        if value < 0:
            self.__remove_water(value)
        else:
            self.__check_occupied_volume(value)
            self.__check_overflow(self.__capacity_volume, self.__occupied_volume + value)
            self.__occupied_volume += value

    def __remove_water(self, value):
        self.__occupied_volume += value

if __name__ == "__main__":
    glass1 = Glass(800, 100)  # экземпляр класса
    print(glass1.get_capacity_volume(), glass1.get_occupied_volume())
    glass1.add_water(-100)
    print(glass1.get_capacity_volume(), glass1.get_occupied_volume())

    # glass2 = ...  # TODO инициализировать ещё один стакан
    # print(...)  # TODO распечатать атрибуты экземпляра glass2
    #
    # print("Доливаем воды в первый стакан...")
    # #  TODO доливаем воды в первый стакан
    # print(glass1.capacity_volume, glass1.occupied_volume)
    # print(glass2.capacity_volume, glass2.occupied_volume)
    #
    # #  TODO сравнить id объектов
