n=int(input())
a=list(map(int,input().split()))

map_index={}
for i in range(n):
    if a[i] in map_index:
        map_index[a[i]].append(i)
    else:
        map_index[a[i]]=[i]

ans=0
for key in map_index:
    if key % 5 != 0: continue
    if key * 7 // 5 not in map_index: continue
    if key * 3 // 5 not in map_index: continue

    i_idx=0
    k_idx=0
    i_list=map_index[key * 7 // 5]
    k_list=map_index[key * 3 // 5]
    
    for j in map_index[key]:
        while i_idx < len(i_list) and i_list[i_idx] < j:
            i_idx += 1
        while k_idx < len(k_list) and k_list[k_idx] < j:
            k_idx += 1

        cnt = (i_idx * k_idx) + (len(i_list) - i_idx) * (len(k_list) - k_idx)
        ans += cnt
print(ans)