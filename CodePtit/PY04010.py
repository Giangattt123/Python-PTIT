## LỚP THÍ SINH - 1

class ThiSinh:
    def __init__(self, name, dob, dm1 , dm2 , dm3):
        self.name = name
        self.dob = dob
        self.dm1 = dm1
        self.dm2 = dm2
        self.dm3 = dm3

    def __str__(self):
        ## Formatted String
        return f'{self.name} {self.dob} {self.dm1 + self.dm2 + self.dm3}'

name = input()
dob = input()
dm1 = float(input())
dm2 = float(input())
dm3 = float(input())

ts = ThiSinh(name , dob , dm1 , dm2 , dm3)
print(ts)