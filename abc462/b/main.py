N = int(input())

ans = [[] for _ in range(N)]

for i in range(1, N + 1):
    A = list(map(int, input().split()))
    for x in A[1:]:
        ans[x - 1].append(i)

for users in ans:
    print(len(users), *users)