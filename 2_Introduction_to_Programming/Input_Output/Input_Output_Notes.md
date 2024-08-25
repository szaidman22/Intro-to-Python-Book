# Input/Output
8/25/24
___

Computers need to take input from a source and provide output.

Many things can be an import source, like mice, keyboards, disks, the network, environmental sensors, etc. Similarly, computers can write output to multiple locations, such as logs, screens and networks.

Computers can get input from other computers' output.

## Terminal Output

The *print* function is one way to display output in the terminal.

**Print**
- works with all data, often formatting the output in a way humans can read easily
- you can print multiple objects in a row by separating them with a comma
    - by default, multiple objects are separated by spaces.
    - you can include the *sep* keyword argument to specify a different separation character
- use the *end* keyword argument to define what prints after the last argument

```python
print(1, 2, 3, 'a', 'b', sep=',')      # 1,2,3,a,b
print('a', 'b', 'c', 'd', 'e', sep='') # abcde

>>> print(1, 2, 'a', 'b', sep=',', end=' <-\n')
1,2,a,b <-

>>> print('a', 'b', end='', sep=','); print('c', 'd', sep=',')
a,bc,d
```

- print() with no arguments starts a new line

## Terminal Input

- Instead of hard-coding, you can ask the user for input.
- **input()** function lets Python programs read input from the terminal.

### Example: greet the user by name

See personalized_greeting.py