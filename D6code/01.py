#定义一个学生类，用来形容学生

#定义一个空的类
class Student():
	#一个空值，pass 代表直接跳过。类下面必须有东西，pass 用于占位
    pass

#定义一个对象
mingyue = Student()

#定义另外一个类，描述听 python的学生
class PythonStudent():
	#用 None 给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    #需要注意
    #1. def doHomework 的缩进层级
    #2. 系统默认存在一个 self 参数
    def doHomework(self):
        print("I am doing homework")

        #在函数末尾使用 return,也可以不写，推荐使用
        return None

#实例化一个叫yueyue的学生，是一个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
#注意成员函数的调用没有传递进入参数
yueyue.doHomework()

