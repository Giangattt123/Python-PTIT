## DANH SÁCH EMAIL

with open("CONTACT.in","r") as inp:
    a = set()
    s = inp.readline()
    while s:
        s = s.strip()
        a.add(s.lower())
        s = inp.readline()
    a = sorted(list(a))
    for i in a:
        print(i)