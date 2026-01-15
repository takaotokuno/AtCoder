import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n, q = map(int,input().split())
a = sorted(list(map(int,input().split())))
c = [x-i-1 for i, x in enumerate(a)] #欠損数の累積和

out = []

for _ in range(q):
    x, y = map(int,input().split())

    count_less_than_x = bisect_left(a, x) #x未満の要素数
    missing_before_x = x-count_less_than_x-1 #x未満で存在しない数の個数
    target = missing_before_x + y #欠損数が累積でいくつまで進むか

    # target個の欠損数までにaに存在する数の個数
    # c[i]<target となる最大のi <=> c[i]<=target-1
    idx = bisect_right(c, target-1) 
    ans = target + idx

    out.append(ans)

print(*out,sep='\n')