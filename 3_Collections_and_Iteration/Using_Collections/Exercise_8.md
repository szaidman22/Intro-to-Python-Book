Explain why the code below prints different values on lines 3 and 4.

```python
text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29
```

Line 3 searches for 'f' in reverse through a slice of the original string, so the index it returns is based only on the substring.

Line 4 searches through the original string but only looks from index 21 through index 34. The index it returns is the rightmost occurrence of 'f' in the original string between index 21 and 34. 