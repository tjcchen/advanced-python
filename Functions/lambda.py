#
# Lambda Functions - Use lambdas as in-place functions
# 1. Small, anonymous functions
# 2. Can be passed as arguments where you need a function
# 3. Typically used in place just when needed
# 4. Defined as:
#    `lambda (parameters) : (expression)`
# 


def CelsisusToFahrenheit(temp):
    return (temp * 9/5) + 32


def FahrenheitToCelsisus(temp):
    return (temp-32) * 5/9


def main():
    ctemps = [0, 12, 34, 100]
    ftemps = [32, 65, 100, 212]

    # use regular functions to convert temps
    results1 = map(FahrenheitToCelsisus, ftemps)
    results2 = map(CelsisusToFahrenheit, ctemps)
    print(list(results1)) # [0.0, 18.333333333333332, 37.77777777777778, 100.0]
    print(list(results2)) # [32.0, 53.6, 93.2, 212.0]

    # use lambdas to accomplish the same thing
    print(list(map(lambda t: (t-32) * 5/9, ftemps)))   # [0.0, 18.333333333333332, 37.77777777777778, 100.0]
    print(list(map(lambda t: (t * 9/5) + 32, ctemps))) # [32.0, 53.6, 93.2, 212.0]


if __name__ == "__main__":
    main()
