Temp = input()
if Temp[0] in ['C']:
    F = 1.8 * eval(Temp[1:]) + 32
    #原来写的是 eval(Temp[1:])*1.8 +32，为何不正确？后来把加号之前的内容加上括号就正确了，为什么？
    print("F{:.2f}".format(F))
elif Temp [0] in ['F']:
    C = (eval(Temp[1:]) -32) /1.8
    print("C{:.2f}".format(C))