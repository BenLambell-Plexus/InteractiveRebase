def add(*args):
    return sum(args)


def multiply(*args):
    if len(args) == 0:
        raise ValueError("Cannot multiply an empty list of values.")
    result = 1
    for arg in args:
        result *= arg
    return result
