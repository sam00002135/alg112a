#參考網路上的遞迴函式 理解後再自己寫
def permutations(s, i, n):
    if i == n:
        print("".join(s))
    else:
        for j in range(i, n):
            s[i], s[j] = s[j], s[i]
            permutations(s, i + 1, n)
            s[i], s[j] = s[j], s[i]

a = "123"
x = len(a)
s = list(a)
permutations(s, 0, x)
 