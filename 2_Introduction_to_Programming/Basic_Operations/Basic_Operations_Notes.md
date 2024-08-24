# Basic Operations
8/24/24

---
**Built-in types**: data typeps that are available in every program. Part of Python.

**Standard types**: not automatically loaded when running Python. Available from modules you can import.

**Non-standard types**: any other type made by yourself or colleagues or as downloadable modules on the internet.


## Arithmetic Operations

| Symbol | Operation |
|--------|-----------|
| \+ | Addition  |
| \- | Subtraction|
| * | Multiplication |
| / | Division |
| // | Integer Division |
| % | Modulo |
| ** | Exponentiation |

These work with built-in integer and float types, in addition to other numeric types. 

- Dividing with / , always returns a float
- // integer division always returns the largest whole number <= the floating point result.
    - if either operand is a float, returns a float (but a whole number), otherwise returns an integer
    - // doesn't work with the built-in complex numbers

- **Modulo** returns what is called the "modulus" of a division.
    - like a remainder but not exactly
    - can be used to check for divisibility i.e. x % y == 0
    - doesn't work with the built-in complex numbers

### Floating Point Imprecision

- .1 + .2 isn't exactly equal to .3 for some reason
    - artifact of how real numbers are stored on most computers
    - poses issues for some things like finance
    - you can use the math.isclose function to get around this
    - or you can use the decimal.Decimal type

```python
import math
math.isclose(0.1 + 0.2, 0.3)  # True

from decimal import Decimal
Decimal('0.1') + Decimal('0.2') == Decimal('0.3')  #True
```
## Equality Comparison

== and !=

- work with almost all data types
- all built in and standard number types can be compared for equality regardless of specific type, e.g. you can compare ints and floats.
- comparing different data types that aren't numbers for equality gets less predictable, usually are not equal.
- unpredictable when using standard and non-standard data types.

## Ordered Comparisons

- < , > , <= , >=

- Strings are compared **lexicographically**, meaning they are compared **charcter by character, left to right**
- shorter strings are considered smaller than longer strings (if equal up to where the shorter string ends)
- all upper-case letters are considered to be less than a;; lowercase letters
- numeric characters are less than alphabetic characters
- other characters are a tossup
- based on this [standard ASCII table]('https://www.ascii-code.com/ASCII')
- you can compare sets to see if a set is a subset or superset of another set
- can compare lists and tuples
    - will go element by element

## String Concatenation

- uses \+ and * to join strings
- * performs **repetitive concatenation**

```python
print('abc' * 3)              # 'abcabcabc'
print(3 * 'abc')              # 'abcabcabc'
```
## Coercion

- **type coercion** changes an object's type
- *int* and *float* functions coerce a string to a number
- *str* coerces a number (or other values) to a string

### Implicit coercions

- using functions str, int, etc. is someitimes called **explicit coercion**
- **implicit coercion** happens behind the scenes when using some functions, such as *print()*.
- implicit coercion can also occur when mixing numbers of different types in expressions:

| Type A | Type B | Type C |
|--------|--------|--------|
| int | float | float |
| int | Decimal | Decimal |
| int | Fraction | Fraction |
| float | Decimal | --error-- |
| float | Fraction | float |
| Decimal | Fraction | --error-- |

- Boolean values True and False coerce to 1 and 0 in mathematical expressions

## Determining Types

- good for debugging
- use the *type* function
- if you just want the class name to be returned, access only the __ name __ property:

```python
print(type('abc').__name__)   # str
print(type(False).__name__)   # bool
print(type([]).__name__)      # list
```
- you can use *type* with the *is* operator, which will return True or False

```python
print(type('abc') is str)     # True
print(type('abc') is int)     # False
print(type(False) is bool)    # True
print(type([]) is list)       # True
print(type([]) is set)        # False
```
- you can use the *isinstance* function to see if an object is an instance of a particular type, which is useful for determining *inheritance* which is not discussed in this book (is discussed in the Object Oriented Programming book later).

## String Representations

- *str* and *repr* each return a string representation of an object
- however, *repr* returns a string that can be used to create a new instance of the object

```python
my_str = 'abc'
print(my_str)       # abc
print(str(my_str))  # abc (same as print(my_str))
print(repr(my_str)) # 'abc' (note the quotes)
```
## Collection and String Lengths

- all built-in collection types have lengths.
- string = character length, other collections' length is the number of elements in the collection
- use *len* function

## Indexing and Key Access

- **strings, ranges, lists, and tuples** support indexed access to indidvidual elements in the collection.
- indices start at 0 and go to len(object) - 1
- **dictionaries** use keys that work similarly to indexes, but keys are *not* indexes

### Using [] to update elements

- b/c they are mutable, **lists and dictionaries** let you use [] to replace collection elements 
- strings, ranges, tuples and frozen sets are immutable so you can't use [] to replace elements
- sets are mutable but don't support indexing, so can't use either

## Expressions and Statements

- there is a fundamental distinction b/w statements and expressions in Python

**Expressions** combine values, variables, operators and calls to function to **produce a new object**.
- examples include:
    - literals,
    variable references, arithmetic operations, comparisons, string operations, function calls
    - any combo of the above that evaluates to a single object

An expression is something that **produces a value** that can be assigned to a variable, passed to a function or method, or returned by a function or method.

**Statements** are instructions that tell Python to perform an action of some kind. They **don't return values**. 
- examples include:
    - Assignment (x = 5)
    - control flow (e.g. if, else, while , for)
    - function and class definitions using *def* or *class*
    - return *statements* in functions
    - import statements

*The key differences:*
- Expressions always return a value; statements do not
- expressions are often part of statements
    - y = x + 5; x + 5 is an expression
- statements often represent bigger chunks of functionality like loops or conditionals; expressions deal with determining values

**Note**: some expressions are stand-alone. They aren't part of an ordinary statement, but their return value is ingored. They are in a gray area. At Launch school they are considered expressions and statements. They are:

```python
3 + 4            # Simple expression
print('Hello')   # Function call; returns None
my_list.sort()   # Method call; returns None
```

## Express Evaluation

- Python evaluates most expressions left to right.
- Python uses order of evaluation with multiplication/division first left to right and then addition/subtraction left to right
- you shouldn't rely on this though, you should **always** use parentheses to be explicit about your intent.

## Output vs. Return Values

- **log** is a term often used as a synonym for printing or showing something on the display.
- in many cases, your code doesn't have an output; it has a return value. This is returned in the REPL so that you know the expression returned a value, but it will not be output unless you print it. 