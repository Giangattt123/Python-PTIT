## ĐẾM SỐ TRONG XÂU
## Code chay
t = int(input())

for _ in range(t):
    s = input()
    n = input()
    count = 0
    i = 0
    while i <= len(s) - len(n):
        if s[i:i + len(n)] == n:
            count += 1
            i += len(n)
        else:
            i += 1
    print(count)
## dùng hàm có sẵn: count , find
def Count(s , n):
    return s.count(n)
print(Count("1212121112211221121" , "121"))
print("1331232".find("2"))
