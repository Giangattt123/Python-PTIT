## NGƯỠNG TỐI THIỂU

"""
Input:
124356141111434356149
2

124356141111434356149
10
"""

"""
Output:
11 2
14 2
43 3
56 2

NOT FOUND
"""

s = input()
k = int(input())
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
a = [key for key in my_dict.keys()]
a.sort()
check = False
for key in a:
    if my_dict[key] >= k:
        check = True
        print(key , my_dict[key])
if not check: print("NOT FOUND")