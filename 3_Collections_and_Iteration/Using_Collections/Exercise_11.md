Without running the following code, determine what each line should print.

```python
print('johnson' in 'Joe Johnson')
print('sen' not in 'Joe Johnson')
print('Joe J' in 'Joe Johnson')
print(5 in range(5))
print(5 in range(6))
print(5 not in range(5, 10))
print(0 in range(10, 0, -1))
print(4 in {6, 5, 4, 3, 2, 1})
print({1, 2, 3} in {1, 2, 3})
print({3, 2} in {1, frozenset({2, 3})})
```
false
true
true
false
true
false
false
true
true **wrong, this is false** "in with sets only checks whether a specific value is in the set."
true