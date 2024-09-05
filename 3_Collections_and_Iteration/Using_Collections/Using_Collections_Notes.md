# Using Collections

9/4/2024

---

## Indexing

**Indexing** is the process of using a whole number to access (and sometimes alter) an element in a sequence.

All sequences, including strings, support indexing. 

You can use negative indexes to count backward, so the last element in a collections has index -1.

Example:

```python
seq = ('a', 'b', 'c')
print(seq[-1])  # c (last element)
print(seq[-2])  # b (next to last element)
print(seq[-3])  # a (2nd to last element)
```

## Slicing

**Slicing** allows you to extract or modify any number of conecutive elements in a sequence simultaneously. The syntax is as follows:

seq[start:stop]
- to get the elements from seq with index start to stop - 1 inclusive.

or

seq[start:stop:step]
- to specify the step amount if it's not 1, similar to range. 

Examples:

```python
seq = 'abcdefghi'
print(seq[3:7])       # defg
print(seq[-6:-2])     # defg
print(seq[2:8:2])     # ceg
print(repr(seq[3:3])) # ''
print(seq[:])         # abcdefghi
print(seq[::-1])      # ihgfedcba

seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(seq[3:7])       # [4, 5, 6, 7]
print(seq[-6:-2])     # [5, 6, 7, 8]
print(seq[2:8:2])     # [3, 5, 7]
print(seq[3:3])       # []
print(seq[:])         # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(seq[::-1])      # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

seq = [[1, 2], [3, 4]]
seq_dup = seq[:]
print(seq[0] is seq_dup[0])   # True
```

## Key-Based Access

Mappings use syntax called **key-based access**, similar to indexing but with keys rather than whole numbers. 
- a key can be any hashable object
- this includes the built-in immutable types

Use the **dict.get** method if you aren't sure if your key will return anything. This is often better than having it throw a key error:

```python
my_dict = {
    'a': 'abc',
    37: 'def',
    (5, 6, 7): 'ghi',
    frozenset([1, 2]): 'jkl',
}

print(my_dict.get('a'))                 # abc
print(my_dict.get('nothing'))           # None
print(my_dict.get('nothing', 'N/A'))    # N/A
print(my_dict.get('nothing', 100))      # 100
```

## Common Collection Operations

### Non-Mutating Operations for Collections

#### Collections Membership

- **in** operator tells you if the object to the operator's left is in the collection on the right. It returns a boolean.
- **not in** does the opposite.
- for dicts, it only looks at the keys.

#### Minimum and Maximum Members

- **min** and **max** functions return the min and max members in an iterable collection.
- Any pair of the collection's elements must be comparable with the > and <  operators.

#### Summation
- **sum** function gives the sum of iterable collections with numeric values only.

#### Locating Indices and Counting

- **index** method returns returns the index of the first element in the sequence that matches a given object. It raises a value error if a match is not found.
- **count** method returns the number of times a value occurs in the sequence.

```python
names = ['Karl', 'Grace', 'Clare', 'Victor',
         'Antonina', 'Allison', 'Trevor']
print(names.index('Clare'))   # 2
print(names.index('Trevor'))  # 6
print(names.index('Chris'))
# ValueError: 'Chris' is not in list
```

```python
numbers = [1, 3, 6, 5, 4, 10, 1, 5, 4, 4, 5, 4]
print(numbers.count(1))       # 2
print(numbers.count(3))       # 1
print(numbers.count(4))       # 4
print(numbers.count(7))       # 0
```
**index** also works with strings:

```python
names = 'Karl Grace Clare Victor Antonina Trevor'
print(names.index('Clare'))   # 11
print(names.index('Trevor'))  # 33
print(names.index('Chris'))
# ValueError: substring not found
```

#### Merging Collections

- **zip** function works with all iterables.
    - **zip** merges the members of multiple iterables into a single list of tuples.
    - each tuple in the list of tuples has the members with the same index from each merged iterable. 

Example:
```python
iterable1 = [1, 2, 3]
iterable2 = ('Kim', 'Leslie', 'Bertie')
iterable3 = [None, True, False]

zipped_iterables = zip(iterable1, iterable2, iterable3)
print(list(zipped_iterables))
# Pretty printed for clarity
# [
#   (1, 'Kim', None),
#   (2, 'Leslie', True),
#   (3, 'Bertie', False)
# ]
```
The result is a lazy sequence. You must request values explicitly, which can be done with a loop or iterable constructor.

To enforce identical lengths for the tuples, use strict = True. Zip will raise an exception if the input iterables don't all have the same length. Zip will stop at the shortest iterable in this case.

Zip returns an **iterator**. Iterators can be *consumed* once. More details in core curriculum.

