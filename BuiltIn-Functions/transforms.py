#
# transforms - use transform functions like sorted, filter, map
# 

# filter out the even number from the numbers
def filterFunc(x):
    # return x % 2 != 0
    if x % 2 == 0:
        return False
    return True


# filter out the upper case of characters
def filterFunc2(x):
    # if x.islower():
    #     return True
    # return False
    if x.isupper():
        return False
    return True


# map a number to its square format (powers of 2)
def squareFunc(x):
    return x**2


# transform grades to letter format
def toGrade(x):
    if (x >= 90):
        return "A"
    elif (x >= 80 and x < 90):
        return "B"
    elif (x >= 70 and x < 80):
        return "C"
    elif (x >= 60 and x < 70):
        return "D"
    else:
        return "F"


def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74, 58)
    
    # use filter to remove this items from a list
    odds = list(filter(filterFunc, nums))
    print(odds)    # [1, 5, 13, 381, 47]
    
    # use filter on non-numeric sequence
    lowers = list(filter(filterFunc2, chars))
    print(lowers)  # ['a', 'b', 'c', 'e', 'i', 'k', 'l', 'm', 'n', 'o']
    
    # use map to create a new sequence of values
    squares = list(map(squareFunc, nums))
    print(squares) # [1, 64, 16, 25, 169, 676, 145161, 168100, 3364, 2209]
    
    # use sorted and map to change numbers to grades
    grades = sorted(grades) 
    letters = list(map(toGrade, grades))
    print(grades)   # [58, 61, 66, 74, 78, 81, 89, 94, 99]
    print(letters)  # ['F', 'D', 'D', 'C', 'C', 'B', 'B', 'A', 'A']
    

if __name__ == "__main__":
    main()
