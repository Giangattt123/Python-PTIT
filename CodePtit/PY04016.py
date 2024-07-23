## LẬP HÓA ĐƠN - 2

from datetime import datetime

class KhachHang:
    def __init__(self, id:int, name:str, numberRoom:str, startDay:str, endDay:str, vat:int) -> None:
        self.id = 'KH{:02d}'.format(id)
        self.name = name
        self.numberRoom = numberRoom
        self.startDay = datetime.strptime(startDay.strip(), "%d/%m/%Y")
        self.endDay = datetime.strptime(endDay.strip(), "%d/%m/%Y")
        self.vat = vat

    def getDay(self):
        delta = self.endDay - self.startDay
        return delta.days + 1

    def getMoney(self):
        num = int(self.numberRoom[0])
        numberDay = self.getDay()
        totalMoney = 0
        if num == 1:
            totalMoney = numberDay * 25 + self.vat
        elif num == 2:
            totalMoney = numberDay * 34 + self.vat
        elif num == 3:
            totalMoney = numberDay * 50 + self.vat
        else:
            totalMoney = numberDay * 80 + self.vat
        return totalMoney

    def __str__(self):
        return str(self.id) + ' ' + self.name.strip() + ' ' + self.numberRoom.strip() + ' ' + str(self.getDay()).strip() + ' ' + str(self.getMoney())

def main():
    n = int(input())
    a = []
    for i in range(n):
        name = input()
        numberRoom = input()
        startDay = input()
        endDay = input()
        vat = int(input())
        kh = KhachHang(i + 1, name, numberRoom, startDay, endDay, vat)
        a.append(kh)
    a.sort(key=lambda x: -x.getMoney())
    for j in a:
        print(j)

if __name__ == '__main__':
    main()

"""
Test case mẫu:
3
Huynh Van Thanh   
103 
05/06/2010   
05/06/2010   
15
Le Duc Cong  
106 
08/03/2010   
01/05/2010   
220
Tran Thi Bich Tuyen   
207 
10/04/2010   
21/04/2010   
96
Output:
KH02 Le Duc Cong 106 55 1595
KH03 Tran Thi Bich Tuyen 207 12 504
KH01 Huynh Van Thanh 103 1 40
"""

