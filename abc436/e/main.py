import math

n = int(input())
p = list(map(int, input().split()))

visited = [False] * n
ans = 0

for i in range(n):
    if visited[i]:
        continue

    cur = i
    size = 0

    while not visited[cur]:
        visited[cur] = True
        size += 1
        cur = p[cur] - 1

    ans += math.comb(size, 2)

print(ans)