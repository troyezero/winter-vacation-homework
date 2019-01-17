b = input("请输入5个数字：")
a = [int(i) for i in b.split()]
print("排序前的列表:",a)
a.sort()
print("排序后的列表",a)