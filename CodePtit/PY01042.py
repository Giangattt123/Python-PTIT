## KIỂM TRA HỆ CƠ SỐ 3

def check(s):
    for i in s:
        if i != '0' and i != '1' and i != '2':
            return False
    return True

t = int(input())
for i in range(t):
    s = input()
    print('YES' if check(s) else 'NO')