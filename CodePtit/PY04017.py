## TÍNH VẬN TỐC
from math import *
class DuaXe:
    def __init__(self , name:str, donVi:str, endTime:str) -> None:
        self.name = name
        self.donVi = donVi
        self.endTime = endTime
        self.quangDuong = 120
        self.ma = self.getMa()
        self.VTTB = self.getVTTB()

    def getVTTB(self):
        a = self.endTime.split(":")
        vttb = self.quangDuong / (int(a[0]) - 6 + int(a[1]) / 60)
        return round(vttb)

    def getMa(self):
        string = str(self.donVi + " " + self.name).split(" ")
        res = ""
        for value in string:
            res += value[0]
        return res.strip()

    def __str__(self):
        # return "{} {} {} {} Km/h".format(self.ma , self.name , self.donVi , self.VTTB)
        return f"{self.ma} {self.name} {self.donVi} {self.VTTB} Km/h"

n = int(input())
a = []
for i in range(n):
    name = input()
    donVi = input()
    endTime = input()
    duaXe = DuaXe(name , donVi , endTime)
    a.append(duaXe)
a1 = sorted(a , key = lambda x : -x.VTTB)
print(*a1 , sep = '\n')

class CuaRo :
    def __init__(self, ten, donVi, thoiGian) :
        a = [i[0] for i in ten.split()]
        b = [i[0] for i in donVi.split()]
        self.id = ''.join(b) + ''.join(a)
        self.ten = ten
        self.donVi = donVi
        c = thoiGian.split(':')
        self.vanToc = 120 / (int(c[0]) - 6 + int(c[1]) / 60)

    def __str__(self) :
        return f"{self.id} {self.ten} {self.donVi} {round(self.vanToc)} Km/h"

n = int(input())
cuaRo = []
for i in range(n) :
    cuaRo.append(CuaRo(input(), input(), input()))
cuaRo = sorted(cuaRo, key = lambda x : -x.vanToc)
print(*cuaRo, sep = '\n')






