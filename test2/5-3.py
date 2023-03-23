list = [1, 1, 2, 2, 3, 3, 3, 3, 6, 6, 5, 5, 2, 2]
lst = []
for el in list:
    if lst.count(el) < 1:
        lst.append(el)
print(lst)