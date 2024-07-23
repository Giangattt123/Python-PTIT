def is_dodac(arr):
    n = len(arr)
    count = {}

    for i in range(n):
        if arr[i] not in count:
            count[arr[i]] = 1
        else:
            count[arr[i]] += 1

        if count[arr[i]] > 1:
            return "NO"


    for i in range(n - 1):
        count = {}
        count[arr[i]] = 1
        count[arr[i + 1]] = 1
        for j in range(i + 2, n):
            if arr[j] in count:
                return "NO"
            else:
                count[arr[j]] = 1

    return "YES"


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(is_dodac(A))
