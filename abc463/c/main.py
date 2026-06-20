import sys
from bisect import bisect_right
input = sys.stdin.readline

N = int(input())

stack = []
for _ in range(N):
    H, L = map(int, input().split())

    # Lは昇順なので、Hの小さい手前の要素は不要
    while stack and stack[-1][0] <= H:
        stack.pop()
    
    stack.append((H, L))

heights, times = zip(*stack)

Q = int(input())
T = list(map(int, input().split()))

ans=[]
for t in T:
    idx = bisect_right(times, t)
    ans.append(heights[idx])
print(*ans, sep="\n")