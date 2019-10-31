# 递归调用深度限制代码
x = 0

def fun():
	global x
	x += 1
    print(x)
    #函数自己调用给自己
    fun ()
#调用函数
fun()

