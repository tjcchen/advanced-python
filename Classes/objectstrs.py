#
# customize string representations of objects
#

class Person():
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    # use __repr__ to create a string useful for debugging
    # with prop name specified, for debugging purpose
    def __repr__(self):
        return "<Person Class - fname:{0}, lname:{1}, age:{2}".format(
            self.fname, self.lname, self.age
        )

    # use str for a more human-readable string
    def __str__(self) -> str:
        return "Person ({0} {1} is {2})".format(
            self.fname, self.lname, self.age
        )

    # override the __bytes__ function,
    # otherwise we cannot use the bytes() conversion function 
    def __bytes__(self):
        val = "Person:{0}:{1}:{2}".format(
            self.fname, self.lname, self.age
        )
        return bytes(val.encode("utf-8"))


def main():
    # create a new Person object
    cls1 = Person("Andy", "Chen", 25)

    # use different Python functions to convert it to a string
    # if we don't override the default __repr__, __str__ method, the result will be somethine like:
    # <__main__.Person object at 0x10b40c390> | $<__main__.Person object at 0x10b40c390>
    print(repr(cls1))  # <Person Class - fname:Andy, lname:Chen, age:25
    print(str(cls1))   # Person (Andy Chen is 25)
    print("Formatted: {0}".format(cls1))  # Formatted: Person (Andy Chen is 25)
    print(bytes(cls1)) # b'Person:Andy:Chen:25'


if __name__ == "__main__":
    main()
