import sys
input=sys.stdin.readline

N,M,L,S,T=map(int,input().split())

roots=[[] for _ in range(N+1)]
costs=[[] for _ in range(N+1)]

for _ in range(M):
    U,V,C=map(int,input().split())
    roots[U].append(V)
    costs[U].append(C)

flags=[False]*(N+1)
q=[(1,0,0)]
while q:
    pos, dist, cost = q.pop()

    if dist == L:
        if S <= cost <= T:
            flags[pos]=True
        continue

    for i in range(len(roots[pos])):
        nv=roots[pos][i]
        nc=costs[pos][i]
        if cost+nc > T:
            continue

        q.append((nv, dist+1, cost+nc))

indices=[i for i, v in enumerate(flags) if v]
print(*indices)
