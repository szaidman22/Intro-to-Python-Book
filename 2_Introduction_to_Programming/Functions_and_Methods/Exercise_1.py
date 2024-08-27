# What happens when you run the following program? Why do we get that result?

# def set_foo():
#     foo = 'bar'

# set_foo()
# print(foo)

print('''
      You will get an error when running this program.
      foo is not defined in the global scope, only within the function,
      and it is not returned. So to Python, foo does not exist so it
      can't be printed.
      ''')