
dict1 = {
    'a': [[7, 1], ['aa', 'aaa']],
    'b': ([3, 2], ['bb', 'bbb']),
}

dict2 = dict(dict1)

print(dict1         is dict2) #false
print(dict1['a']    is dict2['a']) #true
print(dict1['a'][0] is dict2['a'][0]) #true
print(dict1['a'][1] is dict2['a'][1]) #true
print(dict1['b']    is dict2['b']) #true
print(dict1['b'][0] is dict2['b'][0]) #true
print(dict1['b'][1] is dict2['b'][1]) #true


