
def fun():
	global b1
	b1 = 100
	print(b1)
    print("I am in fun")
    b2 = 99
    print(b2)
#b1是在函数内部定义的，而最后是在函数外部使用，因此会出现nameerror 错误。这个问题还没解决。

fun()
print(b1)
