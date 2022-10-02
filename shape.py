import abc


class Shape:

    def __init__(self, color=''):
        """
        the constructor function
        :param color: the color of the shape
        """
        self.__color = color

    def set_color(self, color):
        """
        changing the color of the shape
        :param color: the color of the shape
        """
        color = self.__color

    def get_color(self):
        """
        :return: the color of the shape
        """
        return self.__color

    # empty functions

    @abc.abstractmethod
    def get_area(self):
        pass

    @abc.abstractmethod
    def get_perimeter(self):
        pass


def main():
    element = Shape('red')
    assert element.get_color() == 'red'


if __name__ == '__main__':
    main()
