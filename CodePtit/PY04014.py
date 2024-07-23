## BẢNG ĐIỂM
from math import *
class HocSinh:
    def __init__(self, mhs , name , tong):
        self.mhs = mhs
        self.name = name
        self.avg = round((float(tong)/12 + 0.01) , 1)
    def rank(self):
        if self.avg >= 9:
            return 'XUAT SAC'
        elif self.avg >= 8:
            return 'GIOI'
        elif self.avg >= 7:
            return 'KHA'
        elif self.avg >= 5:
            return 'TB'
        else:
            return 'YEU'
    def __str__(self):
        return '{} {} {} {}'.format(self.mhs , self.name , self.avg , self.rank())

hsAll = []
t = int(input())
for i in range(t):
    mhs = f'HS{i + 1:02}'
    name = input()
    a = [float(i) for i in input().split()]
    tong = sum(a) + a[0] + a[1]
    hs = HocSinh(mhs , name , tong)
    hsAll.append(hs)

hsAll.sort(key = lambda x : (-x.avg , x.mhs) , reverse=False)
## Unpacking
print(*hsAll , sep = "\n")