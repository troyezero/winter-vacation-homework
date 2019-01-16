num1 = int(input("请输入一个数："))
num2 = int(input("请再输入一个数："))
a = num1
b = num2
c =a%b
while c !=0:
    a = b
    b = c
    c = a%b
print("%d和%d的最大公约数为：%d,最小公倍数为：%d"%(num1,num2,b,num1*num2/b))