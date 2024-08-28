# Flow Control
8/27/24

---

**Flow control**: controlling the flow of data inside a program.

## Conditionals

**Conditionals** represent a fork or forks in the road that data travels.
- use keywords **if, elif,** and **else**.

**Single block** if statement example:

```python
value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')
```

Adding an **else** block:

```python
value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')
else:
    print('value is NOT 3')
```
Note that the else block isn't its own statement - it is part of the if statement.

You can have nested if statements - if statments within an if statement, but that isn't recommended. Try to use elif or functions instead and keep nesting to a minimum.

Nested if example:

```python
value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')
else:
    if value == 4:
        print('value is 4')
    else:
        print('value is NOT 3 or 4')
```
This can be rewritten as:

```python
if value == 3:
    print('value is 3')
elif value == 4:
    print('value is 4')
else:
    print('value is NOT 3 or 4')
```

**Note** that elif blocks are evaluated in the order that they appear.

If you want to create a block in an if statement that does *nothing* you can use a **pass statement**. This is usually for readability purposes. It is good practice to add a comment explaining the pass statement.

Example of a **pass statement**:

```python
if value == 3:
    print('value is 3')
elif value == 4:
    print('value is 4')
elif value == 9:
    pass # We don't care about 9
else:
    print('value is something else')
```

## Comparisons

Recall that comparison operators compare two **operands** and return True or False.

**Note**: when comparing strings that might have a mix of cases, use the **casefold()** function rather than upper or lower. It removes case instead, and allows you to compare some special characters in other languages better.

**Operators to know and review**:
- equality ==
- inequality !=
- < and <=
- > and >=

## Logical Operators

- **not, and** and **or**

### not

Returns True when its operand is False and False when the operand is True. It negates its operand.

```python
print(not True)           # False
print(not False)          # True
print(not(4 == 4))        # False
print(not(4 != 4))        # True
```

- best practice to use parentheses as in the last two examples so as not to confuse yourself.

- **not** takes a single operand, making it a **unary operator**.

### and & or

- **and** returns True if both operands are True, False if either is False
- **or** returns True if either operand is True, False only if both are False

## Short Circuits

**and** and **or** use a mechanism called **short circuit evaluation** to evaluate their operands. 
- this means that Python terminates the expression early if it can already determine that it will evaluate to True or False based on the first operand before the second operand is evaluated. 

## Truthiness

**Truthy** and **falsy** are terms that describe how specific objects behave in a Boolean context.

Conditionals only care about truthiness - it's what they use to determine which block runs and if criteria are met. They don't need to produce Boolean values.

**Built-in falsy values:**
- *False* and *None*
- all numeric 0 values (integers, floats and complex)
- empty strings
- empty collections
custom data types can also define built-in falsy values

**Everything else is truthy**

Example:

```python
value = 5                     # 5 is truthy
if value:
    print(f'{value} is truthy')
else:
    print(f'{value} is falsy')
```
### Truthiness and short-circuit evaluation

**and** and **or** logical operators don't always return True or False. They care only about the truthiness of their operands.

If you want to have a logical expression that returns a non-Boolean object like this:

```python
foo = None
bar = 'qux'
is_ok = foo or bar
```

it is best practice to rewrite as this for clarity:

```python
is_ok = bool(foo or bar)
```

(you could also write an if/else statement but that would be wordier)

## Logical Operators and Precedence

Python has **precedence** rules for evaluating expressions that use multiple operators and sub-expressions.

Precedence rules (top having higher precedence):

- ==, !=, <=, <, >, >= (comparison)
- not (logical NOT)
- and (logical AND)
- or (logical OR)

**just for fun** figure out what these logical expressions return:
```python
print(1 or 2 and 3) # 2 and 3 returns 3, 1 or 3 returns 1.
print(0 or 2 and 3) # 2 and 3 returns 3, 0 or 3 returns 3.
print(1 or 0 and 3) # 0 and 3 returns 0, 1 or 0 returns 1. 
print(1 or 2 and 0) # 2 and 0 returns 0, 1 or 0 returns 1. 
print(0 or 0 and 3) # 0 and 3 returns 0, 0 or 0 returns 0.
print(0 or 2 and 0) # 2 and 0 returns 0, 0 or 0 returns 0.
print(1 or 0 and 0) # 0 and 0 returns 0, 1 or 0 returns 1. 
print(0 or 0 and 0) # 0 and 0 returns 0, 0 or 0 returns 0.

print(1 and 2 or 3) # 1 and 2 returns 2, 2 or 3 returns 2. 
print(0 and 2 or 3) # 0 and 2 returns 0, 0 or 3 returns 3. 
print(1 and 0 or 3) # 1 and 0 returns 0, 0 or 3 returns 3.
print(1 and 2 or 0) # 1 and 2 returns 2, 2 or 0 returns 2. 
print(0 and 0 or 3) # 0 and 0 returns 0, 0 or 3 returns 3.
print(0 and 2 or 0) # 0 and 2 returns 0, 0 or 0 returns 0.
print(1 and 0 or 0) # 1 and 0 returns 0, 0 or 0 returns 0.
print(0 and 0 or 0) # 0 and 0 returns 0, 0 or 0 retunrs 0.
```
**Use parentheses** to control the order of evaluation if you are combining operators. 

## match/case Statement (aka match statement)

A **match** statement in its most basic form is similar to an if statement. However, it compares a single value against multiple values, whereas if can test multiple expressions with any condition.
- it was introduced in Python 3.10.
- it's basically like a case statement in SQL

example:

```python
value = 5

match value:
    case 1 | 2 | 3 | 4:
        print('value is < 5')
    case 5 | 6:
        print('value is 5 or 6')
    case _: # default case
        print('value is not 1, 2, 3, 4, 5, or 6')
# value is 5 or 6
```

## Ternary Expressions

The official name is *conditional expression*, sometimes called *ternary operator*, but it's not an operator. Launch school calls them **ternary expressions**. 

**Ternary expressions** provide a conscise way to choose between two values based on a condition.

example:

```python
value1 if condition else value2
```

If condition is truthy, value1 is returned. If it is falsy, value2 is returned. 

This:

```python
if shape.sides() == 3:
    print("Triangle")
else:
    print("Square")
```

is the same as this:

```python
print("Triangle" if shape.sides() == 3 else "Square")
```
Ternary expressions aren't always the right way to go for readability, but they can be useful in the right context.