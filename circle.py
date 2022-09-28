import shape
PAI = 3.14


class Circle(shape.Shape):

    def __init__(self, color=0, radius=0):
        super().__init__(color)
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_area(self):
        return self.__radius * self.__radius * PAI

    def get_perimeter(self):
        return self.__radius * PAI * 2


def main():

    assert Circle.get_color() == "RED"


if __name__ == '__main__':
    main()