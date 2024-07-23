## KÍ TỰ THỨ K

t = int(input())
for _ in range(t):
    n , k = map(int , input().split())
    count = 0
    while k % 2 == 0:
        k /= 2
        count += 1
    print(chr(count + 65))