from collections import deque

def main():
    d=deque()
    N=int(input())
    S=input().strip()
    
    is_reversed = False
    for i in range(1,N+1):
        s=S[i-1]

        if is_reversed:
            d.appendleft(i)
        else:
            d.append(i)

        if s == "o":
            is_reversed = not is_reversed

    if is_reversed:
        d=reversed(d)
    print(*d)

if __name__ == "__main__":
    main()
