## THAY ĐỔI CHỮ SỐ

t = int(input())
for _ in range(t):
    p , q = input().split()
    inp = input().split()
    if len(inp) == 1:
        x1 = inp[0]
        x2 = input()
    else:
        x1 = inp[0]
        x2 = inp[1]
    sum1 = int(x1.replace(p , q)) + int(x2.replace(p , q))
    sum2 = int(x1.replace(q , p)) + int(x2.replace(q , p))
    print(min(sum1 , sum2) , max(sum1 , sum2))


