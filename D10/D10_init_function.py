#Python类/对象
#_init_()函数
#要理解类的含义，我们必须先了解内置的 __init__() 函数。

#所有类都有一个名为 __init__() 的函数，它始终在启动类时执行。

#使用 __init__() 函数将值赋给对象属性，或者在创建对象时需要执行的其他操作：
#创建名为 Person 的类，使用 _init_()函数为name和age 赋值
#注释：每次使用类创建新对象时，都会自动调用 __init__() 函数。
#运行错误，提示:;object()takes no parameters
class Person:
  def _init_(self,name,age):
    self.name= name
    self.age = age

p1 = Person("Bill", 63)

print(p1.name)
print(p1.age)

