#封装
class person():
#name 是共有的成员
    name = "liuying"
    #__age就是私有成员
    __age = 18

p = person()
print(p.name)
#__age 是私有，会出错，提示没有属性‘age"
#print(p.age)

#name mangling技术,会写出age 信息
print(person.__dict__)

p._person_age = 19
print(p._person_age)
