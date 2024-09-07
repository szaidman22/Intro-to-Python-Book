# More Stuff

9/7/2024

---

## Function Composition

**Composition** occurs when a function call is uses as an argument for another function:

```python
print(list(range(3, 17, 4)))
```
Composition works best when all inner functions return an object besides None. 

Make sure it's understandable when you do this.

## Method Chaining

Good methods tend to only carry out one task (e.g. str.upper, str.split).

**Method chaining** is connecting methods one after another to carry out multiple tasks:

```python
tv_show = "Monty Python's Flying Circus"
tv_show = tv_show.upper().split()
# ['MONTY', "PYTHON'S", 'FLYING', 'CIRCUS']
```

You can multi-line format code for understandability if you use method chaining of several methods:

```python
letters = 'abcdefghijklmnoqrstuvwxyz'

# Note that the parentheses surrounding this
# multi-line chain are required.
consonants = (letters.replace('a', '').
                      replace('e', '').
                      replace('i', '').
                      replace('o', '').
                      replace('u', ''))
print(consonants)    # bcdfghjklmnqrstvwxyz
```

Best to keep things simple and limit very long method chains.

## Modules

You import modules that contain functions with import statements:

```python
import math

print(math.sqrt(math.pi))   # 1.7724538509055159
```

If you want to use functions from math without writing math, you can do it with a from statement:

```python
from math import pi, sqrt

print(sqrt(pi))             # 1.7724538509055159
```

and you can use an alias:

```python
import math as m

print(m.sqrt(m.pi))         # 1.7724538509055159
```

### Useful modules:
- math (for sqrt, etc.)
- datetime (for all date handling)
    - (see book for details)

## Function Definition Order

In Python, programmers usually define functions at the beginning of the program, then write the meat of the program.

As long as a function is defined before it is called, all is well.

## Nested Functions

You can write functions within functions.

## The global and nonlocal Statements

You can use Python's global and nonlocal stuatements to change the scope of a variable:

```python
greeting = 'Salutations'

def well_howdy(who):
    global greeting
    greeting = 'Howdy'
    print(f'{greeting}, {who}')

well_howdy('Angie')
print(greeting)
```
prints 

Howdy, Angie
Howdy

**nonlocal** will move the variable up one level, while global makes the variable global.

Using global and nonlocal is *rarely* required.
