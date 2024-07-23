## SỐ KRISH

dp = [1]*10
for i in range(2, 10):
    dp[i] = dp[i-1] * i

for i in range(int(input())):
    n = input()
    s = sum(dp[int(j)] for j in n)
    print('Yes' if s == int(n) else 'No')