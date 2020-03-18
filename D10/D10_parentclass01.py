#Python继承
##创建子类
##要创建从其他类集成功能的类，请在创建子类时间父类作为参数发送：
##创建一个名为 Student的类，它将从 Person 类继承属性和方法：
##如果您不想向该类添加任何其他属性或方法，请使用 pass 关键字。
##现在，Student 类拥有与 Person 类相同的属性和方法。
class Student(Person):
  pass

##使用 Student 类创建一个对象，然后执行printname 方法
class Student(Person):
x = Student("Elon","Musk")
x.printname()
