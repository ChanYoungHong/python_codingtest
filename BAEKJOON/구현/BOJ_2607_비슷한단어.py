import sys

input = sys.stdin.readline

n = int(input())
answer = 0

stand = list(input().rstrip())

for _ in range(n-1):

    word = input().rstrip()
    compare = stand[:]
    cnt = 0

    for i in word:

        if i in compare:
            compare.remove(i)
        else:
            cnt += 1

    if cnt < 2 and len(compare) < 2:
        answer += 1

print(answer)

