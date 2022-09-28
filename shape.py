import abc


class Shape:

    def __init__(self, color=0):
        """
        constructor
        :param color: the color of the shape
        """
        self.__color = color

    def set_color(self, color):
        color = self.__color

    def get_color(self):
        return self.__color

    @abc.abstractmethod
    def get_area(self):
        pass

    @abc.abstractmethod
    def get_perimeter(self):
        pass
