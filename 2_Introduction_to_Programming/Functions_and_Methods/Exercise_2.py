# foo = 'bar'

# def set_foo():
#     foo = 'qux'

# set_foo()
# print(foo)

# What does this program print? Why?

print('''
    This program prints 'bar'.
    foo was only assigned the value 'qux' in the function's scope.
    foo was never reassigned outside of the function's scope.
    ''')