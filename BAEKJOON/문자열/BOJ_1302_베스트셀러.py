import sys

input = sys.stdin.readline

'''
1. 알고리즘 - 가장 많이 팔린 책을 구하기, 사전 순으로 출력을 해줘야 함
2. 시간복잡도 - 1000보다 작을 때, 공식 상 벨만 포드인데..
3. 배열? - dict 너리를 써서 카운트 해줘야 할 것 같은, 아니면 itertools
'''

n = int(input())
arr = dict()

for i in range(n):

    a = input().rstrip()

    if a in arr:
        arr[a] += 1
    else:
        arr[a] = 1

ans = sorted(arr.items())

max = 0
for i,j in ans:

    if max < j:
        max = j
        maxim = i

print(maxim)

