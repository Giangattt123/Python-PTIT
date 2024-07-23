## LỚP PHÂN SỐ - 1

from math import *
class PhanSo:
    def __init__(self , tuso , mauso):
        self.tuso = tuso
        self.mauso = mauso
    def rutgon(self):
        g = gcd(self.tuso , self.mauso)
        return str(int(tuso/g)) + "/" + str(int(mauso/g))
s = input().split()
tuso = int(s[0])
mauso = int(s[1])
p1 = PhanSo(tuso , mauso)
print(p1.rutgon())
