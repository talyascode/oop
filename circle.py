import shape
PAI = 3.14


class Circle(shape.Shape):

    def __init__(self, color=0, radius=0):
        """
         the constructor function
        :param color: the color of the circle (inherited from the shape class)
        :param radius: the radius of the circle
        """

        super().__init__(color)
        self.__radius = radius

    def get_radius(self):
        """
        :return: the radius of the circle
        """
        return self.__radius

    def set_radius(self, radius):
        """
        changing the radius of the circle
        :param radius: the radius of the circle
        """
        self.__radius = radius

    def get_area(self):
        """
        :return: the area of the circle
        """
        return self.__radius * self.__radius * PAI

    def get_perimeter(self):
        """
        :return: the perimeter of the circle
        """
        return self.__radius * PAI * 2


def main():
    circle = Circle('red', 2)
    assert circle.get_color() == 'red'
    assert circle.get_radius() == 2


if __name__ == '__main__':
    main()
