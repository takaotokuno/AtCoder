import sys
import math
from itertools import accumulate

input = sys.stdin.readline

# 時刻の最大値に合わせて十分な長さを確保
M = 10**6 + 2
diff = [0] * M

N, D = map(int, input().split())

for _ in range(N):
    S, T = map(int, input().split())

    # D時間以上滞在する 
    if T - S >= D:
        # 反抗開始時刻としてあり得る最初の時刻、最後の時刻を記録
        diff[S] += 1
        diff[T - D + 1] -= 1

ans = 0
# 各時刻について、同席可能な人数から2人組を選ぶ
for cnt in accumulate(diff):
    ans += math.comb(cnt, 2)

print(ans)