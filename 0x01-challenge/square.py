#!/usr/bin/python3
"""doc string"""


class square():
    """doc string"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """doc string"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """doc string"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """doc string"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
