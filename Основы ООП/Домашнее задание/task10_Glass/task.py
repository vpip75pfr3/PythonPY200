# TODO написать класс Glass согласно условию
class Glass:
    def __init__(self, material: str):
        self._material = material

    def get_material(self):
        return self._material


if __name__ == "__main__":
    first_glass = Glass('plastic')
    print(first_glass.get_material())

