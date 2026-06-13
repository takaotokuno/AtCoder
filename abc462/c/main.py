import sys
from itertools import groupby

input = sys.stdin.readline

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

points.sort()  # X昇順、同じXならY昇順

INF = 10**18
min_y_before = INF
ans = 0

for x, group in groupby(points, key=lambda p: p[0]):
    ys = [y for _, y in group]

    for y in ys:
        if y <= min_y_before:
            ans += 1

    min_y_before = min(min_y_before, min(ys))

print(ans)