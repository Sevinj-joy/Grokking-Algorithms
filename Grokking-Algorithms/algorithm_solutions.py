#Exercise 1

#Suppose you have a sorted list of 128 names, and you’re searching
#through it using binary search. What’s the maximum number of
#steps it would take?

import math

def binary_search(n):
    if n <=0:
        return 0
    return math.ceil(math.log2(n))+1

list_size=128
steps=binary_search(list_size)
print(f'Maximum steps for binary search list of {list_size} items: {steps}')

#______________________________________________________________________________________________