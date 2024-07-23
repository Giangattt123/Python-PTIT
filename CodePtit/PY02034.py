## ĐẾM CÁC SỐ CÓ HAI CHỮ SỐ
## Input: 124356141111434356149
"""
Output:
12 1
43 3
56 2
14 2
11 2
"""

s = input()
my_dict = dict({})
i , cnt , num = 0 , 0 , ""
while i < len(s):
    num += s[i]
    cnt += 1
    i += 1
    if cnt == 2:
        if num not in my_dict:
            my_dict[num] = 1
        else:
            my_dict[num] += 1
        num = ""
        cnt = 0
for key, value in my_dict.items():
    print(key , value)