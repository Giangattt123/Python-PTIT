## LỚP PHÂN SỐ - 2

from math import gcd

class PhanSo:
    def __init__(self, tuso=0, mauso=1):
        self.tuso = tuso
        self.mauso = mauso

    def __add__(self, other):
        z = PhanSo()
        z.mauso = self.mauso * other.mauso
        z.tuso = self.tuso * other.mauso + self.mauso * other.tuso
        z.rutgon()
        return z

    def rutgon(self):
        g = gcd(self.tuso, self.mauso)
        self.tuso //= g
        self.mauso //= g

    def __str__(self):
        return f'{self.tuso}/{self.mauso}'

a = list(map(int, input().split()))
x = PhanSo(a[0], a[1])
y = PhanSo(a[2], a[3])
z = x + y
print(z)
