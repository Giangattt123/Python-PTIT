## HOÁN VỊ NGƯỢC

def sinh():
    global stop
    i = n - 1
    while i >= 0 and a[i] > a[i + 1]:
        i -= 1
    if i == 0:
        stop = 1
    else:
        k = n
        while a[i] > a[k]:
            k -= 1
        a[k], a[i] = a[i], a[k]
        c, r = n, i + 1
        while r < c:
            a[c], a[r] = a[r], a[c]
            r += 1
            c -= 1

def inHoanVi():
    global results
    result = ""
    for i in range(1, n + 1):
        result += str(a[i])
    results.append(result)

def hoan_vi():
    while not stop:
        inHoanVi()
        sinh()

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        stop = 0
        a = [0] * (n + 1)
        for i in range(1, n + 1):
            a[i] = i
        results = []
        hoan_vi()
        results.reverse()
        print(len(results))
        print(" ".join(results))
