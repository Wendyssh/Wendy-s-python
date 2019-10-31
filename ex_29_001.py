a1 = 100
def fun():
    print (a)
    print("I am in fun")
    a2=99
    print(a2)
    
 
 print(a1)
 #如下函数是a1的局部变量，不可在全局使用
 fun()
 print(a2)
