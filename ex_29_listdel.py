#del
a = [1,2,3,4,5,6]
del a[2]
print(a)

#验证删除后的列表是否和原来的列表是一样的

a = [1,2,3,4,5,6]
print(id(a))
del a[2]

print(id(a))
print(a)


#del一个变量后不能继续使用该变量
del a
print(a)