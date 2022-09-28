import shape


class Rectangle(shape.Shape):

    def __init__(self, color=0, height=0, width=0):
        super().__init__(color)
        self.__height = height
        self.__width = width

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return (self.__width * 2) + (self.__height * 2)

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def add(self, element):
        color = 0
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

