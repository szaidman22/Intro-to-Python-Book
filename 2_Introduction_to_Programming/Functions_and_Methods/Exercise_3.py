# Write a program that uses a multiply function 
# to multiply two numbers and returns the result. 
# Ask the user to enter the two numbers, then output 
# the numbers and result as a simple equation.

def multiply(number1, number2):
    number1 = float(number1)
    number2 = float(number2)
    print(f'{number1} * {number2} = {number1*number2}')

number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')

multiply(number1,number2)