#方法一
count=0
for year in range(2000,3001):
    if (year%4==0 and year%100!=0) or (year%400==0):
        print(year,end=" ")
        # 每五个一排
        count += 1
        if count % 5 == 0:
            print()
#方法二
print()
print("------------------------下面是方法二------------------------------")
count=0
import calendar
for year in range(2000,3001):
    check_year=calendar.isleap(year)
    if check_year:
        print(year,end=" ")
        # 每五个一排
        count += 1
        if count % 5 == 0:
            print()