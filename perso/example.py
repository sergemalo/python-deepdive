# import this
import sys
import ctypes
import string
import time

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
        return self._width   ### SEE HOW _width exists!!
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

def ref_count(addr: int):
    return ctypes.c_long.from_address(addr).value


class A:
    def __init__(self):
        self.i = 10
        self.t = (1, 2, 3)

class B:
    def __init__(self):
        self.i = 10
        self.t = (1, 2, 3, 4, 5)
a = A()
b = B()
#print ("A: {0}; B: {1}".format(sys.getsizeof(a), sys.getsizeof(b)))
#print ("A.t: {0}; B.t: {1}".format(sys.getsizeof(a.t), sys.getsizeof(b.t)))

def peep_hole():
    a = 24 * 60
    b = (1, 2)
    c = [3, 4] * 11
    d = {5, 6}

#print (peep_hole.__code__.co_consts)

ll = list(string.ascii_letters)
tt = tuple(string.ascii_letters)
ss = set(string.ascii_letters)

def membership_test(n, container):
    for i in range(n):
        if 'z' in container:
            pass

start = time.perf_counter()
membership_test(10000000, ll)
end = time.perf_counter()
print("result = ", end-start)

start = time.perf_counter()
membership_test(10000000, ss)
end = time.perf_counter()
print("result = ", end-start)
