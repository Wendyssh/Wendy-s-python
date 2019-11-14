class A():
	name="n"
	age = 18

A.__dict__
print(A.__dict__)

class student():
	name = "dana"
	age = 18

	#注意say 的写法，参数有一个self
	def say(self):
		self.name = "aaaa"
		self.age = 200
		print("My name is {0}".format(self.name))	
		print("My age is {0}".format(self.age))
    #self 并非关键字，只是一个普通参数。如下换成 s，执行结果也一样
	def sayagain(s):
		print("My name is {0}".format(s.name))
		print("My age is {0}".format(s.age))
yueyue = student()
yueyue.say()
yueyue.sayagain()

#有 self 的通过对象访问，没有的通过类访问

class teacher():
	name = "dana"
	age =19
	def say(self):
		self.name = "yaona"
		self.age = 17
		print("My name is {0}".format(self.name))
		print("My age is {0}".format(self.age))
	def sayAgain():
		print(__class__.name)
		print(__class__.age)
		print("Hello, nice to meet you again")

t = teacher()
t.say()
#默认将实例t传入第一个参数，但sayAgain()并没有对象，所以出错
#调用绑定类函数使用类名。如果直接写 t()会提示出错。因为类 sayAgain()没有对象，智能通过类访问。
teacher.sayAgain()





