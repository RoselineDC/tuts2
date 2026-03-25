# Create a Python program that identifies all numbers between 100 and 300 (inclusive) 
# that are divisible by 7 but not multiples of 5. 
# The identified numbers should be displayed in a single line, separated by commas.
# find_numbers(100, 200)
# 112,119,126,133,147,154,161,168,182,189,196

def find_numbers(a, b):
    for i in range(a, b + 1):
        if(i % 7 == 0 and i % 5 != 0):
            print(i, end=", ")

find_numbers(100, 2000)