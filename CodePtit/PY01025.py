## CHÈN DẤU PHẨY

s = input()
s = s[::-1]
num = 0
ans = ""

for i in s:
    if num == 3:
        ans += ','
        num = 0
    ans += i
    num += 1
ans = ans[::-1]
print(ans)