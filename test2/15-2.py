str=input("请输入字符串：")
letters = 0   # 统计字母个数
space = 0     # 统计空格个数
digit = 0     # 统计数字个数
others = 0    # 统计其他字符个数
i = 0
while i < len(str):
    oneword = str[i]  # 获取每个位置的值
    i += 1
    if oneword.isalpha():  # 判断是否是字母
        letters += 1
    elif oneword.isdigit(): # 判断是否为数字
        digit += 1
    elif oneword.isspace(): # 判断是否为空格
        space += 1
    else:
        others += 1
print("所有字母的总数为：{0}\n英文字母出现的次数：{1}\n数字出现的次数：{2}\n空格出现的次数：{3}\n其他字符出现的次数：{4}".format(letters+digit+space+others,letters,digit,space,others))