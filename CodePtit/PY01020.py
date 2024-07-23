## SỐ PHÁT LỘC

def check(s):
    if s[-2:] == "86": return True
    return False

t = int(input())
for _ in range(t):
    s = input()
    print('YES' if check(s) else 'NO')