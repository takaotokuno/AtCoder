N, MAX_MONEY = map(int, input().split())
scores = [0] * N
costs = [0] * N
probs = [0] * N

for i in range(N):
    scores[i], costs[i], probs[i] = map(int, input().split())
    probs[i] /= 100 # 100分率を少数表記に補正

states = 1<< N # 解答状況
dp = [[0.0]*(MAX_MONEY + 1) for _ in range(states)] # 残金×解答状況

# 残金0→残金満額へ推移
for money in range(MAX_MONEY + 1):
    for state in range(states):
        for i in range(N):
            next_money = money - costs[i]
            next_state = state | (1 << i)

            # 金額不足または既に解いている問題はスキップ
            if next_money < 0 or state == next_state:
                continue

            prob = probs[i]
            # 成功 -> next_state, next_money, scores[i] を得る
            # 失敗 -> stateのまま, next_money
            # ※for maney for state の計算順により、金額が小さいものは全statesについて計算済み
            expected = (
                prob * (dp[next_state][next_money] + scores[i]) +
                (1 - prob) * dp[state][next_money]
            )
            dp[state][money] = max(dp[state][money], expected)

print(dp[0][MAX_MONEY])
