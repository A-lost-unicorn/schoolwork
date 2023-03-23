def calnum(str):
    t=0
    for i in str:
        if i in ' ':
            t=t+1
    t=t+1
    print("单词的个数为：{t}")
str=input("请输入字符串：")
calnum(str)