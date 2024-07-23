## THU PHÍ XE Ô TÔ

def Sum(loaiXe , soGhe):
    if loaiXe == "Xe_con":
        if soGhe == 5: return 10000
        return 15000
    if loaiXe == "Xe_tai":
        return 20000
    if loaiXe == "Xe_khach":
        if soGhe == 29:
            return 50000
        return 70000

n = int(input())
dic = dict({})
for i in range(n):
    s = input().split()
    if s[3] == "IN":
        if s[4] in dic:
            dic[s[4]] += Sum(s[1], int(s[2]))
        else:
            dic[s[4]] = Sum(s[1], int(s[2]))
for i, j in dic.items():
    print(f"{i}: {j}")