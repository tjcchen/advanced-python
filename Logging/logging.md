## Python Logging

- Captures and records events while app is running

- Useful debugging feature
  - Not always practical to debug in real time

- Events can be categorized for easier analysis

- Provides transaction record of a program's execution

- Highly customizable output



## Using the Logging Module

- import logging
- logging.debug("debug-level message")
- logging.info("info-level message")
- logging.warning("warning-level message")
- logging.error("error-level message")
- logging.critical("critical-level message")



## Logging Levels

| Message Level | Logging API        | Description                                           |
| ------------- | ------------------ | ----------------------------------------------------- |
| DEBUG         | logging.debug()    | Diagnostic information useful for debugging           |
| INFO          | logging.info()     | General information about program execution results   |
| WARNING       | loggin.warning()   | Something unexcepted, or an approaching problem       |
| ERROR         | logging.error()    | Unable to perform a specific operation due to problem |
| CRITICAL      | logging.critical() | Program may not be able to continue, serious error    |

logging.basicConfig(level=logging.DEBUG)



## Customized Logging

``js

basicConfig(

​	format=formatstr,

​	datefmt=date_format_str

)

``

| %(asctime)s   | Human readable date format when the log record was created   |
| ------------- | ------------------------------------------------------------ |
| %(filename)s  | File name where the log message originated                   |
| %(funcName)s  | Function name where the log message originated               |
| %(levelname)s | String representation of the message level (DEBUG, INFO, etc) |
| %(levelno)d   | Numeric representation of the message level                  |
| %(lineno)d    | Source line number where the logging cal was issued (if available) |
| %(message)s   | The logged message string itself                             |
| %(module)s    | Module name portion of the filename where the message was logged |







