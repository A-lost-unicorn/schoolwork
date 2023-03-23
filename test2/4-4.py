import random
# 生成三个不同的随机数
rand_nums = random.sample(range(101), 3)
x=a=rand_nums[0]
y=b=rand_nums[1]
z=c=rand_nums[2]
print("原始值: a={0}, b={1}, c={2}".format(a,b,c))
#方法一
m=0#空值，互换值用
if x>y:
    m=x
    x=y
    y=m
if x>z:
    m=x
    x=z
    z=m
#以上为取出最小值给x
if y>z:
    m=y
    y=z
    z=m
#以上为余下两值比较
print("(方法一)升序值: a={0}, b={1}, c={2}".format(x,y,z))
p=max(a,b,c)
q=min(a,b,c)
b=a+p+q
c=p
a=q
print("(方法二)升序值: a={0}, b={1}, c={2}".format(a,b,c))
