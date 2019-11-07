#函数定义
def func():
    print("thisisanexample")
    print("ilovethe wolrd")
print("函数结束了")

#调用函数，直接会输出func下面的两个print语句
func()


#参数
#person只是一个符号，调用的时候用另一个

def hello(person):
	print("{0},你好吗？".format(person))
	print("{},你看见孝敬了吗？".format(person))

p = "小明"
#调用函数，需要把P作为实参传入
hello(p)

m ="小红"
hello(m)

#返回值 return return None
#即使没写 return，仍然返回 None
pp=hello("HELEN")
print(pp)

#help
help(print)

#help(print())等同于help(None)
#print()没有返回值，而默认返回 None，因此二者等价
help(print())