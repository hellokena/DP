# 다이나믹 프로그래밍
# 점화식 dp[n] = dp[n-1] + dp[n-2]
# dp[1], dp[2] = 1, 2

import sys

def solution(n):
    dp = [0]*(n+1)
    if n < 3: print(n)
    else:
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        print(dp[n]%10007)

n = int(sys.stdin.readline().rstrip()) # 구하고자 하는 수
solution(n)
