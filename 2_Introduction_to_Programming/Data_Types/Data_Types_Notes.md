# Data Types
8/21/24

---

### Object: Everything with a value in python
- each object has an associated data type aka a type
- each type has an associated class

*Object* & *Value* can be used interchangeably

*Class*, *Type*, and *Data Type* can be used interchangeably

### Primitive data types
- fundamental types
- almost all data in a language is built from these types
- int, float, bool, str, none (maybe)

### Collection Types:
- data types that collect multiple items in a single object
- lists, sets, etc.

Functions are not collections, they are their own special thing

### Literals: any syntactic notation that lets you directly represent an object in source code

```python
'Hello world'  #string literal
3.14156  #float literal
True  #bool literal
{'a':1,'b':2,'c':3}  #dict literal
[1,2,3]  #list literal
(4,5,6)  #tuple literal
{7,8,9}  #set literal
```
Not all objects have literals

We can use the type constrcutor to create objects of types that don't have literals:

```python
range(10)  #gives a range from 0-9
range(1,11)  #gives a range from 1 to 11
set()  #creates an empty set
frozenset([1,2])  #frozen set of values 1 and 2
```
### Numeric Values: represent numbers
- **int**: integers; whole numbers; not decimals
  - you can use underscores to break these up; commas won't work
  - e.g. a million would be 1_000_000 if you want to break it up
- **float**: floating point numbers aka decimals and can be integers as well
  - note that floats use scientific notation for large numbers and ints do not

### Variables: names to identify values.
- aka **Identifiers**
    - more general term that applies to constants, function names, list names etc.
- created by **initializing** to a value
- the term for the syntax used when creating variables is **assignment**

```python
foo = 'abc'  #we can say the variable foo is asinged the value 'abc'
```
- we can also say the reverse, the value 'abc' is assigned to the variable foo, but the first way is preferred by Launch School
- the first variable assgnment is **initialization**
- any subsequent assignment of the same variable name is called **reassignment**

### Boolean Values
- represent binary states such as true or false, on or off, yes or no, one or zero etc.
- the only Boolean values are True or False
- can be used as numbers True = 1 and False = 0

### Text Sequences: strings of characters
- **String**: a sequence of unicode characters
- text sequences do not contain objects, they only contain characters (bytes)
- you can write string literals with single, double, or triple quotes
- you can index strings

```python
my_str = 'abc'
my_str = "abc"
my_str = '''abc'''

my_str[1]  #this will return 'b'
```
- you can escape quote characters within a string if you need to:

```python
print("my name is \"Sofia\".")  #prints: my name is "Sofia".
```
- backslash is the **escape character**
- to use an actual backslash in a string, you must double it or use a **raw string literal**:

```python
print("c:\\users\\xyz")
# or
print(r"C:\users\xyz")  #raw string literal
```
- **raw string literals** are string literals with prefix r
    - don't recognize escapes

### Formatted string literals: aka f-strings

- enable **string interpolation** operation
- use prefix f

```python
print(f'5 plus 5 equals {5+5}')  # prints: 5 + 5 equals 10

my_name = 'Sofia'
print(f'my name is {my_name}')  #prints: my name is Sofia

print(f'{{foo}} is {5 + 5}')  #prints: {foo} is 10
```
- allows you to add expressions into strings
python **interpolates** the espression's value
- double the bracket character if you want to use it as a literal in an f-string


you can use f-strings to print formatted numbers

```python
print(f'{1000000:,}')  # 1,000,000

print(f'{1000000:_}')  # 1_000_000
```

### None
- literal whose value is the lone representative of the **nonetype** class.

### Sequences: an ordered collections of objects
- ordered lists can be a **list** or a **tuple**
- list literals use square brackets
- tuple literals use parentheses

```python
my_list = [1, 'xyz', True, [2,3,4]]

tup = ('xyz', [2,3,4], 1, True)
```
Both can contain a mix of element types.

They may also use multi-line format which is useful for extensive or nested lists:

```python
[ # Begin multi-line list literal
    "Monty Python's Flying Circus",
    ( # Begin multi-line tuple literal
      'Eric Idle',
      'John Cleese',
      'Terry Gilliam',
      'Graham Chapman',
      'Michael Palin',
      'Terry Jones',
    ), # End multi-line tuple literal
] # End multi-line list literal
```
- note the trailing comma on the last item is optional but a common best practice. If you use it be consistent.

You can use **indexing** to access the objects in a list/tuple. 
- the value between the brackets must be an integer between 0 and length of list/tuple - 1.

