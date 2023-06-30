#
# demonstrate template string functions
# doc: https://docs.python.org/3/library/string.html#template-strings
# 

from string import Template

def main():
    # 1. usual string formatting with format()
    str1 = "You're watching {0} by {1}".format("Advanced Python", "Andy Chen")
    print(str1) # You're watching Advanced Python by Andy Chen
    
    # 2. create a template with placeholders
    templ = Template("You're watching ${title} by ${author}")
    
    # use the substitution method with keyword arguments
    str2 = templ.substitute(title="Advanced Python", author="Andy Chen")
    print(str2) # You're watching Advanced Python by Andy Chen
    
    # 3. use the substitute method with a dictionary
    data = {
        "author": "Andy Chen",
        "title": "Advanced Python"
    }
    str3 = templ.substitute(data)
    print(str3) # You're watching Advanced Python by Andy Chen

if __name__ == "__main__":
    main()
