str = input("请输入一串字符：")
a = input("要查找字符：")
c = str.find(a)+1
if c!=0:
    print("该字符是字符串中的第%d个"%(c))
else:
    print("该字符不在这个字符串中")