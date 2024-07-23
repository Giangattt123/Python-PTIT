## TUYỂN NHÂN VIÊN

class NhanVien:
    def __init__(self, id , name , diemLT , diemTH):
        self.id = id
        self.name = name
        self.diemLT = diemLT
        self.diemTH = diemTH

    def diemTB(self):
        diemTB = (self.diemLT + self.diemTH) / 2
        return diemTB

    def status(self):
        diemTB = self.diemTB()
        if diemTB > 9.5: return 'XUAT SAC'
        elif diemTB >= 8: return 'DAT'
        elif diemTB >= 5: return 'CAN NHAC'
        else: return 'TRUOT'

    def __str__(self):
        return '{} {} {:.2f} {}'.format(self.id , self.name , self.diemTB() , self.status())

a = []
t = int(input())
for i in range(t):
    id = 'TS0{}'.format(i + 1)
    name = input()
    diemLT , diemTH = float(input()) , float(input())
    diemLT /= 10 if diemLT > 10 else 1
    diemTH /= 10 if diemTH > 10 else 1
    a.append(NhanVien(id , name , diemLT , diemTH))

a.sort(key=lambda x : -x.diemTB())
print(*a , sep = "\n")
