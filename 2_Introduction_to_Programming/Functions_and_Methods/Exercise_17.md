Which of the identifiers in the following program are function names? Which are method names? Which are built-in functions?

```python
def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))
```
**Function names:**
- say
- max
- input
- print

**Method names:**
- upper
- lower

**Built-in functions:**
- print
- input
- max