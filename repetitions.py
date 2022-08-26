import math
import itertools
from itertools import *
list_e = ["a", "1", "2", "3", "4", "@"]

def getCountStrWithoutRepetitions(list_e):
    b=0
    a = []
    count = int(len(list_e))
    while b < count:
        b += 1
        c = itertools.permutations(list_e, b)
        for i in c:
            delimiter = ''
            single_str = delimiter.join(i)
            length_str = len(single_str)
            n = math.factorial(count)
            k = math.factorial(count - length_str)
            s= int(n / k)
        a.append(s)
        d = sum(a)
    return d

print("Number of options without repetition: ", getCountStrWithoutRepetitions(list_e))

def getCountStrWithRepetitions(list_e):
    b=0
    a = []
    count = int(len(list_e))
    while b < count:
        b += 1
        c = (product(list_e, repeat=b))
        for i in c:
            delimiter = ''
            single_str = delimiter.join(i)
            length_str = len(single_str)
            s = int(count**length_str)
        a.append(s)
        d = sum(a)
    return d

print("Number of options with repetitions: ", getCountStrWithRepetitions(list_e))
