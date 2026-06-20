import sys

input = sys.stdin.readline

N, K = map(int, input().split())

cloth = [tuple(map(int, input().split())) for _ in range(N)]

# 右端 R でソート
cloth.sort(key=lambda x: x[1])


def can(x):
    chosen = 0
    last = 0

    for L, R in cloth:
        if last <= L:
            chosen += 1
            last = R + x + 1

            if chosen >= K:
                return True

    return False


lo = 0
hi = 10**9

while lo < hi:
    mid = (lo + hi) // 2

    if can(mid):
        lo = mid + 1
    else:
        hi = mid

ans = lo

print(ans if ans else -1)