#### Operations on Dictionaries

- **dict.keys** method gets a list of keys
- **dict.values** method gets a list of values
- **dict.items** method gives a list of tuples, each with a key and its value.

These aren't normal lists. They are **dictionary view objects** that are tied to the dicitonary. If you add, remove, or change objects in the dictionary, the dictionary view objects will change as well, immediately (without needing to reassign or update the variable name if you have assigned it to a variable).

### Operations for Mutable Sequences

#### Adding Elements to Mutable Sequences

**append, insert, extend**

- **append** method appends a single object to the end of a mutalbe sequence.
- **insert** method inserts an object into a mutable sequence *before* the element at a given index. If the index given is greater than or equal to the sequence's length, the object is appended. If the index is negative, it counts from the end of the sequence backwards (still inserted before the index, though).

Examples of **insert**:
```python
numbers = [1, 2]

numbers.insert(0, 8)    # Insert 8 before numbers[0]
print(numbers)          # [8, 1, 2]
numbers.insert(2, 6)    # Insert 6 before numbers[2]
print(numbers)          # [8, 1, 6, 2]
numbers.insert(100, 55) # Insert 55 before numbers[100]
print(numbers)          # [8, 1, 6, 2, 55]
numbers.insert(-3, 33)  # Insert 33 before the 3rd element
                        # from the end.
print(numbers)          # [8, 1, 33, 6, 2, 55]
```

- **extend** appends the contents of an iterable sequece to the calling iterable sequence:

```python
numbers = [1, 2]

numbers.extend([7, 8])  # Append 7 and 8 to numbers
print(numbers)          # [1, 2, 7, 8]
```

#### Removing Elements from Mutable Sequences

**remove, pop, clear**

- **remove** method searches a sequence for a specific object and removes the *first* occurrence of that object. It will raise a value error if there is no occurrence of the object.
- **pop** method removes and returns an *indexed element* from a mutable sequence. If no index is given as an argument, it removes the last element in the sequence. 
    - only works with mutable *indexed* sequences
- **clear** method removes all elements from a sequence, leaving it empty.

#### Sorting Collections

The **sorted** function will return a sorted list from any iterable collection, mutable or immutable. The original collection remains unchanged.

You can use the **list.sort** method as well, but this will mutate the list. 

- To sort **descending**, use **reverse=True**
- You can pass a **key=func** keyword argument to tell sort or sorted how to determine what values it should sort.

Example: case-insensitive sort with str.casefold:
```python
words = ['abc', 'DEF', 'xyz', '123']
print(sorted(words))
# ['123', 'DEF', 'abc', 'xyz']

print(sorted(words, key=str.casefold))
# ['123', 'abc', 'DEF', 'xyz']
```

- can also for example use key=int to convert numeric-valued strings to integers to sort as numbers.

- using sorted on a dictionary will return a sorted list of the dictionary's keys.

#### Reversing Sequences and Dictionaries

Use the **reversed** function to reverse the order of elements in a sequence or dictionary. It will return a lazy sequence. You need to iterate over the result or expand it with list or tuple.

You can reverse lists with the **list.reverse** method. This will mutate the list.

The **reversed** function should be used as a *looping aid*, to iterate over a collection's contents in reverse.

### String Operations

The str class offers many methods for using and manipulating strings, specifically.

#### Letter Case

- already know **str.upper** and **str.lower**
- **str.capitalize** method returns a copy of str with the first letter capitalized, and the rest of the letters converted to lowercase
- **str.title** returns a copy of str with every word in the string capitalized, and the remaining letters converted to lowercase.
    - sometimes this behaves weird because it uses whitespace *and* certain special characters to break words
    - ir you only want to break with whitespace, uses **capwords** function from the string module:

```python
import string
print(string.capwords("i can't believe it's already mid-july."))
# I Can't Believe It's Already Mid-july.
```
- **str.swapcase** returns a copy of str with every uppercase letter converted to lowercase and lowercase converted to uppercase.

#### Character Classification

Methods that check which characters are present in a string.

- **str.startswith** returns a boolean value if str startswith a given substring.
    - you can also use this with a tuple of strings to check each:

```python
'abc def'.startswith(('abc', 'xyz', 'stu'))  # True
'def ghu'.startswith(('abc', 'xyz', 'stu'))  # False
'xyz uvw'.startswith(('abc', 'xyz', 'stu'))  # True
'stu vwx'.startswith(('abc', 'xyz', 'stu'))  # True
```

- you can use start and end indexes to control where the search ends and begins:

```python
'abc def'.startswith('def', 4)           # True
'abc def ghi'.startswith('def', 4, 7)    # True
```

