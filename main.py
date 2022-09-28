from shape_storage import *

my_container = ShapeStorage()
my_container.generate(100)
print("total area:", my_container.sum_areas())
print("total perimeter:", my_container.sum_perimeter())
print("colors:", my_container.count_colors())
