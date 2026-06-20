N,X=input().split()
n=int(N)
x=ord(X)-ord("A")
for _ in range(n):
    S = input().strip()
    if S[x]=="o":
        print("Yes")
        break
else:
    print("No")