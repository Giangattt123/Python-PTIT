## SỐ MAY MẮN - 2

def check(n):
    for i in str(n):
        if i != '4' and i != '7':
            return False
    return True

t = int(input())
for i in range(t):
    s = input()
    print('YES' if check(s) else 'NO')