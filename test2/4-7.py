import math
def checktri(a, b, c):
    if (a+b > c and a+c > b and b+c > a): 
        if(a==b or b==c or a==c):
            print("该三角形为等边三角形！")
        if(a==b and b==c):
            print("该三角形为等腰三角形！")
        if(a**2==math.sqrt(b**2+c**2) or b**2==math.sqrt(a**2+c**2) or c**2==math.sqrt(b**2+a**2)):
            print("该三角形为直角三角形！")
    else:
        print("无法构成三角形！")
a=float(input("请输入三角形的边a："))
b=float(input("请输入三角形的边b："))
c=float(input("请输入三角形的边c："))
checktri(a,b,c)