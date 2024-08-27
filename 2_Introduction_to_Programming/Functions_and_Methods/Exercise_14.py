# Identify all of the identifiers on 
# each line of the following code.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

print('''
      1. multiply, left, right
      2. left, right
      4. get_num, prompt
      5. prompt, float, input
      7. first_number, get_num
      8. second_number, get_num
      9. product, multiply, first_number, second_number
      10. print, first_number, second_number, product
      ''')