def calcu_fee(salary):
    if(0<salary and 3000>=salary):
        f=0.005*salary
        print("月工资={0}，交纳党费={1}".format(salary,f))
    elif(3000<salary and 5000>=salary):
        f=0.01*salary
        print("月工资={0}，交纳党费={1}".format(salary,f))
    elif(5000<salary and 10000>=salary):
        f=0.015*salary
        print("月工资={0}，交纳党费={1}".format(salary,f))
    else:
        f=0.02*salary
        print("月工资={0}，交纳党费={1}".format(salary,f))
salary=int(input("请输入有固定工资收入的党员收入的月工资："))
calcu_fee(salary)