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
