## ĐẶT TÊN

from itertools import combinations

n,k=map(int,input().split())
a=sorted(list(set(input().split())))
b=sorted(list(combinations(a,k)))
for i in b:
    print(' '.join(i))