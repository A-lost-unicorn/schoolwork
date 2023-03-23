def getValue(b,r,n):
    v=b*((1+r)**n)
    return v
a=int(input('请输入本金:'))
b=float(input('请输入年利率:'))/100
c=int(input('请输入年数:'))
total=getValue(a,b,c)
print(str.format("最终收益为：{0:2.2f}",total))