What does the following function do? Be sure to identify the output value.

```python
def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))
```
The function sorts the dictionary keys in ascending order, indexes the second key, changes it to uppercase and returns it.

CHRIS