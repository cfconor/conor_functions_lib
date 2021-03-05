def stringify(*argv):
    """
    Takes one or more variables as arguments and returns a string containing the arguments
    """
    return_string = ""

    for arg in argv:
        arg_string = str(arg)
        return_string.join(arg_string)

    return return_string

print(stringify("hello ","world"))