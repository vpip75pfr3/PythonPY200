from typing import Union


# TODO  создать класс Glass

class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.__check_capacity_volume(capacity_volume)
        self.capacity_volume = capacity_volume
        self.__check_occupied_volume(occupied_volume)
        self.occupied_volume = occupied_volume
        self.__check_overflow()
        #  TODO инициализировать объект "Стакан"

    @staticmethod
    def __check_capacity_volume(value):
        if not isinstance(value, (int, float)):
            raise TypeError
        if value <= 0:
            raise ValueError

    @staticmethod
    def __check_occupied_volume(value):
        if not isinstance(value, (int, float)):
            raise TypeError
        if value < 0:
            raise ValueError

    def __check_overflow(self):
        if self.capacity_volume < self.occupied_volume:
            raise OverflowError('Стакан не резиновый')



if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)
