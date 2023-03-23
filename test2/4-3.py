import math
a=float(input("请输入直角三角形的直角边A(>0):"))
b=float(input("请输入直角三角形的直角边B(>0):"))
c=math.sqrt(a**2+b**2)#利用勾股定理得出c
sina=a/c
sinb=b/c
A=round(math.asin(sina)*180/math.pi,0)
B=round(math.asin(sinb)*180/math.pi,0)
print("直角三角形三边分别为：a={0}, b={1}, c={2:.1f}".format(a,b,c))
print("三角形的周长={0:.1f}，面积={1:.1f}".format(a+b+c,a*b/2))
print("三角形两个锐角的度数分别为{0},{1}".format(A,B))
