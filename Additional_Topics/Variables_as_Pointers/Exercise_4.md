Without running this code, what will it print? Why?

```python
dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])
```

[1,42,3]

Because dict() initializes dict2 as a shallow copy of dict1, nested collections within dict1 have the same identity as those in dict2. Changing the value of an object in a nested collection in dict1 changes the value for dict2 as well because they point to the same object in memory.