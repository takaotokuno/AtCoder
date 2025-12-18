from collections import deque

INF = 10**9
DIRS = ((-1,0),(1,0),(0,-1),(0,1))

h,w = map(int,input().split())
labyrinth = [input().strip() for _ in range(h)]
warp_points = [[] for _ in range(26)]
warp_seen = [False]*26

for i in range(h):
    for j in range(w):
        if 'a' <= labyrinth[i][j] <= 'z':
            idx = ord(labyrinth[i][j]) - ord('a')
            warp_points[idx].append((i,j))

dp = [[INF]*w for _ in range(h)]
dp[0][0] = 0

dq = deque()
dq.append((0,0))

while dq:
    i,j = dq.popleft()
    for di,dj in DIRS:
        ni,nj = i+di,j+dj
        if 0 <= ni < h and 0 <= nj < w:
            if labyrinth[ni][nj] != '#':
                if dp[ni][nj] > dp[i][j] + 1:
                    dp[ni][nj] = dp[i][j] + 1
                    dq.append((ni,nj))

    if 'a' <= labyrinth[i][j] <= 'z':
        idx = ord(labyrinth[i][j]) - ord('a')
        
        if not warp_seen[idx]:
            warp_seen[idx] = True

            for ni,nj in warp_points[idx]:
                if dp[ni][nj] > dp[i][j] + 1:
                    dp[ni][nj] = dp[i][j] + 1
                    dq.append((ni,nj))

ans = dp[h-1][w-1] if dp[h-1][w-1] != INF else -1
print(ans)        