import rectangle


class Sqaure(rectangle.Rectangle):

    def __init__(self, color=0, height=0, width=0):
        super().__init__(color, height, width)

        def set_width(self, width):
            super(Sqaure, self).set_width(width)
            super(Sqaure, self).set_height(width)

        def set_height(self, height):
            super(Sqaure, self).set_width(height)
            super(Sqaure, self).set_height(height)

