#
# Demonstrate the use of variable argument lists
# Using variable arguments:
#   Define functions that can take variable number of parameters
#   1. def addition(*numbers)
#   2. def log_message(msgType, msg, *params)
#

# define a function that takes variable arguments
# signature - def addition(base, *args), if you decide to refactor your method,
# then all the reference methods should be changed
def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result


def main():
    # pass different arguments
    print(addition(1, 2, 3, 4)) # 10
    print(addition(5, 10, 15, 20)) # 50
    
    # pass an existing list
    myNums = [5, 10, 15, 20]
    # print(addition(myNums)) # TypeError: unsupported operand type(s) for +=: 'int' and 'list'
    print(addition(*myNums)) # 50


if __name__ == "__main__":
    main()
