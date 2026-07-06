def main():
    X,Y,L,R,A,B=map(int,input().split())
    ans=Y*(B-A)+(X-Y)*(max(0,min(R,B)-max(L,A)))
    print(ans)

if __name__ == "__main__":
    main()
