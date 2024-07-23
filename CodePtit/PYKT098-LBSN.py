def check(s) :
	k = 0
	for i in s :
		if not i.isdigit() :
			return True
		k = k * 10 + int(i)
	if k <= (2**31 - 1) and k >= -(2**31) :
		return False
	return True

file = open('DATA.in', 'r')
a = []
for line in file:
	for i in line.split():
		if check(i) : a.append(i)
for i in sorted(a) :
	print(i, end = ' ')