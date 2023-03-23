
a = int(input("您想计算前多少项的和："))
sum = 0
for i in range(1, a+1):
    sum = sum + 1/i
print(sum)