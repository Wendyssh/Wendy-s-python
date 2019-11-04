s1={1,2,3,4,5,6}
s2={5,6,7,8,9}

s_1 = s1.intersection(s2)
print(s_1)

s_2=s1.difference(s2)
print(s_2)

s_3=s1.issubset(s2)
print(s_3)

s1={1,2,3,4,5,6}
s2={5,6,7,8,9}
s_1=s1-s2
print(s_1)

#不支持加法s_2=s1+s2
#print(s_2)

#冰冻集合
s=frozenset()
print(type(s))
print(s)

