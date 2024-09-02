# Introduction to Collections

8/29/27

---

## Collection Types

Collections are objects that contain zero or more member objects, often called **elements**.
- 3 main categories: sequences, mappings and sets

| Type | Class | Category | Kind | Mutable |
|------|-------|----------|------|---------|
| ranges | range | sequences | Non-primitive | No
| tuples | tuple | sequences | Non-primitive | No
| lists | list | sequences | Non-primitive | **yes**
| dictionaries | dict | mappings | Non-primitive | **yes**
| sets | set | sets | Non-primitive | **yes**
| frozen sets | frozenset | sets | Non-primitive | No

**Strings and other text sequences are not collections** though we often include text sequences when talking about collections. They will be included in this chapter.

| Type | Class | Category | Kind | Mutable |
|------|-------|----------|------|---------|
| strings | str | text sequences | Primitive | no

The only difference between a list and a tuple is that **lists are mutable, tuples are immutable**.

## Sequences

**Sequences** are types that maintain an **ordered** collection of objects (aka elements aka values), that can be **indexed** by whole numbers.

**Lists and Tuples** are **heterogeneous**; they can contain different kinds of objects, including other sequencs.

**Ranges** are homogenous. They only contain integers. 

**Strings** are a special form of sequence called a **text sequence**.
- homogenous (characters only)
- charactesrs are strings of length 1
- a string's characters are not separate strings until you reference a character
- strings are not actual collections because the characters inside the string aren't objects.

## Sets

**Sets** maintain an **unordered** collection of unique objects (aka elements aka **members**).
- can't be indexed

**Sets** are mutable and **frozen sets** are immutable. Both are **heterogeneous**.

# Mappings

**Mappings** are an **unordered** collection of key/value pairs. Mappings are accessed by their keys. The only mapping type discussed in this book is **dictionaries**. 

**Dict**
- mutable
- keys must be unique
- keys must be **hashable** values.
    - more details on hashable elsewhere, any built-in immutable type is hashable.
- values can be any object

Dicts maintain insertion order, but they are technically not ordered.

## Sequence Constructors

**Constructors** can be used to create sequence objects.

### String Constructor

- str()
- self explanatory

```python
str()            # returns '' (empty string)
str('abc')       # returns 'abc'
str(42)          # returns '42'
str(3.141592)    # returns '3.141592'
str(False)       # returns 'False'
str(None)        # returns 'None'
str(range(3, 7)) # returns 'range(3, 7)'
str([1, 2, 3])   # returns '[1, 2, 3]'
str(int)         # returns "<class 'int'>"
str(list)        # returns "<class 'list'>"

class Person: pass
str(Person())
# returns "<__main__.Person object at 0x1006d21e0>"
```

### Range Constructor

- range(start, stop, step)
- you can create an empty range by setting the start >= stop.
    - not a good reason to do this
    - probably a bug
- you can omit the step argument and the default step is 1.
- if you just have one argument, that will be the stop and the start will default to 0.
- use the list or tuple constructor (or set or frozen set) with the range constructor to save the values if you want to print them.
    - ranges are **lazy sequences**: they don't create any element values until your program needs them.

### List, Tuple, Set and Frozen Set Constructors

Lists, tuples, sets and frozen sets share two common constructor forms:

- list() or list(iterable)
- tuple() or tuple(iterable)
- set() or set(iterable)
- frozenset() or frozenset(iterable)

Constructors that take an **iterable** argument expect an object that python can iterate.
- includes all sequences, strings, sets and mappings.
- iterating a mapping iterates the mappings keys only.

You can use constructors to duplicate a collection. There are wonky rules when you duplicate collections with nested collections that involve shallow copies. All to remember is that nested collections are subject to shallow copies. 

