# Without running the following code, 
# what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)

print('''
      I think the code will raise an error 
      because the third parameter has no argument.

      It did raise an error but I was wrong about what 
      the error would be. 

      "SyntaxError: non-default argument follows
       default argument"
      
      - Once Python sees a positional parameter with 
      a default value, all subsequent parameters must 
      have default values.
      ''')