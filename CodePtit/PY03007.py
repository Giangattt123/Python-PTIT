## XỬ LÍ VĂN BẢN

a = []
while True:
    try:
        for i in input().split():
            a.append(i.lower())
    except: break
check = True
kt = ['.' , '?' , '!']
for i in a:
    if check:
        i = i.capitalize()
    if i[-1] in kt:
        check = True
        print(i[:-1])
    else:
        check = False
        print(i,end=" ")

