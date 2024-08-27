# Without running the following code, 
# what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)

print('''
      I think the code will print:
      42
      3.141592
      2.718
      ''')