#
# customize logging output
# 

import logging


extData = {
    "user": "andyc@example.com"
}


# add another function to log from
def anotherFunction():
    logging.debug("This is a debug-level message", extra=extData)


def main():
    # set the output file and debug level, and 
    # use a custom formatting specification
    fmtstr = "User:%(user)s %(asctime)s: %(levelname)s: %(funcName)s: Line:%(lineno)d %(message)s"
    datestr = "%m/%d/%Y %I:%M:%S %p"
    
    logging.basicConfig(filename="output2.log",
                        level=logging.DEBUG,
                        filemode="w",
                        format=fmtstr,
                        datefmt=datestr)
    
    # User:andyc@example.com 07/10/2023 05:05:23 PM: INFO: main: Line:31 This is an info-level log message
    logging.info("This is an info-level log message", extra=extData)
    # User:andyc@example.com 07/10/2023 05:05:23 PM: WARNING: main: Line:33 This is a warning-level message
    logging.warning("This is a warning-level message", extra=extData)
    
    # User:andyc@example.com 07/10/2023 05:05:23 PM: DEBUG: anotherFunction: Line:15 This is a debug-level message
    anotherFunction()
    
    
if __name__ == "__main__":
    main()
