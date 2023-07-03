#
# iterators - use iterator functions like enumerate, zip, iter, next
#

def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven"]
    
    # use iter to create an iterator over a collection (iter and next)
    i = iter(days)
    print(next(i))   # Sun
    print(next(i))   # Mon
    print(next(i))   # Tue
    
    # iterate using a function and a sentinel
    # sentinel means that when the line equals to a specific character,
    # it would exit the loop, in this case, an empty string
    # fp = file pointer
    with open("testfile.txt", "r") as fp:
        for line in iter(fp.readline, ""):
            print(line) # This is line 1 ... 6
            
    # use regular iteration over the days
    for m in days:
        print(m)            # Sun - Sat
        
    for m in range(len(days)):
        print(m+1, days[m]) # 1 Sun ... 7 Sat

    # using enumerate reduces code and provides a counter
    for i,m in enumerate(days):
        print(i, m)         # 0 Sun ... 6 Sat
    
    for i,m in enumerate(days, start=1):
        print(i, m)         # 1 Sun ... 7 Sat
        
    # use zip to combine sequences (return value is a tuple)
    for m in zip(days, daysFr):
        print(m)            # ('Sun', 'Dim'), ..., ('Sat', 'Sam')
    
    # note: the zip function will quit when the shorter sequence is exhausted
    # (when the two sequence does not have the same length)
    for i,m in enumerate(zip(days, daysFr), start=1):
        print(i, m[0], "=", m[1], "in French") # 1 Sun = Dim in French, ..., 6 Fri = Ven in French


if __name__ == "__main__":
    main()
