Which of the following values can't be used as a key in a dict object, and why?

```python
'cat'
(3, 1, 4, 1, 5, 9, 2)
['a', 'b']
{'a': 1, 'b': 2}
range(5)
{1, 4, 9, 16, 25}
3
0.0
frozenset({1, 4, 9, 16, 25})
```

The set, list and dictionary can't be used as keys in the dictionary, because they are mutable and therefore not hashable.