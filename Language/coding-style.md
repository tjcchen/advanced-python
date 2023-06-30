## Python Code Structure and Format

- Import statements go at the top, and each have their own line

- Indent code using spaces instead of tabs

- Use four spaces for each indentation level

- Limit lines to 79 characters (72 for docstrings/comments)

- Separate functions and classes by two blank lines

- Within classes, separate methods by one blank line

- No spaces around function calls, indexes, keyword arguments

  

## Python Whitespace Conventions

| Do                                    | Don't                                                 |
| ------------------------------------- | ----------------------------------------------------- |
| spam(ham[1], {eggs: 2})               | spam(ham[ 1 ], { eggs: 2 })                           |
| fn(arg)                               | fn (arg)                                              |
| dct["key"] = lst[index]               | dct ["key"] = lst [index]                             |
| x = 1<br/>y = 2<br/>long_variable = 3 | x         = 1<br/>y         = 2<br/>long_variable = 3 |
| hypot = x\*x + y\*y                   | hypot2 = x * x + y * y                                |
| i = i + 1                             | i=i + 1                                               |

