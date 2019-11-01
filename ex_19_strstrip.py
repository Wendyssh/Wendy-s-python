s= "     DDDDslkajfldkaj   "
print(s.strip())
#是否成功删除两边空格无法观察出来，使用end =“-----”
print(s.strip(), end="-----")
print()
print(s.lstrip(),end="-----")
print()
print(s.rstrip(),end="-----")

#不删除空格，删除大写字母D,仅适用于字符串两头的字符串。删除指定字符的话，但不删除空格。
C="   OOOOLKDJLAFJLdkajfkldjalf  "
print("另起一行")
print(C.strip("O"))
print()
print(C.strip("O"),end="------")