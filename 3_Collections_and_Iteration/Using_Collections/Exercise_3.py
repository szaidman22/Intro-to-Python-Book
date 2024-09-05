# Write Python code to create a new 
# tuple from (1, 2, 3, 4, 5). 
# The new tuple should be in reverse
# order from the original. It should 
# also exclude the first and last
# members of the original. The result 
# should be the tuple (4, 3, 2).

old = (1, 2, 3, 4, 5)

new = list(old)[1:-1]
new.reverse()
new = tuple(new)
print(new)

#or use negative step index
my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[3:0:-1]
print(result)       # (4, 3, 2)
