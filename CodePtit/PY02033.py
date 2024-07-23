## LIỆT KÊ CÁC SỐ CÓ HAI CHỮ SỐ THEO THỨ TỰ XUẤT HIỆN

## Input: 124356141111434356149
## Output: 12 43 56 14 11
s = input()
a : list[int] = []
i , cnt = 0 , 0
num = ""
while i < len(s):
    num += s[i]
    cnt += 1
    i += 1
    if cnt == 2:
        if int(num) not in a:
            a.append(int(num))
        cnt = 0
        num = ""
for value in a:
    print(value , end = " ")

