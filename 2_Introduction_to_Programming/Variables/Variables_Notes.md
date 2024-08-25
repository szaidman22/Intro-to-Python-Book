# Variables
8/25/24

---

Programs must store information in memory to use and manipulate. They do this with **variables** in almost all computer languages.

**Variables** provide a way to label data with a descriptive name.
- this helps us understand a program.
- variables are *labels* that identify particular objects a program creates and uses.


## Variabes and Variable Names

- variables are attached to specific values stored in a program's memory
- variables can be changed - values can be assigned and reassigned 
- variables can be thought of to contain data, but that's not completely accurate

### Variable Naming

- very challenging task
- must accurately and concisely describe the variable's data
- aka **identifiers** (broader)

**Identifiers** refers to:
- variable and constant names
- function and method names
- Function and method parameter names
- Class and module names
- basically just another way to say "name".

## Naming Conventions

Names that follow the Python naming conventions are considered **idiomatic**. Names that don't are **non-idiomatic**. Illegal names will raise an error or do something unexpected.

**Conventions for most identifiers (excluding constant and class names)**
- use **snake_case** formatting
- names can contain lowercase letters, digits and underscores
- names should begin with a letter
- if the name has multiple words, separate with underscore
- names that begin or end with an underscore are special - don't use unless you understand
- can only use letters and digits from ASCII character set

| Idiomatic Names |
|-----------------|
| foo |
| answer_to_the_ultimate_question |
| eighty_seven |
| index_2 |
| index2 |

**Constant names (unchanging named values)**:

- use **SCREAMING_SNAKE_CASE** formatting
- can contain uppercase letters A-Z, digits and underscores
- otherwise same rules as above

**Class names**

- Use **PascalCase** formatting
    - sometimes called **CamelCase**
- can contain uppercase and lowercase letters and digits
- should begin with a capital letter
- if multiple words, capitalize each word

| Idiomatic Names |
|-----------------|
| Foo |
| UltimateQuestion |
| FourLeggedPets |
| PythonVersion2Rules |

**Note**: many non-idiomatic names are still legal. Not all.

**Illegal vs. non-idiomatic names**:
- non-idiomatic names can use extended ASCII *and* Unicode letters and digits
- punctuation and most special characters or white space are illegal
- it is illegal to start a name with a digit
- can't use Python's reserved words **if, def, while, return, pass**

| Non-Idiomatic Names | Explanation |
|---------------------|-------------|
| fourWayIntersection | camelCase |
| Schön | Extended ASCII |

| Illegal Names | Explanation |
|---------------------|-------------|
| pass | Reserved word |
| 3xy | Starts with digit |
| ultimate-question | Hyphen |
| one two three | Whitespace |
| is_lowercase? | Punctuation |
| is+lowercase | Special character |

- most illegal names will raise an error
- sometimes something that looks like an illegal name doesn't raise an error because it does something else.

For example:

```python
first,last = ['Mary', 'Wonder']
```
- assigns two variables at once

## Creating and Reassigning Variables

We **initialize** variables by giving them a value in an **assignment statement**. Initializations also provide a **definition** for the variable. 

**How Initialization and Reassignment Work**

- see book for diagram on how creating and reassigning a variable works in memory.
- basically, the computer stores the variable name and the value in separate locations in memory, then creates a connection that points from the variable name to the value.
- if reassigned, the computer stores the new value in a separate location in memory, removes the old connection and creates a new connection from the variable name to the new value.

## Creating constants

Constants are created just like variables but with screaming snake case.

You should **never** reassign a constant.

Constants are usually definited in the **global scope**. Definitions are usually written at the top of the program file, just below any imports.
- don't create a constant inside a function.

## Expressions and Assignment

You can use expressions to initialize and reassign variables - doesn't have to just be values.
- i.e. use a function
- variable must always be on the left side of the equals sign
- the right side of an assignment is always completely evaluated before assigning the result to the variable

## Augmented Assignment

When you take the current value of a variable and perform an arithmetic operation on the value then reassign the variable to the newly computed value, you can use **augmented assignment** aka **assignment operators** as shorthand:

```python
foo = 42            # foo is 42
foo -= 2            # foo is now 40
foo *= 3            # foo is now 120
foo += 5            # foo is now 125
foo //= 25          # foo is now 5
foo /= 2            # foo is now 2.5
foo **= 3           # foo is now 15.625
print(foo)          # prints 15.625
```
There's basically no performance benefit, but this is more readable and will reduce the likelihood of mispelling.

It also works with string concatenation, or any type that supports operators:

With strings:
```python
bar = 'xyz'          # bar is 'xyz'
bar += 'abc'         # bar is now 'xyzabc'
bar *= 2             # bar is now 'xyzabcxyzabc'
print(bar)           # prints xyzabcxyzabc
```
With lists:
```python
bar = [1, 2, 3]     # bar is [1, 2, 3]
bar += [4, 5]       # + with lists appends
                    # bar is now [1, 2, 3, 4, 5]
print(bar)          # prints [1, 2, 3, 4, 5]
```
With sets:
```python
bar = {1, 2, 3}     # bar is {1, 2, 3}
bar |= {2, 3, 4, 5} # | performs set union
                    # bar is now {1, 2, 3, 4, 5}
bar -= {2, 4}       # - performs set difference
                    # bar is now {1, 3, 5}
print(bar)          # prints {1, 3, 5}
```
## Reassignment vs. Mutation

Two ways to change things in Python and most other programming languages:
- **Reassignment**: change the *binding* of the variable by making it reference a new object
- **Mutation**: change the value of the object that is *bound* (assigned) to the variable.

Reassigning an element in a list doesn't reassign the variable, it mutates the collection.

Examples:
```python
num = 3               # assignment (initialization)
my_list = [1, 2, 3]   # assignment (initialization)
my_dict = {           # assignment (initialization)
    'a': 1,
    'b': 2,
}

num = 42              # Reassignment
my_list[1] = 42       # Reassignment of element,
                      # my_list is mutated!
my_dict['b'] = 3      # Reassignment of dict pair
                      # my_dict is mutated!

# You can still reassign the variables
my_list = (2, 3, 4)   # Reassignment
my_dict = { 'x': 0 }  # Reassignment
```
**Note**: sometimes augmented assignment is reassignment and sometimes it is mutation - depends on whether the variable you are using augmented assignment with is assigned to a mutable or immutable object.
- important when discussing variables as pointers


