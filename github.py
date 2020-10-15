def Sum(*args):
    All = 0
    for arg in args:
        if isinstance(arg, float) or isinstance(arg, int):
            All += arg
        else:
            raise ValueError("One or more inputs are not numbers!")
    return All

print (Sum(7, 9, 4))
