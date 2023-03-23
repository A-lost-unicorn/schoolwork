a = input("请输入操作数x：")
b = input("请输入操作数y：")
c = input("请输入操作符：")
try:
    s = eval(a + c + b)  # 三个字符串相加后用eval()将其转化成算术运算
    print("{0:.1f} {1} {2:.1f} = {3:.1f}".format(eval(a), c, eval(b), s))
except ZeroDivisionError:
    print("分母 = 0，零除异常")