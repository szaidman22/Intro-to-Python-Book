The following code causes an infinite loop (a loop that never stops iterating). Why?

```python
counter = 0

while counter < 5:
    print(counter)
```

The variable "counter" is never changed within the loop to be greater than or equal to 5. "counter" is assigned the value 0, then the loop runs infitintely because the condtion counter < 5 is always truthy.