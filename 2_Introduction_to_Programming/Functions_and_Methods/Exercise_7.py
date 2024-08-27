# Without running the following code, 
# what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo('Hello')

print('''
      I think the code will print "Hello"
      and then print a blank line.

      I was wrong. It will raise an error because
      one argument is missing.
      ''')