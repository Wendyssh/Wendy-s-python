#任意参数
#如果您不知道将传递给您的函数多少个参数，请在函数定义的参数名称前添加 *。
#这样，函数将接收一个参数元组，并可以相应地访问各项：
#如果参数数目未知，请在参数名称前添加 *
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Phobe","Jennifer","Rory")