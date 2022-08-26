import math
import itertools
from itertools import *
list_e = ["a", "1", "2", "3", "4", "@"]
def getCountStrWithoutRepetitions(list_e):
    b=0
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
            c = int(n / k)
        print("Number of options without repetition: ", c)

getCountStrWithoutRepetitions(list_e)

def getCountStrWithRepetitions(list_e):
    b=0
    count = int(len(list_e))
    while b < count:
        b += 1
        c = (product(list_e, repeat=b))
        for i in c:
            delimiter = ''
            single_str = delimiter.join(i)
            length_str = len(single_str)
            c = int(count**length_str)
        print("Number of options with repetitions: ", c)

getCountStrWithRepetitions(list_e)
