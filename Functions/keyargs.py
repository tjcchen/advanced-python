#
# Keyword-only arguments
# - def myFunction(arg1, arg2, arg3="foo")
# - myFunction(1, 2, arg3="bar")
# - def criticalFunc(arg1, suppressExc=False)
# - def criticalFunc(arg1, *, suppressExc=False)
# 

# use keyword-only arguments to help ensure code clarity (recommended)
def myFunction(arg1, arg2, *, suppressException=False):
    pass


# without keyword-only argument, specifically *
def myFunction2(arg1, arg2, suppressException=False):
    print(suppressException)


def main():
    # try to call the function without the keyword
    # myFunction(1, 2, True) # TypeError: myFunction() takes 2 positional arguments but 3 were given
    
    myFunction(1, 2, suppressException=True) # pass
    
    myFunction2(3, 4, True) # True


if __name__ == "__main__":
    main()