s = "I love python and love Java and love C"
s1 = "love"
#返回第一次发现这个字符串的位置，从0开始
s.find(s1)
#如未找到，则返回-1
s2 = "her"
s.find(s2)
s.find(s1,1)

#index用法,如未找到则返回错误
s = "I love python and love Java and love C"
s1 = "love"
s.index(s1)

#
