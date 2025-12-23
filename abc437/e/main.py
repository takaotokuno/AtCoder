n=int(input())
G=[{} for _ in range(n+1)]
vs=[[] for _ in range(n+1)]
pos=[-1]*(n+1)
pos[0]=0
tmp=1
for i in range(1,n+1):
    p,y=map(int,input().split())
    if y not in G[pos[p]]:
        G[pos[p]][y]=tmp
        tmp+=1
    pos[i]=G[pos[p]][y]
    vs[pos[i]].append(i)

ans=[]
def dfs(i):
    global ans
    ans+=vs[i]
    for j in sorted(list(G[i].keys())):
        dfs(G[i][j])

dfs(0)
print(*ans)

