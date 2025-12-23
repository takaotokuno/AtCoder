t=int(input())

for _ in range(t):
    n=int(input())
    p_all=0
    w_p=[]
    w_p_all=0
    for _ in range(n):
        w,p=map(int, input().split())
        p_all+=p
        w_p.append(w+p)
        w_p_all+=w+p
    w_p.sort(reverse=True)
    ans=n
    for i in range(n):
        if p_all>=w_p_all:
            print(ans)
            break
        w_p_all-=w_p[i]
        ans-=1
    else:
        print(0)

