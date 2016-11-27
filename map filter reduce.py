'''
map(fun,iter):map函数主要的功能是实现多个参数的调用函数，并且可以将数据一次性的输出
              fun是要调用的函数的名字，iter是可以迭代输出的类型，如：字符串，列表，元组
              不过要满足每种类型的操作，如字符串只能相加，不能相乘

def fun(x):
    return x**x


def f(x,y):
    return x+y
L=map(fun,[1,2,3,4])
y=map(fun,[1,2,3,4])
z=map(f,[2,3,4],[7,9,0])
print(tuple(L))
print(list(z))
print(list(map(f,'abcd','cdfg')))
'''
'''reduce（fun,iter):该函数的功能是将iter中的数叠加操作，也即是假如函数中有两个参数，那么就将前面两个参数操作，然后将所得的结果与第三个
数据结合调用函数，一直叠加操作
from functools import reduce

def fun(x,y):
    return x*y

print(reduce(fun,[1,2,3,4]))    #相当于4！
'''

'''filter(fun,iter):该函数的功能是起到一个筛选的作用，根据返回的是true还是false判断是否保留元素，如果返回的是true则保留
由于返回的是一个惰性序列，必须用list将起转换成列表才能输出结果
'''

def fun(x):
    if x%2==0:
        return True
    else:
        return False
print(list(filter(fun,[2,3,4,5,6,8,9,0])))     #求其偶数

