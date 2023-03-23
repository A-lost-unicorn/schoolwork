stu={"张琳":58,"孙治平":70,"徐小伟":89,"徐丽萍":69,"童万丽":90,"钱志敏":84,"赵虚余":64}
#1
print(stu)
#2
stu["晋宇浩"]="缺考"
print(stu)
#3
stu["张琳"]=60
print(stu)
#4
del stu["徐小伟"]
#5
print(stu)
#6
print("当前总人数为：{0}".format(len(stu)))
#7
name=input("请输入一个姓名：")
print('成绩为：{0}'.format(stu.get(name,"没找到该同学")))