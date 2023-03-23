def app1(h,f):
    r=f/2-h
    c=h-r
    if r<0 and c+r!=h:
        print("{}只动物{}条腿的情况无解".format(r, h))
    else:
        print("方法一：鸡有{}只，兔有{}只".format(int(c), int(r)))
def app2(h,f):
    for x in range(1, h):
        y = h - x
        if 2 * x + 4 * y == f:
            print("方法二：鸡有" + str(x) + "只，兔有" + str(y) + "只。")
h = int(input("请输入总头数："))
f = int(input("请输入鸡和兔的脚数："))
app1(h, f)
app2(h,f)
