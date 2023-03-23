import random
# 生成三个不同的随机数
rand_nums = random.sample(range(101), 2)
a=rand_nums[0]
b=rand_nums[1]
print("整数1={0}，整数2={1}".format(a,b))
a1, b1 = a, b
res = a1 % b1
while res != 0:
    a1 = b1
    b1 = res
    res = a1 % b1
print("最大公约数为："+str(b1)+"最小公倍数为："+str(a*b/b1))