import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * 12

dp[1] = 1
dp[2] = 2
dp[3] = 4


for i in range(4, len(dp)):
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1])

print(dp[7])
for _ in range(n):
    print(dp[int(input())])
