from heapq import heappush, heappop

n, k, x = map(int, input().split())
a = sorted(map(int, input().split()), reverse=True)

results = []

# 優先度付きキュー
# ( -sum, up, down, pos )
pq = [(-a[0]*k, 0, k, 0)]

while len(results) < x:
    neg_sum, up, down, pos = heappop(pq)
    sum = -neg_sum
    results.append(sum)

    # 9999→9998→9997→9996...
    if pos + 1 < n:
        nxt = sum - a[pos] + a[pos + 1]
        heappush(pq, (-nxt, down-1, 1, pos + 1))

    # 9999→9998→9988→9888...
    if up > 0:
        nxt = sum + a[pos] - a[pos - 1]
        heappush(pq, (-nxt, up-1, down+1, pos))

print(*results, sep='\n')