**Crucial distinction between lists and tuples**: lists are *mutable* and tuples are *immutable*.
- you can mutate a list by using indexing syntax to the left of the = sign in an assignment.
- this is called **indexed reassignment** or **element reassignment**

```python
my_list = ['sofia','is','nice']
my_list[2] = ['good']
print(my_list)  # ['sofia','is','good']
```
### Ranges: sequences of numbers between two endpoints
- most commonly used to iterate over an increasing or decreasing range of integers

```python
>>> tuple(range(5))
(0, 1, 2, 3, 4)

>>> tuple(range(5, 10))
(5, 6, 7, 8, 9)

>>> list(range(1, 10, 2))
[1, 3, 5, 7, 9]

>>> list(range(0, -5, -1))
[0, -1, -2, -3, -4]
```
- with one argument, the range starts from 0 and ends one before the argument
- with two arguments, the first argument is the starting point and the second argument is one past the last integer
- with three arguments, the third argument is the step value
    - a negative step value will cause the range to go from the highest to lowest value

You can convert a range to a list or tuple to save the numbers within. 

You can index a range:

```python
>>> my_range = range(5, 10)
>>> my_range[3]               # 8
```

### Mappings: unordered collections of objects stored as key-value pairs

- each key (usually a string) provides a *unique identifier* for a specific object in the mapping.
- the *value* of the object is associated with that *key*.
- **dictionary (dict)** class is the most common mapping in python. It is a collection of *key-value pairs*.
    - similar to a list but uses keys rather than indexing to access specific elements.
    - other languages have similar structures with different names (e.g. hashes, mapping, objects, associative arrays)

To create a dict literal, key-value pairs are separated by commas. The key is followed by a semi-colon, which is followed by the value. Everything is surrounded by curly brackets:

```python
my_dict = {
    'dog': 'woof',
    'cat': 'meow',
    'mouse': 'squeek',
}
```
Can use multi-line format:

```python
my_dict = {
    'title': "Monty Python's Flying Circus",
    'cast': [
        'Eric Idle',
        'John Cleese',
        'Terry Gilliam',
        'Graham Chapman',
        'Michael Palin',
        'Terry Jones',
    ],
    'first_season': 1969,
    'last_season': 1974,
    'reboot_season': None,
}
```
Use the [] key access syntax to access objects in a dict. The value between the brackets must be a key.

```python
my_dict['cat']  # 'meows'
```
You can use the same key access syntax on the left side of an assignment to reassign the key:

```python
my_dict['cat'] = 'nudge'

my_dict # {'dog': 'barks', 'cat': 'nudge', 'mouse': 'squeek'}

```

As of Python 3.7, **insertion order is preserved** in dictionaries. That is, dictionaries are ordered based on the order that key-value pairs were entered. 

Special note: you can use almost any *immutable* object as a key in a dict; not just a string. The only significant reuirement is that the key is **hashable** (discussed in PY110 course).

### Sets: unordered collections of unique objects.
- objects are sometimes referred to as **members** of the set.
- a collection of *immutable* and hence *hashable* objects
    - makes them somewhat similar to mappings
- support operations corresponding to mathematical sets (beyond scope of this book)

Set literal syntax is a comma-separated list of values between curly brackets. Because {} is used to create an empty dictionary, you must use the set constructor to make an empty set:

```python
>>> d1 = {}         # Empty dict
>>> print(type(d1))
<class 'dict'>

>>> s1 = set()      # Empty set
>>> print(s1)
set()

# Create a set from a literal
>>> s2 = {2, 3, 5, 7, 11, 13}
>>> print(s2)
{2, 3, 5, 7, 11, 13}

# Create a set from a string
>>> s3 = set("hello there!")
{'t', 'o', 'e', 'l', ' ', 'h', '!', 'r'}
```
Set members are always unique, even if you try to add duplicates. They are unordered.

Set literals can use the multi-line format.

**Frozen sets (frozenset)** are just immutable sets.
- frozen sets don't have their own literal syntax, so you use the frozenset function to create one.
- you can intialize a frozen set with any *iterable type* (list, tuple, set, range):

```python
>>> s5 = frozenset([1, 2, 3])
>>> print(s5)
frozenset({1, 2, 3})

>>> s6 = frozenset((1, 2, 3))
>>> print(s6)
frozenset({1, 2, 3})

>>> s7 = frozenset({1, 2, 3})
>>> print(s7)
frozenset({1, 2, 3})

>>> s8 = frozenset(range(1, 4))
>>> print(s8)
frozenset({1, 2, 3})
```
Items in a set must be **hashable**. (like keys in a dictionary).

