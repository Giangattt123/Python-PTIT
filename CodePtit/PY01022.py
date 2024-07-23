## TỔNG CHỮ SỐ

def sumDigit(s):
    ans = 0
    for i in s:
        ans += ord(i) - 48
    return str(ans)
def solve(s , count):
    if len(s) == 1: return count
    return solve(sumDigit(s), count + 1)

s = input()
print(solve(s , 0))