#
# use special methods to compare objects to each other
#


class Employee():
    def __init__(self, fname, lname, level, yrsService):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = yrsService

    # implement comparison functions by emp level
    def __ge__(self, other):
        if (self.level == other.level):
            return self.seniority >= other.seniority
        return self.level >= other.level

    def __gt__(self, other):
        if (self.level == other.level):
            return self.seniority > other.seniority
        return self.level > other.level

    def __lt__(self, other):
        if (self.level == other.level):
            return self.seniority < other.seniority
        return self.level < other.level

    def __le__(self, other):
        if (self.level == other.level):
            return self.seniority <= other.seniority
        return self.level <= other.level

    def __eq__(self, other):
        if ((self.level == other.level) & (self.seniority == other.seniority)):
            return True
        return False


def main():
    # define some employees
    dept = []
    dept.append(Employee("Tim", "Sims", 5, 9))
    dept.append(Employee("John", "Doe", 4, 12))
    dept.append(Employee("Jane", "Smith", 6, 13))
    dept.append(Employee("Rebecca", "Robinson", 5, 13))
    dept.append(Employee("Tyler", "Durden", 5, 12))
    dept.append(Employee("Andy", "Chen", 5, 12))

    # who's more senior?
    print(dept[0].level, dept[2].level, dept[0] > dept[2])  # 5, 6, False
    print(dept[4].level, dept[3].level, dept[4] < dept[3])  # 5, 5, True, compare both level and seniority
    print(dept[5].level, dept[4].level, dept[4] == dept[5])  # 5 5 True
    
    # sort the items
    emps = sorted(dept)
    for emp in emps:
        print(emp.lname) # Doe, Sims, Durden, Chen, Robinson, Smith - based on level and seniority


if __name__ == "__main__":
    main()
