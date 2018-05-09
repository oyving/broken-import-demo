
def add():
    from .a import x as a
    from .b import x as b
    from .c import x as c
    return a + b + c

x = add()

