def factorial(number):
    result = number
    index = 1
    while index < number:
        result *= index
        index += 1
    return result

print(factorial(8))