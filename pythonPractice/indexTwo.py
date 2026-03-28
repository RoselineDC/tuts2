# Q2: Generate Square Dictionary 
# Create a Python function that
#  takes an integer ( n ) as input and 
# generates a dictionary containing 
# pairs ( (i, i^2) ) for all integers ( i ) from 1 to ( n ) (inclusive). 
# The function should then return this dictionary.

# generate_square_dict(8)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

import math


def generate_square_dict(n):
    j = { }

    for i in range(n + 1):
         j[i] = i  * i
    return j


        

print(generate_square_dict(8))
