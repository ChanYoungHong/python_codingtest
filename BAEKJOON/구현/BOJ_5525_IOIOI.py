import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

ans, i, cnt = 0,0,0


while i < (m-1):

    if s[i:i+3] == 'IOI':
        i += 2
        cnt += 1

        if n == cnt:
            cnt -= 1
            ans += 1
    else:
        i += 1
        cnt = 0

print(ans)