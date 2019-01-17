a = []
print("请输入五个数字：")
for i in range(5):
    a.append(int(input()))
print ("排序前的列表：",a)
for i in range(4) :
    if a[i]>a[i+1] :
        c=a[i]
        a[i]=a[i+1]
        a[i+1]=c
print("从小到大排序后的列表为：",a)

