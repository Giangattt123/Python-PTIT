## LIỆT KÊ CÁC SỐ CÓ HAI CHỮ SỐ TĂNG DẦN
## Input: 124356141111434356149
## Output: 11 12 14 43 56
se = set()
s = input()
i , cnt = 0 , 0
num = ""
while i < len(s):
    num += s[i]
    cnt += 1
    i += 1
    if cnt == 2:
        se.add(int(num))
        num = ""
        cnt = 0
a = list(se)
a.sort()
for value in a:
    print(value , end = " ")
