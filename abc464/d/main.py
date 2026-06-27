import sys
input = sys.stdin.readline

def main():
    T=int(input())
    ans=[]

    for _ in range(T):
        N=int(input())
        S=[1 if s=="S" else 0 for s in input().strip()]
        X=list(map(int,input().split()))
        Y=list(map(int,input().split()))
    
        ans.append(solve(N,S,X,Y))
    
    print(*ans, sep="\n")

def solve(N,S,X,Y):
    INF=10**18
    dp=[-INF,-INF]

    for b in [0,1]:
        cost = X[0] if b != S[0] else 0
        dp[b] = -cost

    for i in range(N-1):
        ndp=[-INF,-INF]
        for b in [0,1]:
            for nb in [0,1]:
                gain=Y[i] if b==0 and nb==1 else 0
                cost=X[i+1] if nb!=S[i+1] else 0

                ndp[nb] = max(ndp[nb], dp[b]+gain-cost)
        dp=ndp
        
    return max(dp)

if __name__ == "__main__":
    main()
