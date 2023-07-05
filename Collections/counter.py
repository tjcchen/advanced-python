#
# counter
# use case of dictionary - keep track of the count of individual items
#

from collections import Counter


def main():
    # list of students in class 1
    class1 = ["Bob", "Becky", "Chad", "Darcy", "Frank", "Hannah"
              "Kevin", "James", "James", "Melanie", "Penny", "Steve"]
    
    # list of students in class 2
    class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
              "Gabby", "Kellt", "James", "Joe", "Sam", "Tara", "Ziggy"]
    
    # create a counter for class1 and class2
    c1 = Counter(class1)
    c2 = Counter(class2)
    
    # how many students in class 1 named James?
    print(c1["James"]) # 2
    
    # how many students are in class 1?
    print(c1.keys()) # dict_keys(['Bob', 'Becky', 'Chad', 'Darcy', 'Frank', 'HannahKevin', 'James', 'Melanie', 'Penny', 'Steve'])
    print(c1.values()) # dict_values([1, 1, 1, 1, 1, 1, 2, 1, 1, 1])
    print(sum(c1.values()), "students in class 1") # 11 students in class 1
    
    # combine the two classes
    c1.update(class2)
    print(sum(c1.values()), "students in class 1") # 23 students in class 1
    
    # what's the most common name in the two classes?
    print(c1.most_common(3)) # [('James', 3), ('Frank', 2), ('Bob', 1)], top 3
    
    # separate the classes again
    c1.subtract(class2)
    print(c1.most_common(3)) # [('James', 2), ('Bob', 1), ('Becky', 1)]
    
    # what's common between the two classes?
    print(c1 & c2) # Counter({'Frank': 1, 'James': 1})


if __name__ == "__main__":
    main()
