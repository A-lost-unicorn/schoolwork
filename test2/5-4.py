import numpy as np
list1 = [1,2,3,4,5,6,7,8,9,10] 
#方法一
total=0
mean1 = np.mean(list1)   #平均值
max1 = np.max(list1)     #最大值
min1 = np.min(list1)     #最小值
for ele in range(0, len(list1)):
    total = total + list1[ele]

print("最大值为：{0},最小值为：{1}，平均值为：{2},列表之和为：{3},列表总数为：{4}".format(mean1, max1, min1,total,len(list1)))

#方法二
mean2 = sum(list1)/len(list1)
total=0
list1.sort()
max2 = list1[-1]
min2 = list1[0]
def sumOfList(list, size):
   if (size == 0):
     return 0
   else:
     return list[size - 1] + sumOfList(list, size - 1)   
total = sumOfList(list1, len(list1))
print("最大值为：{0},最小值为：{1}，平均值为：{2},列表之和为：{3},列表总数为：{4}".format(mean1, max1, min1,total,len(list1)))