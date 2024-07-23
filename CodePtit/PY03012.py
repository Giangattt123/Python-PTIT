## BẢNG XẾP HẠNG

from functools import cmp_to_key
def cmp(a , b):
    if a.ac > b.ac: return -1
    elif a.ac == b.ac:
        if a.submit > b.submit: return 1
        elif a.submit == b.submit:
            if a.name > b.name: return 1
            else: return -1
        else: return -1
    return 1

class SinhVien:
    def __init__(self , name , ac , submit):
        self.name = name
        self.ac = ac
        self.submit = submit

a = []
n = int(input())
for i in range(n):
    S = input()
    C , T = map(int , input().split())
    a.append(SinhVien(S , C , T))

a.sort(key = cmp_to_key(cmp))
for i in a:
    print(i.name , i.ac , i.submit)