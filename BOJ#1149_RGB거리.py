# 다이나믹 프로그래밍
# i-1번째 집과 색이 안 같으면 된다.
import sys

def solution(n):
    dp = []
    for _ in range(n):
        dp.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for i in range(1, n):
        dp[i][0] = dp[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = dp[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = dp[i][2] + min(dp[i-1][0], dp[i-1][1])
    print(min(dp[-1][0], dp[-1][1], dp[-1][2]))

n = int(sys.stdin.readline().rstrip()) # 구하고자 하는 수
solution(n)
