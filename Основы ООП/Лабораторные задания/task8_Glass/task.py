# TODO Добавить методы add_water и remove_water

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