## ĐỔI CƠ SỐ - 2

from math import *

t = int(input())
for i in range(t):
	base = int(input())
	s = input()
	bitCount = int(log2(base))
	listBit = [s[i:i + bitCount] for i in range(len(s) - bitCount, -1, -bitCount)]
	bitCur = len(listBit) * len(listBit[0])
	listBit.append(s[0:(len(s) - bitCur)])
	listBit = listBit[::-1]
	for j in listBit:
		if j:
			num = int(j , 2)
			if num == 10: num = 'A'
			if num == 11: num = 'B'
			if num == 12: num = 'C'
			if num == 13: num = 'D'
			if num == 14: num = 'E'
			if num == 15: num = 'F'
			print(num , end="")
	print()




