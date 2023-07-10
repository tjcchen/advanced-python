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

