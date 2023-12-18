#有使用到老師的程式
import random

def hillClimbing(f, p, h=0.01):
    failCount = 0 
    while (failCount < 10000):
        fnow = f(*p)
        p1, f1 = neighbor(f, p, h)
        if f1 >= fnow:
            fnow = f1
            p = p1
            print('p=', p, 'f(p)=', fnow)
            failCount = 0
        else:
            failCount = failCount + 1
    return (p,fnow)

def neighbor(f, p, h=0.01):
    i = len(p) #取得這個向量有幾個值
    p1 = [x + random.uniform(-h, h) for x in p] #找到局部最大值和最小值
    f1 = f(*p1) #計算最新的位置
    return p1, f1


def f(x, y, z):
    return -1*(x**2+y**2+z**2)

hillClimbing(f, [2,1,3])