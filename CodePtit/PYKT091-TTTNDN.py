
file = open('VANBAN.in', 'r')
b = {}
s = 0
for x in file:
	a = x.split()
	for i in a :
		if i == i[::-1] :
			if len(i) > s :
				s = len(i)
				b.clear()
				b[i] = 1
			elif len(i) == s :
				if i not in b : b[i] = 1
				else : b[i] += 1
for i in b :
	print(i, b[i])