list=[12.04,11.15,13.47,13.58,12.04,12.04,11.15,12.58,11.15]
print("一共有{0}个数据".format(len(list)))
print("12.04出现了{0}次".format(list.count(12.04)))
print("最小值为:{0}".format(min(list)))
list.remove(min(list))
print (list) 
