#
# set comprehensions
#

def main():
    # define a list of temperature data points
    ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]
    ftemps1 = [(t*9/5)+32 for t in ctemps]
    # [41.0, 50.0, 53.6, 57.2, 50.0, 73.4, 105.8, 86.0, 53.6, 75.2, 53.6, 64.4, 84.2]
    print(ftemps1)

    # build a set of unique Fahrenheit temperatures
    ftemps2 = {(t*9/5)+32 for t in ctemps}
    # {64.4, 73.4, 41.0, 105.8, 75.2, 50.0, 84.2, 53.6, 86.0, 57.2}, set weeped out the duplicated temps
    print(ftemps2)

    # build a set of from input source
    sTemp = "The quick brown fox jumped over the lazy dog"
    chars = {c.upper() for c in sTemp if not c.isspace()}
    # {'E', 'U', 'B', 'P', 'C', 'I', 'J', 'D', 'H', 'K', 'G', 'X', 'M', 'Q', 'F', 'L', 'Y', 'N', 'W', 'Z', 'T', 'R', 'V', 'O', 'A'}
    print(chars)


if __name__ == "__main__":
    main()
