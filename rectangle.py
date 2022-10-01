import shape


class Rectangle(shape.Shape):

    def __init__(self, color='', height=0, width=0):
        """
        the constructor function
        :param color: the color of the rectangle (inherited from the shape class)
        :param height: the height of the rectangle
        :param width: the width of the rectangle
        """

        super().__init__(color)
        self.__height = height
        self.__width = width

    def get_area(self):
        """
        :return: the area of the rectangle
        """
        return self.__width * self.__height

    def get_perimeter(self):
        """
        :return: the perimeter of the rectangle
        """
        return (self.__width * 2) + (self.__height * 2)

    def get_width(self):
        """
        :return: the width of the rectangle
        """
        return self.__width

    def get_height(self):
        """
        :return: the height of the rectangle
        """
        return self.__height

    def set_width(self, width):
        """
        changing the width of the rectangle
        :param width: the width of the rectangle
        """
        self.__width = width

    def set_height(self, height):
        """
        changing the height of the rectangle
        :param height: the height of the rectangle
        """
        self.__height = height

    def add(self, element):
        """
        adding two shapes together ( square or a shape )
        :param element: a rectangle or a square
        :return: the new shape
        """
        color = element.get_color()
        new_shape = None
        # isinstance(other, Rectangle)
        if element.get_height() == self.__height:
            width = element.get_width() + self.__width
            new_shape = Rectangle(color, element.get_height(), width)
            return new_shape
        if element.get_width() == self.__width:
            height = element.get_height() + self.__height
            new_shape = Rectangle(color, height, element.get_width())
            return new_shape
        if element.get_height() == self.__width:
            height = element.get_width() + self.__height
            new_shape = Rectangle(color, height, self.__width)
            return new_shape
        if element.get_width() == self.__height:
            width = element.get_width() + self.__height
            new_shape = Rectangle(color, self.__height, width)
            return new_shape
        return new_shape


def main():
    rectangle = Rectangle('red', 2, 4)
    assert rectangle.get_color() == 'red'
    assert rectangle.get_height() == 2
    assert rectangle.get_width() == 4


if __name__ == '__main__':
    main()

