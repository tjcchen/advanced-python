#
# advanced iteration functions in the itertools package
# documentation: https://docs.python.org/3/library/itertools.html
#

import itertools


def testFunction(x):
    return x < 40


def main():
    # cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "Andy", "Mike"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1)) # Joe
    print(next(cycle1)) # Andy
    print(next(cycle1)) # Mike
    print(next(cycle1)) # Joe
    
    # use count to create a simple counter
    count1 = itertools.count(100, 10)
    print(next(count1)) # 100
    print(next(count1)) # 110
    print(next(count1)) # 120
    
    # accumulate creates an iterator that accumulates values
    vals = [10, 20, 30, 40, 50, 40, 30]
    acc = itertools.accumulate(vals)
    print(list(acc)) # [10, 30, 60, 100, 150, 190, 220], acc is an itertools.accumulate object
    acc = itertools.accumulate(vals, max)
    print(list(acc)) # [10, 20, 30, 40, 50, 50, 50]
    
    # use chain to connect sequences together
    x = itertools.chain("ABCD", "1234")
    print(list(x))   # ['A', 'B', 'C', 'D', '1', '2', '3', '4']
    
    # dropwhile and takewhile will return values until a
    # certain condition is met that stops them
    result1 = itertools.dropwhile(testFunction, vals)
    result2 = itertools.takewhile(testFunction, vals)
    print(list(result1)) # [40, 50, 40, 30], drop the value when x < 40, based on index
    print(list(result2)) # [10, 20, 30], take the value when x < 40, based on index


if __name__ == "__main__":
    main()