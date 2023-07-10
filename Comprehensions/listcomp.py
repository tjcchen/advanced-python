#
# list comprehensions
#


def main():
    # define two lists of numbers
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # perform a mapping and filter function on a list
    evenSquared = list(map(lambda e: e**2, evens))
    print(evenSquared)  # [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
    evenSquared2 = list(
        map(lambda e: e**2, filter(lambda e: e > 4 and e < 16, evens)))
    print(evenSquared2)  # [36, 64, 100, 144, 196]

    # derive a new list of numbers from a given list
    evenSquared3 = [e ** 2 for e in evens]
    print(evenSquared3)  # [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

    # limit the items operated on with a predicate condition
    oddSquared = [e ** 2 for e in odds if e > 3 and e < 17]
    print(oddSquared)  # [25, 49, 81, 121, 169, 225]


if __name__ == "__main__":
    main()
