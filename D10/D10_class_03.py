#对象方法
#对象也可以包含方法。对象中的方法是属于该对象的函数。
#插入一个打印问候语的函数，并在p1对象上执行它
#self 参数是对类的当前实例的引用，用于访问属于该类的变量。
class Person:
  def _init_(self,name,age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Bill", 63)
p1.myfunc()
