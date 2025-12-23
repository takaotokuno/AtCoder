import sys
input = sys.stdin.readline

n,m=map(int,input().split())

recipes=[set() for _ in range(m+1)]
food_to_recipe=[set() for _ in range(n+1)]

for i in range(1,m+1):
    vals = list(map(int, input().split()))
    recipes[i] = set(vals[1:])
    for j in range(vals[0]):
        food_to_recipe[vals[j+1]].add(i)

b=list(map(int, input().split()))
ans=[]
for i in range(n):
    idx=b[i]
    cnt = 0
    recs = food_to_recipe[idx]
    for j in recs:
        recipes[j].remove(idx)
        if len(recipes[j]) ==0:
            cnt += 1
    ans.append(cnt)

from itertools import accumulate
print(*accumulate(ans), sep='\n')


