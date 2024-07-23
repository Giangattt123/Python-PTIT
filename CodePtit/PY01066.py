## XÂU "THĂNG BẰNG"

def check(s):
    sRev = s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(sRev[i]) - ord(sRev[i-1])):
            return False
    return True
t = int(input())
for _ in range(t):
    print("YES" if check(input()) else "NO")