- **str.endswith** works the same way as startswith.

- **str.isalpha** returns boolean value indicating if *all* the characters of str are alphabetic.

- **str.isdigit** returns boolean value indicating if *all* the characters of str are digits.

- **str.isalnum** returns boolean indicating if str is composed of letters and/or digits.

- **str.islower** returns boolean indicating if all cased characters in str are lowercase.

- **str.isupper** same as str.islower but with uppercase.

- *str.isspace** returns boolean indicating if all characters in str are **whitespace characters**.
    - whitespace characters include spaces, tabs (\t), newlines (\n), carriage returns (\r), vertical tabs (\v) and form feeds (\f). Also includes some foreign character white spaces.
- all of these are **Unicode-aware**, if you want need to exclude non-ASCII characters, use **isascii** mehtod:

```python
text.isalpha() and text.isascii()
```

#### Stripping Characters

- **str.strip** method returns a copy of str with all leading and trailing whitespace characters removed. 
    - usually used to remove unwanted whitespace input data, such as keyboard input

Example:
```python
text = input(prompt).strip()
```

Note: use **repr** function to show the presence of whitespace characters in strings:

```python
text = ' \t  abc def    \n\r'
print(repr(text))             # ' \t  abc def    \n\r'
print(repr(text.strip()))     # 'abc def'
```

**strip** can remove other leading and trailing characters by including them as an argument. This means it won't remove leading and trailing whitespaces.
- it will remove indidvidual characters, not just substrings. 

Examples:
```python
text = ' \t  abc def    \n\r'
print(repr(text.strip('abc'))) # ' \t  abc def    \n\r'

text = 'aaabaacccabxyzabccba'
print(text.strip('a'))         # baacccabxyzabccb
print(text.strip('ab'))        # cccabxyzabcc
print(text.strip('ba'))        # cccabxyzabcc
print(text.strip('abc'))       # xyz
print(text.strip('bc'))        # aaabaacccabxyzabccba

print(repr(text.strip('abcxyz'))) # ''
```

- **str.lstrip** and **str.rstrip** are the same as **strip** but lstrip is just leading and rstrip is just trailing. 

#### Splitting and Joining Strings

- **str.split** method returns a list of the words in the string str
    - splits the string at sequences of one or more whitepsace characters (removes the whitespace)
    - you can add an argument for a different delimiter if you don't want to split by whitespaces
    - can do multi-character delimiters

To split a string into individual characters, use the list or tuple functions (not str.split):

```python
text = 'abcde'
print(list(text))             # ['a', 'b', 'c', 'd', 'e']
print(tuple(text))            # ('a', 'b', 'c', 'd', 'e')
```
- **str.splitlines** looks for line-ending characters line \n (line feed) and \r (carriage return) and \n\r (new lines)
    - it returns a list of lines of text from str

- **str.join** method concatenates all strings in an iterable collection into a single string. The collection is the argument and the object the method is called on (str) is the delimiter with which to join the strings in the iterable:

```python
words = ['You', 'were', 'lucky']
print(''.join(words))         # Youwerelucky
print(' '.join(words))        # You were lucky
print(','.join(words))        # You,were,lucky
print('\n  '.join(words))
# You
#   were
#   lucky
```

#### Finding Substrings

- **str.find** searches through str looking for the first occurrence of the argument and returns the index of the first matching substring.
- **str.rfind** is the same as str.find but it searches from right to left (reverse).
    -  if there is no match, they will return -1.
    - both case-sensitive
    - you can add start and stop arguments to search a slice

### Nested Collections

There are some limitations on what you can nest in certain collections.

- usually can't nest mutable collections inside some collections
    - e.g. you can't nest a mutable collection like a list, dictionary, or other set inside a set
- you **can** nest mutable collections inside tuples even though tuples are immutable.

To index items from several layers of nesting, run several [] operations together:

```python
nested_seq = [
    [1, 2, [3, 4, (5, 6, 7, 8)]],
    [9, [10, (11,)]],
    [12, 13, [14, 15, (16, 17)]],
    [18, [19, 20, (21, 22)]],
]

print(nested_seq[1])          # [9, [10, (11,)]]
print(nested_seq[3][0])       # 18
print(nested_seq[0][2][2])    # (5, 6, 7, 8)
print(nested_seq[2][2][2][1]) # 17
```

## Comparing Collections

- Equality is the most straightforward:
- the collections are equal if:
    - they have the same type
    - same # of elements
    - for sequences, each pair of corresponding elements is equal
    - for sets, have the same members
    - for mappings, each key/value pair must be present and identical
- != also works the same
- won't go into < and >

