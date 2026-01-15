import sys
input=sys.stdin.readline

t=int(input())
out=[]

for _ in range(t):
    n, w = map(int,input().split())
    c = list(map(int,input().split()))

    period = w*2
    costs = [0]*period

    for i, x in enumerate(c):
        costs[i%period] += x
    
    window = sum(costs[-w:])
    best = window

    for start in range(period):
        window += costs[start] - costs[start-w]
        best = min(best,window)

    out.append(best)

print(*out,sep='\n')
