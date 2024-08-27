def multiply(number1, number2):
    number1 = float(number1)
    number2 = float(number2)
    return(number1*number2)

number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')

number1 = float(number1)
number2 = float(number2)

print(f'{number1} * {number2} = {multiply(number1,number2)}')
