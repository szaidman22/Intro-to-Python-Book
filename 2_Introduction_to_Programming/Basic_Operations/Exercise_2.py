# 2. This question may be a little challenging if your math 
# skills are rusty. Don't be afraid to take advantage of the hints.
# Try your best to solve the problem, but don't feel compelled to 
# complete it if you become frustrated.

# Use the REPL and the arithmetic operators to extract the 
# individual digits of 4936:

# One place is 6.
# Tens place is 3.
# Hundreds place is 9.
# Thousands place is 4.

number = 4936

print(f"""The number is {number}
Thousands place is {number // 1000}
Hundreds place is {number % 1000 // 100}
Tens place is {number % 100 // 10}
One place is {number % 10}""")

