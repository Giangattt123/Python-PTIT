## TÍNH TOÁN THỜI GIAN
def time(startTime, endTime):
    startHour, startMinute = map(int, startTime)
    endHour, endMinute = map(int, endTime)
    return (endHour * 60 + endMinute) - (startHour * 60 + startMinute)

class ThoiGian:
    def __init__(self , id , name , totalTime):
        self.id = id
        self.name = name
        self.totalTime = totalTime
    def __str__(self):
        hour = self.totalTime // 60
        minute = self.totalTime % 60
        return '{} {} {} gio {} phut'.format(self.id , self.name , hour , minute)
n = int(input())
a = []
for i in range(n):
    id = input()
    name = input()
    startTime = input().split(":")
    endTime = input().split(":")
    totalTime = time(startTime , endTime)
    a.append(ThoiGian(id , name , totalTime))

a.sort(key = lambda x : -x.totalTime)
for i in a:
    print(i)

