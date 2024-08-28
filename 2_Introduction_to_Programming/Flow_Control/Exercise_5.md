What does this code output, and why?

```python
def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])
```

This code will return 'Empty'.

The function has been called with an empty list as the argument for the my_list paramenter. if my_list evaluates to False. The empty list is falsy, so the first condition has not been met, and the else statement will be evaluated, which prints 'Empty'.