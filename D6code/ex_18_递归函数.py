def funa(n):
    print("I'm liu dana")

def funcb(n):
    funa(100)
    print("i am wangxiaojing")

funcb(100)

#func_a 表示计算阶乘
#利用数学公式

def fun_a(n):
    print(n)
    #递归一定要有结束条件
    if n==1:
    	return 1
    #else可以省略？（老师回答说可写可不写）
    return n * fun_a(n-1)


rst = fun_a(5)
print("f(5)=",rst)

#递归必须有结束条件，否则会死掉，是死循环
def fun_b(n):
 	print(n)
 	return n * fun_b(n-1)

fun_b(100)