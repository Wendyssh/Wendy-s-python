
#汉诺塔
#汉诺塔：汉诺塔（又称河内塔）问题是源于印度一个古老传说的益智玩具。大梵天创造世界的时候做了三根金刚石柱子，在一根柱子上从下往上按照大小顺序摞着64片黄金圆盘。大梵天命令婆罗门把圆盘从下面开始按大小顺序重新摆放在另一根柱子上。并且规定，在小圆盘上不能放大圆盘，在三根柱子之间一次只能移动一个圆盘。
a='A'
b='B'
c='C'

def hano(a,b,c,n):
	if n == 1:
		print("{}---> {}".format(a,c))
		return None

    if n == 2:
		print("{}---> {}".format(a,c))
		print("{}---> {}".format(a,b))
		print("{}---> {}".format(b,c))
		return None
	hano(a,c,b,n-1)
	print("{}---> {}".format(a,c))
	hano(b,a,c,n-1)

hano(a,b,c,1)