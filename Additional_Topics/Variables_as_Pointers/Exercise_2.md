Without running this code, what will it print? Why?

```python
set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)
```
{42, 'Monty Python', ('a', 'b', 'c'), range(5,10)}

It will print the above. When set2 was set equal to set1, a new pointer was created for the set2 variable, that points to the same object that set1 points to. The object was then mutated using the set1 alias (variable). This mutated object is still the same object that set2 points to, so changes made to set1 through mutation will be reflected in set2.