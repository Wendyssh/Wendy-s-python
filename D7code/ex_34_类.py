class A():
    name = 'liu'
    age = 18
    #以上内容在python中存储在了类实例 A 中
    #下面的A是实例,dict前后各有两个下划线
A.__dict__

#实例化
a=A()
a.__dict__

print(a.name)

class A():
	name = 'dana'
	age = 18

#注意say的写法，参数有一个self
	def say(self):
		self.name = 'aaaa'
		self.age = 200

#此案例说明
#类实例的属相和其对象的实例的属性在不对对象的实例属性赋值的前提下，
#指向同一个变量

#此时，A称为类实例
print(A.name)
print(A.age)

print("*"*20)

#id检测变量是否相同
print(id(A.name))
print(id(A.age))

print("*"*20)

a = A()

print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

#给a 重新赋值时，Id 变化（自己想的好像是类是对象的共同点一样）
print(id(A.name))
print(id(A.age))

print("*"*20)

a = A()
#查看A内所有的属性
print(a.__dict__)
print(A.__dict__)

a.name='yaona'
a.age=16

print(a.__dict__)

print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))