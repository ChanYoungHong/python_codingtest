'''

1. 시간복잡도 -> 1 < < 1000 사이니깐

'''


import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):

        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

