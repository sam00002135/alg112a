# 方法 1
def power2n_0(n):
    return 2 ** n

# 方法 2a：用遞迴
def power2n_1(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return power2n_1(n - 1) + power2n_1(n - 1)

# 方法2b：用遞迴
def power2n_2(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return 2 * power2n_2(n - 1)

# 方法 3：用遞迴+查表
pow = [None] * 100
pow[0] = 0
pow[1] = 1

def power2n_3(n):
    if not pow[n] is None:      
        return pow[n]
    else:
        pow[n] = power2n_3(n - 1) + power2n_3(n - 2)
        return pow[n]


n = int(input("enter a number："))

result1 = power2n_0(n)
print(result1)

result2 = power2n_1(n)
print(result2)

result3 = power2n_2(n)
print(result3)

result4 = power2n_3(n)
print(result4)
