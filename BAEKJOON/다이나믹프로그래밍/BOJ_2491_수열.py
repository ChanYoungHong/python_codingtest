import sys

input = sys.stdin.readline

n = int(input())

dp1 = [1] * n
dp2 = [1] * n

nums = list(map(int, input().split()))

for i in range(n - 1):
    if nums[i] <= nums[i+1]:
        dp1[i+1] = dp1[i] + 1

for j in range(n-1):

    if nums[j] >= nums[j+1]:
        dp2[j+1] = dp2[j] + 1

res = []
res.append(max(dp1))
res.append(max(dp2))

print(max(res))