
```python
my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)
```

Given the above code, answer the following questions and explain your answers:

1. Are the lists assigned to my_list and another_list equal?

The lists are equal. They have the same values.

2. Are the lists assigned to my_list and another_list the same object?

The lists are not the same object. Another list is a new object because it was created with the list constructor.

3. Are the nested lists at index 3 of my_list and another_list equal?

Yes. The nested lists contain the same values and are equal.

4. Are the nested lists at index 3 of my_list and another_list the same object?

Yes. Nested lists are subject to shallow copies so they are equal.