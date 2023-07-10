#
# basic logging api in Python
#

import logging


def main():
    # use basicConfig to configure logging
    # note:
    # 1. if we don't set log level to DEBUG, then we are not able to see DEBUG and INFO logging information.
    # 2. logging.basicConfig will be called once only, later invocation to it won't affect the logging system.
    # 3. with filename specificed, we are going to append log information to output.log.
    # 4. the default filemode is `append` mode, but we can change it.
    logging.basicConfig(level=logging.DEBUG,
                        filename="output.log",
                        filemode="w")

    # try out each of the log levels
    logging.debug("This is a debug message")        # DEBUG:root:This is a debug message
    logging.info("This is a info message")          # INFO:root:This is a info message
    logging.warning("This is a warning message")    # WARNING:root:This is a warning message
    logging.error("This is a error message")        # ERROR:root:This is a error message
    logging.critical("This is a critical message")  # CRITICAL:root:This is a critical message
    
    # output formatted strings to the log
    # INFO:root:Here's a string variable and a int 10
    logging.info("Here's a {0} variable and a int {1}".format("string", 10))


if __name__ == "__main__":
    main()
