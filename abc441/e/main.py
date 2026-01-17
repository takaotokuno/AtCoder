N = int(input())
S = input()

# freq[acc_diff + N] 累積差の出現頻度
# 累積差acc_diff は-nからnまで変化するので2N+1要素必要
freq = [0]*(2*N+1) 

freq[N] = 1 # 初期化（累積差0に+1）
acc_idx = N # acc_diff + N 累積差0のインデックス

ans = 0
new_count = 0 # 右端を固定したときに条件を満たす部分列の個数 

for i in range(N):
    if S[i]=='A':
        new_count += freq[acc_idx]
        acc_idx += 1

    elif S[i]=='B':
        acc_idx -= 1
        new_count -= freq[acc_idx]

    freq[acc_idx] += 1
    ans += new_count

print(ans)
