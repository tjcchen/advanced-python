## Python Truth Values

- False and None evaluate to false

- Numeric zero values: 0, 0.0, 0j

- Decimal(0), Fraction(0, x)

- Empty sequences/collections: "", (), [], {}

- Empty sets and ranges: set(), range(0)



| Boolean Operation | Result                               |
| ----------------- | ------------------------------------ |
| X and Y           | true if X and Y are both true        |
| X or Y            | true if either X or Y are true       |
| not X             | if X is false, then true, else false |



## Override Classes
```py
# the class will be evaluated to false
class myClass:
    def __bool__(self):
        return false

    def __len__(self):
        return false
```
