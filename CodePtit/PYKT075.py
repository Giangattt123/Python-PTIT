class DB:
    def __init__(self , name:str , phoneNumber:str , time:str) -> None:
        self.name = name
        self.phoneNumber = phoneNumber
        self.time = time
        self.val = name.split()[-1]
    def __str__(self) -> str:
        return f'{self.name}: {self.phoneNumber} {self.time}'

def main() -> None:
    file = open('SOTAY.txt' , mode='r')
    ContentsFile = file.read().split('\n')
    date , index , a = None , 0 , []
    while index < len(ContentsFile):
        if ContentsFile[index][:4] == 'Ngay':
            date = ContentsFile[index][5:]
            index += 1
        else:
            a.append(DB(ContentsFile[index] , ContentsFile[index + 1] , date))
            index += 2
    a.sort(key = lambda x : (x.val , x.name))
    file.close()
    writeDT = open('DIENTHOAI.txt' , mode='w')
    for i in a: writeDT.write(i.__str__() + '\n')
    writeDT.close()
if __name__ == "__main__": main()




