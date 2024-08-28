Without running the following code, what does it print? Why?

```python
def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')
bar_code_scanner(142)
```
The code prints:
Product2
Product not found!

The first function call has '113' as the argument for the serial parameter. In the match statement, 113 will match the case that prints 'Product 2'. The second function call has an integer as input. None of the cases specified will match the integer 142, so the default case is evaluated, which prints 'Product not found!'. 
