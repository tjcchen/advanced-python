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

