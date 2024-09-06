Without running this code, what will it print? Why?

```python
dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])
```

'The Life of Brian'

dict2 was initialized with the dict constructor based on dict1. The dict initiator makes a shallow copy of dict1 and assigns that object to dict2. There were no nested collections in dict1, so everything has been copied to a new location in memory, and dict1 does not point to the same object as dict2. Changing the value for the Monty Python key in dict2 does not change the value for dict1, because they point to separate objects. 