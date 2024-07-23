## ĐỊA CHỈ IP

def check(s):
    if len(s) != 4: return False
    for i in s:
        try:
            if int(i) < 0 or int(i) > 255: return False
        except: return False
    return True

t = int(input())
for _ in range(t):
    s = input().split(".")
    print('YES' if check(s) else 'NO')