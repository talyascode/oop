import rectangle


class Sqaure(rectangle.Rectangle):

    def __init__(self, color=0, height=0, width=0):
        """
        the constructor function
        :param color:  the color of the square (inherited from the rectangle class)
        :param height: the height of the square (inherited from the rectangle class)
        :param width: the width of the square (inherited from the rectangle class)
        """
        super().__init__(color, height, width)

    def set_width(self, width):
        """
        changing the width of the square
        :param width: the width of the square
        """
        super(Sqaure, self).set_width(width)
        super(Sqaure, self).set_height(width)

    def set_height(self, height):
        """
        changing the height of the square
        :param height: the height of the square
        """
        super(Sqaure, self).set_width(height)
        super(Sqaure, self).set_height(height)


def main():
    square = Sqaure('red', 2, 2)
    assert square.get_color() == 'red'
    assert square.get_height() == 2
    assert square.get_width() == 2


if __name__ == '__main__':
    main()

