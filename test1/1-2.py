a=int(input('请输入本金:'))
b=float(input('请输入年利率:'))/100
c=int(input('请输入年数:'))
amount=(a*((1+b)**c))
print(str.format("本金利率和为：{0:2.2f}",amount))
