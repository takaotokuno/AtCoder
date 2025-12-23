import sys
import math
input = sys.stdin.readline

n,m=map(int,input().split())
choice = math.comb(m,2)

if n//2==1:
    print(choice)
    exit()

angle_cnt=[0]*n

for _ in range(m):
    a,b=map(int,input().split())
    angle_cnt[(a+b-2)%n] += 1

ans = choice - sum(math.comb(i,2) for i in angle_cnt)
print(ans)