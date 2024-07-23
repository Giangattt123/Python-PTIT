a = []

for t in range(int(input())):
    s = input() + 'a'
    tmp = ''
    for i in s:
        if i.isdigit():
            tmp += i
        else:
            if tmp != '':
                a.append(int(tmp))
                tmp = ''
print(*sorted(a), sep='\n')