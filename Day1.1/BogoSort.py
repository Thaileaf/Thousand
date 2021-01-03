'''
Day 1 of coding
Bogo/Monkey sort
'''
import random

# class Bogosort:
#     Completely random version
#     @staticmethod

def bozosort(array):
    permutations = 0
    while not is_sorted(array):
        permutations += 1
        a = random.randint(0, len(array) - 1)
        b = random.randint(0, len(array) - 1)
        array[a], array[b] = array[b], array[a]
    return permutations

def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i+1]:
            return False
    else:
        return True
