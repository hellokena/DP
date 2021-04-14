# 다이나믹 프로그래밍
# 큰 문제를 작은 문제로 단순화 시켜 해결하는 알고리즘
# dp[N] = min(dp[N-1], dp[N//2] , dp[N//3]) + 1
import sys
n = int(sys.stdin.readline().rstrip())
result = [0]*(n+1) # 알기 쉽게 하기 위해서 첫 시작 인덱스를 1로 둔다
result[1] = 0
for i in range(2, n+1):
    result[i] = result[i-1]+1
    if i%2==0: result[i] = min(result[i], result[i//2]+1)
    if i%3==0: result[i] = min(result[i], result[i//3]+1)
print(result[n])
