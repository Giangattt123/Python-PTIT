## MÃ HÓA 1

def encode(s):
    if not s:
        return ""
    encodedStr = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encodedStr += str(count) + s[i - 1]
            count = 1
    encodedStr += str(count) + s[-1]
    return encodedStr

t = int(input())
for _ in range(t):
    S = input()
    print(encode(S))

