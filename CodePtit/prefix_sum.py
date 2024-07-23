## MẢNG CỘNG DỒN
## Tiêu biểu: tính tổng từ chỉ số l -> r của 1 list
## Nếu dùng slicing => O(N)
## Nếu dùng prefix sum => O(1) nhưng space timecomplexity: O(N)
## Khi l = 0 => F[r]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    F = [0] * n
    F[0] = a[0]
    for i in range(1 , n):
        F[i] = F[i - 1] + a[i]
    l , r = 3 , 5
    print(F[r] - F[l - 1])