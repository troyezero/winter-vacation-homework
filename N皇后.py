max =int(input("请输入棋盘最大坐标:"))
global queen
global sum
sum =0
def show():
    for i in range(0,max):
        print(queen[i],end=" ")
    print("\n")
def place(n):
    for i in range(0,n):
        if queen[i]==queen[n] or abs(queen[i]-queen[n])==abs(n-i):
            return 0
    return 1
def NQUEENS(n):
    
    if n>=max:
        global sum 
        sum+=1
        show()
    else:
        for i in range(max):
            queen[n]=i
            if place(n):
                NQUEENS(n+1)
queen=[0 for i in range(max)]
NQUEENS(0)
print("总共有%d种解法"%sum)
print("注：0为皇后的位置")