#b表示 let's go
#可以使用索引号，及外部使用双引号
#2、转义字符
s = "Let's go"
print(s)

#\'和没有反斜杠的意思一样
ss ="let\'s go"
print(ss)

#双斜杠等同于单斜杠，就能打印出原文中本来有的斜杠
sss = "C:\\user"
print(sss)

#回车换行,用 \r\n 表示
s1="this is a \r\n beatiful day, do \r\n you love it"
print(s1)

#格式化 %s

L="this is %s"
print(L)
print(L%"Tina")

#格式化%d
A = "I'm %d years old."
print(A)
print(A%19)

#需要注意：占位符有几个，就需要填充几个字符,把内容括起来
C = "This is %s, I am %d years old"
print(C%("dadada",20))
