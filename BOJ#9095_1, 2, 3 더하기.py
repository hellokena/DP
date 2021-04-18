# 다이나믹 프로그래밍
# 점화식 dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
# dp[1] = 1, dp[2] = 2
import sys
t = int(sys.stdin.readline().rstrip()) # 테스트 케이스 수
for _ in range(t):
    n = int(sys.stdin.readline().rstrip()) # 구하고자 하는 수
    dp = [[0] for _ in range(n+1)]
    if n<3: # 1 or 2 => 그냥 반환
        print(n)
    else:
        dp[1], dp[2], dp[3] = 1, 2, 4
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        print(dp[n])
