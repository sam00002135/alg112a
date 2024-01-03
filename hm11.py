#有用chatgpt輔助改寫程式
import json

def editDistanceRecursive(b, a):
    def editDist(i, j):
        if i == 0:
            return j
        if j == 0:
            return i

        if b[i-1] == a[j-1]:
            return editDist(i-1, j-1)
        else:
            return min(
                editDist(i-1, j-1) + 1,  # 取代
                min(
                    editDist(i, j-1) + 1,  # 插入
                    editDist(i-1, j) + 1    # 刪除
                )
            )

    return {'d': editDist(len(b), len(a)), 'm': None}  # 不再需要儲存矩陣


def alignRecursive(b, a):
    def alignStrings(i, j):
        if i > 0 and j > 0:
            if b[i-1] == a[j-1]:
                alignStrings(i-1, j-1)
            elif m[i][j] == m[i-1][j-1] + 1 or m[i][j] == m[i-1][j-1]:
                alignStrings(i-1, j-1)
            elif m[i][j] == m[i][j-1] + 1:
                alignStrings(i, j-1)
            elif m[i][j] == m[i-1][j] + 1:
                alignStrings(i-1, j)

            # 根據遞迴結果更新字符串 bx, ax
            nonlocal bx, ax
            if b[i-1] == a[j-1]:
                bx = b[i-1] + bx
                ax = a[j-1] + ax
            elif m[i][j] == m[i-1][j-1] + 1 or m[i][j] == m[i-1][j-1]:
                bx = b[i-1] + bx
                ax = a[j-1] + ax
            elif m[i][j] == m[i][j-1] + 1:
                bx = ' ' + bx
                ax = a[j-1] + ax
            elif m[i][j] == m[i-1][j] + 1:
                bx = b[i-1] + bx
                ax = ' ' + ax

    m = [[-1] * (len(a) + 1) for _ in range(len(b) + 1)]

    def editDist(i, j):
        if m[i][j] == -1:
            if i == 0:
                m[i][j] = j
            elif j == 0:
                m[i][j] = i
            else:
                if b[i-1] == a[j-1]:
                    m[i][j] = editDist(i-1, j-1)
                else:
                    m[i][j] = min(
                        editDist(i-1, j-1) + 1,  # 取代
                        min(
                            editDist(i, j-1) + 1,  # 插入
                            editDist(i-1, j) + 1    # 刪除
                        )
                    )
        return m[i][j]

    d = editDist(len(b), len(a))
    print(f'editDistance({b},{a}) = {d}')
    print('====m======\n')
    for row in m:
        print(json.dumps(row))
    print('===========\n')

    bx, ax = '', ''
    alignStrings(len(b), len(a))
    print('bx=', bx)
    print('ax=', ax)


'''
a = "010100001"
b = "010100010"
print("dist(%s,%s) = %s", a, b, editDistance(a,b))
'''
# b = "ATG  ATCCG"
a = 'ATGCAATCCC'
b = 'ATGATCCG'
# b = "  TCCGAA"
# a   = "ATCCCAAA"
# b   = "TCCGAA"
e = editDistanceRecursive(b, a)
print(f'editDistance({b},{a}) = {e["d"]}')
print('====m======\n')
alignRecursive(b, a)
