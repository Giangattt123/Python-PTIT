## GỬI THÔNG BÁO

t = int(input())
for _ in range(t):
    s = input().split()
    ans = ""
    for i in s:
        if (len(ans+i) > 100):
            break
        ans += (i + " ")
    print(ans)

