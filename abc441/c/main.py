N,K,X = map(int,input().split())
A = list(map(int,input().split()))
B = sorted(A, reverse=True)[N-K:]

cnt=0
for i, v in enumerate(B, N-K+1):
    cnt += v
    if cnt >= X:
        print(i)
        break
else:
    print(-1)
