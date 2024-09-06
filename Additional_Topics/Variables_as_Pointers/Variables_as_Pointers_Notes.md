# Variables as Pointers

9/6/2024

---

Python variables are **pointers** to a location in memory (an **address space**) that contains the object assigned to the variable.

The term **reference** can be used interchangeably with **pointer/point**.

## Variables as Pointers

In Python, all variables are pointers to objects. 
- if the same object is assigned to multiple variables, each of the variables references (points to) the one object
- variables act like aliases for the object (so an object can have multiple aliases)

When you reassign a variable, Python changes which object the variable points to.

When reassignment involves the creation of a new object, Python creates the new object, then changes the variable's stack item to point to the new object.

When **mutating** objects through a variable:
- if a variable points to a mutable object and you mutate that object, Python doesn't change the variable; it changes the object.
- each variable that references that object will see the object's new state

**Augmented assignment** 

When the variable on the left side of an expression references an immutable value, augmented assignment acts like reassignment (becuase the object can't be mutated, the variable is *reassigned* to a new object in memory).
- for example, a = 42, a += 1
    - a is reassigned to 43 because you can't change 42 to 43

When the variable on the left  side of an expression references a mutable value, augmented assignment will usually *mutate* the value/object referenced by the variable
- e.g. adding numbers to a list

## Variables and Objects

**Variables are named locations in a computer's memory.**
- each has a unique address in memory
- usually in an area called the **stack**, sometimes in an area called the **heap**
- the space allocated to a variable in the stack is small, usually 64 bits (8 bytes).
- objects are often larger than this, so are stored in the heap.

Once Python allocates heap space to an object, creates and stores it there, the address of the object is copied to the variable's stack location.

When you access a variable, Python determines:

1. Where the variable is in the stack
2. Gets the object's heap address from the stack item
3. Finds the object

Variable -> stack location -> object

## Equality and Identity

When you assign a new variable like this:

```python
numbers = [1, 2, 3]
numbers2 = numbers
```
numbers2 and numbers will both point to the same object in memory. They will be both equal and have the same identity. Assigning a variable to a variable does not create a new object.

```python
print(id(numbers) == id(numbers2))      # True
print(numbers is numbers2)              # True
```

This isn't the case if you initialize both variables separately. They will only be equal, but will point to separate objects with separate ids in memory.

```python
numbers = [1, 2, 3]
numbers2 = [1, 2, 3]

print(numbers)                # [1, 2, 3]
print(numbers == numbers2)    # True
print(numbers is numbers2)    # False
```

## Shallow vs.  Deep Copies

Shallow copies of nested collections will copy and make a new id in memory for only the *outermost* level of the collection. If there is a collection nested within, that object will not be duplicated and will still point to the same id in memory as the original.

Deep copies copy everything, including all levels of nested collections.

Usually shallow copies are good enough, but sometimes it is necessary to make a deep copy to ensure no strange behavior.

You can use the copy module to make shallow or deep copies.
- **copy.copy()** for shallow copies
- **copy.deepcopy()** for deep copies

