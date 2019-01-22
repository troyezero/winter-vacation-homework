i =1
a =int(input("请输入盘子的个数："))
x='A';y='B';z='C'
def move(a,b,d):
    global i
    print("第%d步：将%d号盘子%s--->%s"%(i,a,b,d))
    i=i+1
def func(a,b,c,d):
    if a==1:
        move(1,b,d)
    else:
        func(a-1,b,d,c)
        move(a,b,d)
        func(a-1,c,b,d)
print("移动的次数:",2**a-1)
func(a,x,y,z)
