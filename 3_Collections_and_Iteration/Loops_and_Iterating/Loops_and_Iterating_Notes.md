# Loops and Iterating

9/5/2024

---

Most programs need code that will run repeatedly while a given condition is truthy until it is falsy. 

**for** and **while** statements are the main looping structures in Python.
- both execute a block repeatedly while a condition remains truthy (or until it is falsy)

## while Loops

- made up of the while keyword, a conditional expression, and colon (:), followed by a block that will be executed while the conditional is truthy
- the block must do something to help Python know when to stop executing
- each time a block runs is called an **iteration**
- if you accidentally have an **infinite loop* use Control+c to terminate the program.

## for Loops

- same purpose as while loops, but have a condensed syntax that works well with **iterating over lists and other sequences**
- no need to index (as you would in a while loop)
- no need for a condition
- work for all built-in collections

If you want to iterate over a string with several words and have the string split into words rather than characters, use the **str.split()** method:

```python
for word in 'Launch School'.split():
    print(word)
```

Iterating over a dictionary will give you keys by default:

```python
# Looping over a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key)
```

If you want values, you should use either the dict.values() or dict.items() methods:

```python
# Looping over a dictionary's values
my_dict = {'a': 1, 'b': 2, 'c': 3}
for value in my_dict.values():
    print(value)

# Looping over a dictionary's key/value pairs
my_dict = {'a': 1, 'b': 2, 'c': 3}
for item in my_dict.items():
    print(item)   
```

(dict.items() will give a set with the key and the corresponding value)

You can also use **tuple unpacking** to iterate over both keys and values simultaneously:

```python
# Looping over a dictionary's key/value pairs
my_dict = {'a': 1, 'b': 2, 'c': 3}
for (key, value) in my_dict.items():
    print(f'{key} = {value}')
```

### Nested Loops

You will often need a loop within a loop, for example building a deck of cards:

```python
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10',
    'Jack', 'Queen', 'King', 'Ace',
]

deck = []
for suit in suits:
    for rank in ranks:
        card = f'{rank} of {suit}'
        deck.append(card)

print(deck)
```

It is not advisable to news 3 or more levels deep. Instead, you should use helper functions.

## Controlling Loops

Keywords **continute** and **break** provide more control over for and while loops.

- **continue** starts a new loop iteration
- **break** stops the loop

### continue

When a loop encounters **continue**, it skips running the rest of the block and jumps to the next iteration, for example:

```python
names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names:
    if name == 'Max':
        continue

    upper_name = name.upper()
    upper_names.append(upper_name)

print(upper_names);
# ['CHRIS', 'KARIS', 'VICTOR']
```
Continue can be useful for removing nested conditional logic.

Instead of this:

```python
for value in collection:
    if some_condition():
        # some code here
        if another_condition():
            # some more code here
```
we can do this:

```python
for value in collection:
    if not some_condition():
        continue

    # some code here

    if not another_condition():
        continue

    # some more code here
```

### Breaking out of a loop

Say you want to use a loop to iterate through a list to find the index of a specific value. It would make sense to stop the loop once you find the value. This is where **break** comes in:

```python
numbers = [3, 1, 5, 9, 2, 6, 4, 7]
found_item = -1
index = 0

while index < len(numbers):
    if numbers[index] == 5:
        found_item = index
        break

    index += 1

print(found_item)
```

### Emulating Do/While Loops

A normal while loop looks roughly like this:

```python
While some condition is truthy
    do some work
```

This works if you always only want to do some work while a condition isn't falsy. 

Sometimes, however, you want to do some work at least once even if the condition is initially falsy, like this:

```python
do some work
while some condition is truthy
```

To do this in python, you typically would want a break statement:

```python
while True:
    # main loop code is here

    answer = input('Play again? (y/n) ')
    if answer == 'n':
        break
```

## Simultaneous Iteration

**zip** is designed to make simultaneous iteration easy.

```python
forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
surnames = ['Camp', 'Blake', 'Flanagan', 'Short']

zipped_names = zip(forenames, surnames)
for forename, surname in zipped_names:
    print(f'{forename} {surname}')
```

## Comprehensions

**Comprehensions** are a concise and readable way to create *mutable collections* from existing iterable collections.
- **list, dict** and **set** comprehensions
- no tuple or range comprehensions

Comprehensions are **expressions**, so they can go on the right side of an assignment, or be a function argument, a return value, anything an expression can be.

### List comprehensions

This is the most commonly used comprehension. It has the following format:

```python
[ expression for element in iterable if condition ]
```
The expression in the comprehension performs a **transformation**. The expression can be any expression, like an if else statement. Or a function call.

The 'if' condition is optional. If it is present, the comprehension performs **selection**.

If you just want to filter a list (and not perform a transformation), you can do this:

```python
[ element for element in iterable if condition ]
```

We can have multiple if statements and multiple for statements if we want:

```python
cats_colors = {
    'Tess':   'brown',
    'Leo':    'orange',
    'Fluffy': 'gray',
    'Ben':    'black',
    'Kat':    'orange',
}

names = [ name.upper()
          for name in cats_colors
          if cats_colors[name] == 'orange'
          if name[0] == 'L' ]
print(names) # ['LEO']
```

```python
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10',
    'Jack', 'Queen', 'King', 'Ace',
]

deck = [ f'{rank} of {suit}'
         for suit in suits
         for rank in ranks ]
print(deck)
```

### Dictionary comprehensions

**Dictionary comprehensions** are almost identical to for loops, but include a key/value pair in the expression componenet, separated by a colon:

```python
{ key: value for element in iterable if condition }
```
Example:
```python
squares = { f'{number}-squared': number * number
            for number in range(1, 6) }
print(squares)
# pretty-printed for clarity.
{
    '1-squared': 1,
    '2-squared': 4,
    '3-squared': 9,
    '4-squared': 16,
    '5-squared': 25
}
```

### Set comprehensions

**Set comprehensions** are also basically exactly the same as list and dict comprehensions. They use curly brackets and don't have key/value pairs:

```python
{ expression for element in iterable if condition }
```