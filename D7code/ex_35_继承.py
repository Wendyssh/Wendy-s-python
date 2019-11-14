#继承的语法
#在python 中，任何类都有一个共同的父类叫 object
#默认有共同的父类
class Person():
	name = "Noname"
	age = 0
	def sleep(self):
		print("Sleeping......")

#父类写在括号里面
class Teacher(Person):
	pass
t = Teacher()
print(t.name)
print(Teacher.name)