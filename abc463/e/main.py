import sys
input = sys.stdin.readline

N,M,Y=map(int,input().split())

graph=[[] for _ in range(N+1)]

for _ in range(M):
    u,v,T=map(int,input().split())
    u-=1
    v-=1
    graph[u].append((v,T))
    graph[v].append((u,T))

X=list(map(int,input().split()))
for i in range(N):
    graph[i].append((N,X[i]+Y))
    graph[N].append((i,X[i]))

INF=10**18
cost=[INF]*(N+1)
cost[0]=0

import heapq
pq=[(0,0)]

while pq:
    cur_cost, cur_node = heapq.heappop(pq)
    if cur_cost != cost[cur_node]:
        continue

    for e,t in graph[cur_node]:
        new_cost=cur_cost+t
        if cost[e] > new_cost:
            cost[e] = new_cost
            heapq.heappush(pq,(new_cost,e))

print(*cost[1:N])