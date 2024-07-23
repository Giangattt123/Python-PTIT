## MÃ HÓA 2

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    s1 = input()
    if s1 == "0": break
    K, S = s1.split()
    ans = ""
    for i in S:
        j = s.find(i)
        ans += s[(j + int(K)) % 28]
    print(ans[::-1])



