"""
Author: Talya Gross
Object Oriented Programming- project
"""
from shape_storage import *
from sqaure import Sqaure

my_container = ShapeStorage()
my_container.generate(100)
print("total area:", my_container.sum_areas())
print("total perimeter:", my_container.sum_perimeter())
print("colors:", my_container.count_colors())

rectangle = Rectangle('red', 2, 4)
square = Sqaure('red', 2, 6)
print(rectangle.add(square).get_width())
