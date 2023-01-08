# import this
def my_func(a: int, b: int):
    print(
        """A
    A"""
    )
    return a * b


#my_func(2, "aaa")

def my_loop():
    i = 5
    while True:
        print(i)
        if i >= 5:
            break


sq = lambda x: x**2

def print_str(the_str):
    for i, c in enumerate(the_str):
        print (i, c)


class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self._height = h

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        else:
            self._width = value


    def __str__(self):
        return "Rectangle de {0} ar {1}".format(self._width, self._height)

    def __eq__(self, other):
        # Pas facile à lire, mais ça marche:
        return False if not isinstance(other, Rectangle) else (self.width, self._height) == (other.width, other._height)

    #def get_width(self):
    #    return self._width

    #def set_width(self, w):
    #    if w <= 0:
    #        raise ValueError("Width must be positive")
    #    else:
    #        self._width = w

r1 = Rectangle(1,2)
r2 = Rectangle(1,2)
