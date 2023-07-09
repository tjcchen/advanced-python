## Class String Functions

| String Function                          | Called When                                      |
| ---------------------------------------- | ------------------------------------------------ |
| object.\_\_str\_\_(self)                 | str(object), print(object), "{0}".format(object) |
| object.\_\_repr\_\_(self)                | repr(object)                                     |
| object.\_\_format\_\_(self, format_spec) | format(object, format_spec)                      |
| object.\_\_bytes\_\_(self)               | bytes(object)                                    |



## Class Attribute Functions

| Attribute Function                      | Called When       |
| --------------------------------------- | ----------------- |
| object.\_\_getattribute\_\_(self, attr) | object.attr       |
| object.\_\_getattr\_\_(self, attr)      | object.attr       |
| object.\_\_setattr\_\_(self, attr, val) | object.attr = val |
| object.\_\_delattr\_\_(self)            | del object.attr   |
| object.\_\_dir\_\_(self)                | dir(object)       |



## Class Numerical Operators

| Numeric Function                     | Called When    |
| ------------------------------------ | -------------- |
| object.\_\_add\_\_(self, other)      | self + other   |
| object.\_\_sub_\_(self, other)       | self - other   |
| object.\_\_mul_\_(self, other)       | self * other   |
| object.\_\_div_\_(self, other)       | self / other   |
| object.\_\_floordiv_\_(self, other)  | self // other  |
| object.\_\_pow_\_(self, other)       | self ** other  |
| object.\_\_and_\_(self, other)       | self & other   |
| object.\_\_or_\_(self, other)        | self \| other  |
| object.\_\_iadd\_\_(self, other)     | self += other  |
| object.\_\_isub_\_(self, other)      | self -= other  |
| object.\_\_imul_\_(self, other)      | self *= other  |
| object.\_\_itruediv_\_(self, other)  | self /= other  |
| object.\_\_ifloordiv_\_(self, other) | self //= other |
| object.\_\_ipow_\_(self, other)      | self **= other |
| object.\_\_iand_\_(self, other)      | self &= other  |
| object.\_\_ior_\_(self, other)       | self \|= other |



Data Modal Chapter: https://docs.python.org/3/reference/datamodel.html



## Class Comparison Operators

| Comparison Function           | Called When   |
| ----------------------------- | ------------- |
| object.\_\_gt_\_(self, other) | self > other  |
| object.\_\_ge_\_(self, other) | self >= other |
| object.\_\_lt_\_(self, other) | self < other  |
| object.\_\_le_\_(self, other) | self <= other |
| object.\_\_eq_\_(self, other) | self == other |
| object.\_\_ne_\_(self, other) | self != other |

