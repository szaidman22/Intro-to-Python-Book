# Use slicing to write Python code 
# to print a 6-character substring of
# 'Launch School' that begins with 
# the first c.

my_string = 'Launch School'

#slicing
print(my_string[4:10])

#another slicing
c_index = my_string.find('c')
print(my_string[c_index:(c_index+6)])
