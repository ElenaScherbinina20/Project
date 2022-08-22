import math

f = open('text.txt', 'r')
list_e = [line.strip() for line in f]

def getCountStrWithoutRepetitions(list):
    count = 0
    length = len(list)
    for element in list_e:
        count += len(element)
        n = math.factorial(count)
        k = math.factorial(count - length)
        f = n/k
    return f

print("Total number of elements in the list of lists: ", getCountStrWithoutRepetitions(list_e))

def getCountStrWithRepetitions(list2):
    count = 0
    length = len(list2)
    for element in list_e:
        count += len(element)
        n = math.factorial(count)
        k = math.factorial(length)
        f2 = n**k
    return f2

print("Total number of elements in the list of lists: ", getCountStrWithRepetitions(list_e))

