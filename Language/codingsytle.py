#
# Language Features
#

# imports go on their own lines
import datetime
import platform


# two blank lines separate classes from other functions
class MyClass():
    def __init__(self):
        self.prop1 = "my class"
        self.now = datetime.datetime.now()
        
    # within classes, one blank line separates methods
    def function_name(self, use_name):
        # Darwin Kernel Version 20.6.0: Mon Aug 30 06:12:21 PDT 2021;
        # root:xnu-7195.141.6~3/RELEASE_X86_64
        print(platform.version())
        if use_name:
            print(use_name) # True


# long comments, like this one that flow accross sereral lines, are
# limmited to 72 characters instead of 79 for lines of code.
cls1 = MyClass()
cls1.prop1 = "Hello Python"
cls1.function_name(True)
