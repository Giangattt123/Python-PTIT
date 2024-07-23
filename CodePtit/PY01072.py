## BÀI TOÁN TỔ HỢP

from itertools import combinations
## itertools.combinations(iterable, r)
n, k = map(int,input().split())
a = list(set(map(int,input().split())))
# print(a)
b = list(combinations(sorted(a),k))
# print(b)
for i in b:
    for j in i:
        print(j, end=" ")
    print()
