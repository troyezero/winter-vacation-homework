str = input("请输入一组数字：")
a = int(input("要查找数字："))
b = [int(i) for i in str.split()]
b.sort()
print("该组数字从小到大排序后为：",b)
c = len(b)-1 
i = 0
while i<=len(b):
    mid = (i+c)//2
    if a==b[mid]:
         print("该数在数组的第%d个"%(mid+1))    
    if a>b[mid]:
        i = i+1
    elif a<b[mid]:
        c = c-1
    else:break