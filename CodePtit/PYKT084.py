## CÂU HỎI THEOI CHỦ ĐỀ 1

n = int(input())
check = True
cnt = 0
for i in range(n):
    s = input()
    if check:
        print(s , end=": ")
        cnt = 0
        check = False
    elif s != "":
        cnt += 1
    if s == "":
        check = True
        print(cnt)
print(cnt)