def remainders_3(numbers):
    return [number % 3 for number in numbers]

# Use this function to determine which of the 
# following lists contains at least one number
# that is not evenly divisible by 3 (that is, 
# the remainder is not 0):

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

def zero_check(result_of_3):
    check = [number != 0 for number in result_of_3]
    print(result_of_3, check)
    return any(check)

zero_check(remainders_3(numbers_1))
zero_check(remainders_3(numbers_2))
zero_check(remainders_3(numbers_3))
zero_check(remainders_3(numbers_4))

# CORRECTION: you can just use any, because 0 is "falsy" and 1 and 2 are "truthy"

print(any(remainders_3(numbers_1)))     # True
print(any(remainders_3(numbers_2)))     # True
print(any(remainders_3(numbers_3)))     # False
print(any(remainders_3(numbers_4)))     # False
