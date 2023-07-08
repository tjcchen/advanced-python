#
# customize string representations of objects
#

class myColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # use getattr to dynamically return a value
    def __getattr__(self, attr):
        if attr == "rgbcolor":
            return (self.red, self.green, self.blue)
        elif attr == "hexcolor":
            return "#{0:02x}{1:02x}{2:02x}".format(
                self.red, self.green, self.blue
            )
        else:
            raise AttributeError

    # use setattr to dynamically return a value
    def __setattr__(self, attr, val):
        if attr == "rgbcolor":
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)

    # use dir to list the available properties
    def __dir__(self):
        return ("red", "green", "blue", "rgbcolor", "hexcolor")


def main():
    # create an instance of myColor
    cls1 = myColor()

    # print the value of computed attribute
    print(cls1.rgbcolor)  # (50, 75, 100)
    print(cls1.hexcolor)  # #324b64
    # print(cls1.rgb)  # AttributeError

    # set the value of a computed attribute
    cls1.rgbcolor = (125, 200, 86)
    print(cls1.rgbcolor)  # (125, 200, 86)
    print(cls1.hexcolor)  # #7dc856
    
    # access a regular attribute
    print(cls1.red)  # 125
    
    # list the available attributes
    print(dir(cls1))  # ['blue', 'green', 'hexcolor', 'red', 'rgbcolor']


if __name__ == "__main__":
    main()
