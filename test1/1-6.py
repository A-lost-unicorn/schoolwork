import datetime
sName=input("请输入你的姓名：")#输入姓名
birth=int(input("请输入你的出生年份："))#输入出生年份
age=datetime.date.today().year-birth#根据当前年份和出生年份计算年龄
print("你好!{0}。您{1}岁。".format(sName,age))