## CHIA DƯ CHO 42

a = []
while len(a) < 10:
    a += list(map(int, input().split()))
for i in range(len(a)):
    a[i] %= 42
s = set(a)
print(len(s))