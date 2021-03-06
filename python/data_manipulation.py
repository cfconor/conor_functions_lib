def stringify(*argv):
    """
    Takes one or more variables as arguments and returns a string containing the arguments
    """
    return_string = []

    for arg in argv:
        arg_string = str(arg)
        return_string.append(arg_string)

    return str(return_string)

print(stringify("hello ","world"))