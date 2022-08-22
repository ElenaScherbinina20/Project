import math

list_e = ["a", "11", "z2", "y3", "6444", "@@@"]

def getCountStrWithoutRepetitions(list):
    count = 0
    length = len(list)
    for element in list_e:
        count += len(element)
        n = math.factorial(count)/(count - length)
    return n

print("Number of options without repetition: ", getCountStrWithoutRepetitions(list_e))

def getCountStrWithRepetitions(list2):
    count = 0
    length = len(list2)
    for element in list_e:
        count += len(element)
        n = math.factorial(count)
        k = math.factorial(length)
        f2 = n**k
    return f2

print("Number of options with repetitions: ", getCountStrWithRepetitions(list_e))

