## SỐ TĂNG GIẢM

def check(s):
    if len(s) < 3:
        return False
    l , r = 0 , len(s) - 1
    while l < r and int(s[l]) < int(s[l + 1]): l += 1
    while l < r and int(s[r]) < int(s[r - 1]): r -= 1
    return l == r

t = int(input())
for i in range(t):
    s = input()
    print('YES' if check(s) else 'NO')

