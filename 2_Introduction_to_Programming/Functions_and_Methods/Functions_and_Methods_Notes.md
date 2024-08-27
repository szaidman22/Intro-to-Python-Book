# Functions and Methods
8/27/24

---

**Procedures**: blocks of code that run as separate units.
- these are called **functions** or **methods** in Python.
- reduce repetitive code
- easy code reuse
- improve readability and maintainability
- methods provide the same benefits as functions but are limited to specific objects

## Calling Functions

**Calling, invoking, executing** and **running** a function all mean the same thing.

- when Python encouters a function call, program flow is redirected to the code that makes up the function and executes it.
- when the code finishes, the function **returns** a value to the code that invoked it.
- the *calling code* can use this value if it wants.

To invoke/call/execute/run a function, write a function's name followed by parentheses. i.e. print().

Functions can take one or more comma-separated **arguments** between the parentheses. These arguents are *passed* to the function.

## Built-in Functions

- Functions that are always available in Python. 
- there are approximately 70 built-in functions as of Python 3.11.4.
- see [documentation here](https://docs.python.org/3/library/functions.html)
- some examples are:

#### min and max

- use to determine a collection's minimum and maximum values.
- The collection's objects must have an ordering that recognizes the < and > operators for comparing any pair of those objects.
    - i.e. you can't use with a collection that contains strings mixed with integers.
- can use with *iterables* (discussed later) - strings, sequences, mappings and sets.

#### ord and chr

- **ord** returns an integer that represents the *Unicode code point* of that character. 
- for the standard ASCII character sets, that refers to the value in the [standard ASCII character set](https://www.ascii-code.com/ASCII).
- **chr** is the inverse of ord. It takes an integer as an argument and returns the corresponding Unicode character.

#### any and all

- operate on iterable collections (lists, tuples, ranges, dictionaries and sets)

**any** returns *True* if any element in a collection is truthy, and *False* if all of the elements are falsy.

**all** returns *True* if all of the elements are truthy, and *False* if any are falsy.

```python
collection1 = [False, False, False]
collection2 = (False, True, False)
collection3 = {True, True, True}

print(any(collection1))       # False
print(any(collection2))       # True
print(any(collection3))       # True
print(any([]))                # False

print(all(collection1))       # False
print(all(collection2))       # False
print(all(collection3))       # True
print(all([]))                # True
```
**Note**: **any** returns False for an empty collection because none of the elements are truthy, while **all** returns True for an empty collection because none of the elements are falsy (so all of the elements are truthy).

These are useful for checking if elements in a collection meet a certain criteria. ([see book for example](https://launchschool.com/books/python/read/functions_methods)).

### Functions for the REPL

Provide quick access to info about your program or Python itself.

#### The Id Function

**id** returns an integer that serves as an object's **identity**.
- every object has a unique identity that does not change as long as it lives. 
- usually objects with the same value have different identities, but sometimes they have the same id because of **interning**.
    - interning applies to unique integers from -5 to 256 and some strings.
    - interning varies based on the specific implementation and version of Python you're using

```python
# Paste this code into the Python REPL
# Don't run it as a program

s = 'Hello, world!'
t = 'Hello, world!'
print(id(s) == id(t))         # False

s = 'supercalifragilisticexpialidocious'
t = 'supercalifragilisticexpialidocious'
print(id(s) == id(t))         # True

x = 5
y = 5
print(id(x) == id(y))         # True

x = 5
y = 6
print(id(x) == id(y))         # False
```
#### The dir Function

Without arguments, **dir** returns a list of all identifiers in the current local scope.

With arguments, **dir** returns a list of the object's attributes (usually the object's methods and instance variables).

- many of the names shown by dir begin and end with two underscores.
- these are **dunder** (double-underscore) or **magic methods** and **magic variables**
- we will learn more about this in Object Oriented Programming.
- see [book](https://launchschool.com/books/python/read/functions_methods) for helpful hints for using dir

#### The help Function

Without arguments, **help** prints some basic help for using help, and leaves you in *help mode* with a help> prompt. 

Or you can put an identifier as an argument for help().

## Creating Functions

Typical function **definition** or **declaration**:

```python
def func_name():
    func_body
```

A **docstring** is a documentation comment - a triple-quoted string at the beginnning of a function's block. Python can access this with the help() function and the \_\_doc__ property.

example:

```python
def say():
    """
    The say function prints "Hi!"
    """
    print('Hi!')

print('-' * 60)
print(say.__doc__)
print('-' * 60)
help(say)
```

This convention isn't followed in Launch School but it should be known.

## Scope

The scope of an identifier determines where you canuse it.

Python determines scope by looking at where you initialized the identifier.

Identifiers have **function scope**, meaning that anything initialized inside a function is only available within the body of that function and any nested functions.
- code outside the body of the function can't access the identifier.

**Variable shadowing** example:

```python
greeting = 'Salutations'

def well_howdy(who):
    greeting = 'Howdy'
    print(f'{greeting}, {who}')

well_howdy('Angie')
print(greeting)
```
i.e. the first greeting assignment shadows the greeting assignment within well_howdy() when it is printed at the end of this codeblock. And the greeting assignment in the well_howdy() function shadows the first greeting assignment when the well_howdy() function is called.

**Lexical scope**: outer scopes outside a function.

The top-most scope is the **global scope**.

See book for scope test with if-else statement.
- basically in an if else statement, if the else criteria isn't met, the else block never runs and is out of scope. This isn't how all programming languages work.

## Namespaces

Closely related to the scope concept.

Defined as a mapping of identifiers to objects.

When you refer to an identifier, Python first looks for that identifier in the **local namespace**. If it doesn't find the identifier there, it looks in any **enclosing namespaces** (outer scopes). Then it searches the **global namespace**. Last it will search the **built-in namespace**.

built-in > global > enclosing > local

## Arguments & Parameters

**Argument**: the value a function takes
- let you pass data from outside the function's scope into the function
- arguments are *passed* into functions

**Parameters** are the names between the parentheses in the function definition.
- placeholders for arguments
- don't combine the two terms.
- though of as **declarations** used to introduce these names as local variables within a function

**Function names and parameters are both considered variable names in Python.**
- **parameters** are local variables within the function.

## Return Values

All Python function calls evaluate to a value (unless there's an error)
- the default return value is *None*
this is the **implicit return value**
- when you add a **return statement**, you can return a specific value from a function. This is an **explicit return value**.
- functions that always return a Boolean value are called **predicates**.
    - i.e. testing if a some object meets some criteria like isnull

## Default Parameters

- you can provide defaults for any or all of a function's parameters
- you do this by setting them equal to a value when defining them 

## Functions vs. Methods

Method invocations have different syntax than calling a function.

To invoke a method, you prepend an object followed by a period, then write the method name followed by parentheses. This is called a **method call**.

Methods work with specific objects. All methods are functions but not all functions are methods. Every method belongs to a class and requires an object of that class to call it. 

## Mutating the Caller

**Mutating the caller** is when a method or mutates the object used to invoke it.
- For instance, the *pop* method removes elements from a list.

You should **avoid** mutating a function's arguments. This makes functions tough to debug and is considered poor practice. 