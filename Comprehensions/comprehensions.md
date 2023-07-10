## Python Comprehensions

- Make your list, dictionary, or set much easier to write and read

```js
list(map(FahrenheitToCelsius, [32, 65, 104, 212]))

->

[(t*9/5) + 32 for t in [32, 65, 104, 212]]
```
