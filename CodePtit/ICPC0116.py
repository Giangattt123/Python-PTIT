## CON SỐ DUYÊN NỢ

# t = int(input())
# for i in range(t):
#     n = int(input())
#     nRev = int(str(n)[::-1])
#     if n % 10 == nRev % 10:
#         print('YES')
#     else:
#         print('NO')

t = int(input())
for i in range(t):
    n = input()
    print('YES' if n[0] == n[-1] else 'NO')
