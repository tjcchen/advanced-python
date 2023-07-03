#
# Demonstrate the use of function docstrings
# Examples of checking docstrings:
#   1. print(map.__doc__)
#   2. import collections
#      print(collections.__doc__)
#
# Documentation: https://peps.python.org/pep-0257/
#


def myFunction(arg1, arg2=None):
    """myFunction(arg1, arg2=None) --> Doesn't really do anything, just prints.
    
    Parameters:
    arg1: the first argument. Whatever you feel like passing.
    arg2: second argument. Defaults to None.
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__) # would print the above function doc


if __name__ == "__main__":
    main()
