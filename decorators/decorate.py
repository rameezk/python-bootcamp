def pretty(func):

    def wrapper():
        s = ""
        s += "========================================\n"
        s += f"==============   {func()}   ==============\n"
        s += "========================================\n"
        return s

    return wrapper


@pretty
def print_name():
    return "Rameez"


print(print_name())
