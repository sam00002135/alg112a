from datetime import datetime

num = int(input('請輸入求第幾項費氏數列? '))

a, b = 0, 1

if num == 0:
    result = 0
elif num == 1:
    result = 1
else:
    for i in range(2, num + 1):
        result = a + b
        a, b = b, result

startTime = datetime.now()
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
#     print(i,a)