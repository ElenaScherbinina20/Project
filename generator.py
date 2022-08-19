import re
list = []
nums = []
big_latin = []
small_latin = []
simbols = []
for i in range(1, 255):
    b = chr(i)
    if re.search(r"\d", b):
        nums.append(b)
    if re.search(r"[a-z]", b):
        small_latin.append(b)
    if re.search(r"[A-Z]", b):
        big_latin.append(b)
    if re.search(r"[^a-zA-Z0-9]", b):
        simbols.append(b)
    list = [nums, big_latin, small_latin, simbols]
print(list[0])
