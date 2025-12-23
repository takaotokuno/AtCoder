from itertools import accumulate

n,m=map(int,input().split())
a=sorted(list(map(int, input().split())))
b=sorted(list(map(int, input().split())))

MOD=998244353

sum_a=list(accumulate(a, initial=0))
sum_b=list(accumulate(b, initial=0))
sum_all=sum_b[-1]

point_list = [0]*n
point=0
for i in range(n):
    while point<m and b[point]<a[i]:
        point+=1
    point_list[i]=point

ans=0
for i in range(n):
    L = point_list[i]
    sumL = sum_b[L]
    ans += 2 * (a[i] * L - sumL) + sum_all - a[i]*m
    ans %= MOD
print(ans)