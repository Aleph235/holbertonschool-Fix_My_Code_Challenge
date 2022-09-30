#!/usr/bin/python3
""" Documentation """


class square():
    """ Documentation """
    size = 0

    def __init__(self, *args, **kwargs):
        """ Documentation """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.size * self.size

    def PermiterOfMySquare(self):
        """ Documentation """
        return (self.size * 2) + (self.size * 2)

    def __str__(self):
        """ Documentation """
        return "{}/{}".format(self.size, self.size)


if __name__ == "__main__":

    s = square(size=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
