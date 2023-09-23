from datetime import datetime

def fibonacci(n):
    if n < 0:
        raise ValueError("輸入不是正整數")
    if not fib[n] is None:
        return fib[n]
    fib[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fib[n]

num = int(input('請輸入求第幾項費氏數列? '))

fib = [None] * (num + 1)
fib[0] = 0
fib[1] = 1

startTime = datetime.now()
result = fibonacci(num)
endTime = datetime.now()
seconds = endTime - startTime

print(f'fibonacci({num})={result}')
print(f'time:{seconds}')


# num = int(input('請輸入求第幾項費氏數列? '))
# a = 1
# b = 1
# print(1,a)
# for i in range(2,num+1):
#     a,b = b,a+b
#    print(i,a)
