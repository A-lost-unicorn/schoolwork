a = int(input('项数：'))
he = 0
for n in range(0,a):
    if (n % 2 == 0):
        he += 2 * n +1
    else:
        he -= 2 * n + 1
print(he)