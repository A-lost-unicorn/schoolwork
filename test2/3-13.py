isfu=True
while isfu:
    n=int(input("请输入非负整数n:"))
    if n>0 or n==0:
        isfu=False
#for循环
sum=1
for i in range(1,n+1):
    sum=sum*i
print("for循环：{0}!={1}".format(n,sum))
#while循环
sum=1
i=1
while i<n+1:
    sum=sum*i
    i=i+1
print("while循环：{0}!={1}".format(n,sum)) 

