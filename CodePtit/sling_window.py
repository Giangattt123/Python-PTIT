## CỬA SỐ TRƯỢT

## Dãy con liên tiếp cỡ K

## TimeComplẽity: O(n * k) => chưa tối ưu
# if __name__ == '__main__':
#     n = int(input())
#     a = list(map(int , input().split()))
#     k = int(input())
#     for i in range(0 , n - k + 1):
#         tong = 0
#         for j in range(i , i + k): tong += a[j]
#         print(tong , end = " ")

## Slingding window

if __name__ == '__main__':
    n = int(input())
    a = list(map(int , input().split()))
    k = int(input())
    tong = sum(a[:k])
    print(tong , end = " ")
    for i in range(1 , n - k + 1):
        tong = tong - a[i - 1] + a[i + k - 1] # O(1)
        print(tong , end = " ")