#!/usr/bin/python3
"""doc string"""


class Square():
    """doc string"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """doc string"""
        for key, value in kwargs.items():
            if value > 0:
                setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """doc string"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """doc string"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """doc string"""
    s = Square(width=-12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
