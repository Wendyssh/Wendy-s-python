#普通参数
#如果仅传入两个参数，则会报typeerror，位置很重要，必须一致
def normal_para(one,two,three):
	print(one+two)
	return None
normal_para(1,2,3)


#默认参数
#写法是默认参数名加=加值
def default_para(one,two,three=100):
    print(one+two+three)
    print(three)
    return None
default_para(1,2)
default_para(1,2,3)

#关键字参数
#不需要考虑位置,写法：参数=  这样写比较清晰明了
def keys_para(one,two,three):
    print(one+two)
    print(three)
    return None

keys_para(one=1,two=2,three=3)
keys_para(one=1,three=2,two=3)

