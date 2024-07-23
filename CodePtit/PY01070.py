import itertools

def is_valid_circle(points, circle, k):
    count = 0
    for point in points:
        if (point[0] - circle[0])**2 + (point[1] - circle[1])**2 <= circle[2]**2:
            count += 1
    return count == k

def find_circle(points, k):
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            for l in range(j+1, n):
                circle = (points[i][0], points[i][1], ((points[j][0] - points[i][0])**2 + (points[j][1] - points[i][1])**2)**0.5)
                if is_valid_circle(points, circle, k):
                    return True
    return False

T = int(input())
for _ in range(T):
    N = int(input())
    K = int(input())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    if find_circle(points, K):
        print("YES")
    else:
        print("NO")
