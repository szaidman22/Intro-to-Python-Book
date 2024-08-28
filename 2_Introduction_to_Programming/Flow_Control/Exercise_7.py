# Write a function that takes a single 
# integer argument and prints a message 
# that describes whether:

# the value is between 0 and 50 (inclusive)
# the value is between 51 and 100 (inclusive)
# the value is greater than 100
# the value is less than 0

def number_range(integer):
    if integer < 0:
        print(f'{integer} is less than 0')
    elif integer < 51:
        print(f'{integer} is between 0 and 50 (inclusive)')
    elif integer < 101:
        print(f'{integer} is between 51 and 100 (inclusive)')
    else:
        print(f'{integer} is greater than 100')

