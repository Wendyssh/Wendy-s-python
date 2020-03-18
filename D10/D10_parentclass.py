#python 继承
#继承允许我们定义继承另一个类的所有方法和属性的类。

#父类是继承的类，也称为基类。

#子类是从另一个类继承的类，也称为派生类。

##创建父类
    #任何类都可以是父类，因此语法与创建人和其他类相同：
    #创建一个名为 Person 的类，其中包含 firstname 和 lastname 属性以及 printname 方法：
class Person():
    def _init_(self, fname, lname):
      self.firstname = fname
      self.lastname = lname

    def printname(self):
      print(self.firstname, self.lastname)

#使用Person来创建对象，然后执行 printname 方法：
x = Person ("Bill", "Gates")
x.printname()