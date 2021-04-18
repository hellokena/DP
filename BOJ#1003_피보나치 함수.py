# 다이나믹 프로그래밍
# 점화식 dp_0[n] = dp_0[n-1] + dp_0[n-2]
# 점화식 dp_1[n] = dp_1[n-1] + dp_1[n-2]
# dp_0 = [1, 0], dp_1 = [0, 1]

import sys
t = int(sys.stdin.readline().rstrip()) # 테스트 케이스 수
for _ in range(t):
    n = int(sys.stdin.readline().rstrip()) # 구하고자 하는 수
    dp_0 = [1, 0]
    dp_1 = [0, 1]
    for i in range(2, n+1):
        dp_0.append(dp_0[i-1]+dp_0[i-2])
        dp_1.append(dp_1[i-1]+dp_1[i-2])
    print(dp_0[n], dp_1[n])
