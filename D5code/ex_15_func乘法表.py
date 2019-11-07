#九九乘法表
#for和while循环的区别是，for有明确的循环次数
#version1
for o in range(1,10):#控制外循环，从1到9
    for i in range(1,o+1):#内循环，每次从第1个数字开始，打印到和行数相同的数量
        print(o*i,end="  ")
    print()


#尝试用函数打印九九乘法表
def jiujiu():
	for o in range (1,10):
		for i in range (1,o+1):
			print(o*i,end="  ")
		print()
		
    #return None


jiujiu()
jiujiu()

#函数优点：复用、任务分解
#改造函数，需要仔细琢磨
def printLine(line_num):

	'''
	line_num:代表行号
	打印一行九九乘法表
	'''
	#end后面的等号必须紧挨着end，函数赋值的时候一般等号两边推荐空格，例如 num = i*8
	for i in range (1,line_num+1):
		print(line_num*i,end=" ")

	print()

def jiujiu():
	for o in range (1,10):
		printLine(o)
    #return None
jiujiu()