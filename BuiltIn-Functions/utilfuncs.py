#
# util functions - demonstrate built-in utility functions
# 

def main():
    # use any() and all() to test sequences for boolean values
    list1 = [1, 2, 3, 0, 5, 6]
    
    # any will return true if any of the sequence values are true
    print(any(list1)) # True
    
    # all will return true if all values are true
    print(all(list1)) # False, since 0 evaluates as false
    print(all([1, 2, 3, 4, 5, 6])) # True
    
    # min and max will return minimum and maximum values in a sequence
    print("min: ", min(list1)) # 0
    print("max: ", max(list1)) # 6
    
    # use sum() to sum up all of the values in a sequence
    print("sum: ", sum(list1)) # 17

if __name__ == "__main__":
    main()
