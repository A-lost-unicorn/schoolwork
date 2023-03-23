#下三角
for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j}x{i}={i*j}\t', end='')
    print()
print("--------------------------------------------")
#上三角
for i in range(1, 10):   # 行
    for j in range(1, 10-i+1,):    # 列
        print('{}x{}={}'.format(i, j, j*i), end='\t')
    print()
#矩形块
print("---------------------------------------------")
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{j}x{i}={i * j}", end="\t")
    print(" ")