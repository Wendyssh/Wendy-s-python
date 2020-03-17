#Lambda 函数
#lambda 函数是一种小的匿名函数。

#lambda 函数可接受任意数量的参数，但只能有一个表达式。
#语法：arguments:expression
#一个 lambda函数，他把作为参数的数字加10，然后返回结果

x = lambda a : a +10
print (x(5))

x= lambda a,b : a*b
print(x(5,6))

x = lambda a,b,c : a+b+c
print(x(5,6,2))

#当您把 lambda 用作另一个函数内的匿名函数时，会更好地展现 lambda 的强大能力。

#假设您有一个带一个参数的函数定义，并且该参数将乘以未知数字：

def myfunc(n):
  return lambda a : a *n

mydoubler = myfunc(2)

print(mydoubler(11))
