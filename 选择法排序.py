a = input("请输入一组数：")
b = a.split()
c = list(map(int,b))
for i in range(len(c)-1):
    for i in range(len(c)-1):
       if c[i]>c[i+1]:
           d = c[i]
           c[i] = c[i+1]
           c[i+1] = d
print("从小到大排序后的该组数为：",c)