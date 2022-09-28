import random

# color dictionary
color_num = {1: 'blue', 2: 'red', 3: 'black'}
from circle import *
from sqaure import *
from rectangle import *


class ShapeStorage:
    def __init__(self):
        self.__my_shapes = []

    def generate(self, x):
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
        sum = 0
        for element in self.__my_shapes:
            sum += element.get_area()
        return sum

    def sum_perimeter(self):
        perimeter = 0
        for element in self.__my_shapes:
            perimeter += element.get_perimeter()
        return perimeter

    def count_colors(self):
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
