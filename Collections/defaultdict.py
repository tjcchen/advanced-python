#
# defaultdict
#

from collections import defaultdict


def main():
    # define a list of items that we want to count
    fruits = ["apple", "pear", "orange", "banana",
              "apple", "grape", "banana", "banana"]

    # use a dictionary to count each element
    fruitCounter = {}
    # fruitCounter2 = defaultdict(str) # create default dict with empty string
    # fruitCounter2 = defaultdict(int) # create default value of integer for each key
    fruitCounter2 = defaultdict(lambda: 100) # counter starts with 100

    # solution1: count the elements in the list
    # error: KeyError: 'apple' (could be fixed with object key check first)
    for fruit in fruits:
        if fruit in fruitCounter.keys():
            fruitCounter[fruit] += 1
        else:
            fruitCounter[fruit] = 1

    # solution2: Count the elements in the list with defaultdict
    for fruit in fruits:
        fruitCounter2[fruit] += 1
 
    # print the result
    for (k, v) in fruitCounter.items():
        print(k + ": " + str(v))

    # print the result of defaultdict
    for (k, v) in fruitCounter2.items():
        print(k + ": " + str(v))


if __name__ == "__main__":
    main()
