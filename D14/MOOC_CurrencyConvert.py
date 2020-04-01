#CurrencyConvert.py
#money = input()
#if money[:3] =="RMB":
    #USD = 6.78 * (eval(money[3:]))
    #print("USD{:.2f}".format(USD),end="")
#elif money[:3] =="USD":
    #RMB = (eval(money[3:]))/6.78
    #print("RMB{:.2f}".format(RMB),end="")

    #CurrencyConvert.py
money = input()
if money[:3] =="RMB":
    USD = (eval(money[3:]))/6.78
    print("USD{:.2f}".format(USD))
elif money[:3] =="USD":
    RMB = (eval(money[3:]))*6.78
    print("RMB{:.2f}".format(RMB))

    #主要问题是[:3]最后一个数字是否包含在内？需要重新回看老师讲的内容
    #字符串切片：[1:3]表示取出第一个字符到不到3的字符串，[0:-1]表示从第0个字符到倒数第二个字符，即去掉最后一个字符。