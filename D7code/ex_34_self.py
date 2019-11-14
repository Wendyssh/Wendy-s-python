#self 案例
class A():
	name = "Liuying"
	age = 18

	#构造函数
	def __init__(self):
		self.name = "aaaa"
		self.age = 200

	def say(self):
		print(self.name)
		print(self.age)

class B():
	name = "bbbb"
	age = 90

#只有实例对象才可以。此时，系统会默认把a作为第一个参数传入函数
a = A()
a.say()
#此时，self 被a 替换
#可以传入a
A.say(a)

#同样可以吧A 作为参数传入,但输出结果不同,不太理解
A.say(A)

#此时，传入的是类实例B，因为B具有name和age属性，所以不会报错
A.say(B)

#以上代码，利用了鸭子模型（不关心是否是鸭子，有翅膀会游泳叫起来嘎嘎就是鸭子）

