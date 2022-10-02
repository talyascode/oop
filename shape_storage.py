import random
from circle import *
from rectangle import *
# color dictionary
color_num = {1: 'blue', 2: 'red', 3: 'black'}


class ShapeStorage:
    def __init__(self):
        """
        the constructor function
        """
        self.__my_shapes = []

    def generate(self, x):
        """
        randomly creating random shapes x times
        :param x: the amount of shapes that are being created
        """
        for x in range(x):
            color = random.randint(1, 3)
            color = color_num[color]
            shape_num = random.randint(1, 3)
            if shape_num == 1:
                #  shape is circle
                radius = random.randint(1, 100)
                new_shape = Circle(color, radius)
            if shape_num == 2:
                #  shape is rectangle
                height = random.randint(1, 100)
                width = random.randint(1, 100)
                new_shape = Rectangle(color, height, width)
            if shape_num == 3:
                #  shape is square
                side = random.randint(1, 100)
                new_shape = Rectangle(color, side, side)

            self.__my_shapes.append(new_shape)

    def sum_areas(self):
        """
        summing all the areas of the shapes in the list
        :return: the sum
        """
        area_sum = 0
        for element in self.__my_shapes:
            area_sum += element.get_area()
        return area_sum

    def sum_perimeter(self):
        """
        summing all the perimeters of the shapes in the list
        :return: the sum
        """
        perimeter_sum = 0
        for element in self.__my_shapes:
            perimeter_sum += element.get_perimeter()
        return perimeter_sum

    def count_colors(self):
        """
        counting how many colors there are from each color of the shapes in the list
        :return: a dictionary of how many colors there are from each color
        """
        red_counter = 0
        blue_counter = 0
        black_counter = 0
        for element in self.__my_shapes:
            if element.get_color() == 'red':
                red_counter += 1
            if element.get_color() == 'black':
                black_counter += 1
            if element.get_color() == 'blue':
                blue_counter += 1
        colors = {'blue': blue_counter, 'red': red_counter, 'black': black_counter}
        return colors
