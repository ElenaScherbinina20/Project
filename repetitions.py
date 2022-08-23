import math

list_e = ["a", "1", "2", "3", "4", "@"]

def getCountStrWithoutRepetitions(list):
    count = 0
    for element in list:
        count += len(element)
        length = len(element)
        n = math.factorial(count)
        k = math.factorial(count - length)
        f = n/k
    return f

print("Number of options without repetition: ", getCountStrWithoutRepetitions(list_e))

def getCountStrWithRepetitions(list2):
    count = 0
    for element in list2:
        count += len(element)
        length = len(element)
        n = math.factorial(count)
        k = math.factorial(length)
        f2 = n**k
    return f2

print("Number of options with repetitions: ", getCountStrWithRepetitions(list_e))

