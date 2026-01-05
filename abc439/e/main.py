from bisect import bisect_left

def lis_length(arr):
    tails = [] 
    for v in arr:
        pos = bisect_left(tails, v)

        if pos < len(tails):
            tails[pos] = v
        else:
            tails.append(v)
    return len(tails)

n=int(input())
pairs = []
for _ in range(n):
    a, b = map(int, input().split()) 
    pairs.append((-a, b))
pairs.sort(reverse=True) # -a,bの降順→aの昇順、bの降順

ans = lis_length([b for _, b in pairs])

print(ans)