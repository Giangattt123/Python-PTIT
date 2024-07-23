from datetime import datetime
class CaThi:
    def __init__(self , id , ngayThi , gioThi , phongThi) -> None:
        self.id = id
        self.ngayThi = datetime.strptime(ngayThi , "%d/%m/%Y")
        self.gioThi = datetime.strptime(gioThi , "%H:%M")
        self.phongThi = phongThi
    def __str__(self):
        return '{} {} {} {}'.format(self.id,
            datetime.strftime(self.ngayThi, '%d/%m/%Y'),
            datetime.strftime(self.gioThi, '%H:%M') , self.phongThi)
def createId(i) -> str:
    res = str(i)
    while len(res) < 3:
        res = '0' + res
    return 'C' + res
with open("CATHI.in" , "r") as f:
    listCaThi = []
    for i in range(int(f.readline())):
        id = createId(i + 1)
        listCaThi.append(CaThi(id , f.readline()[:-1], f.readline()[:-1], f.readline()))
    listCaThi.sort(key = lambda ct : (ct.ngayThi , ct.gioThi , ct.id))
    for i in listCaThi:
        print(i)