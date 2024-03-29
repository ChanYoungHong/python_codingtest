import sys

input = sys.stdin.readline

# alph = {
#     'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
#     'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19,
#     'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24,
#     'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29,
#     'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35
# }

# alph = {
#     10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E',
#     15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J',
#     20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O',
#     25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T',
#     30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'
# }

system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" #10진법이면 9 까지, 36진법이면 Z까지 표현된다
N,B = map(int, input().split())

answer = ''
while N:
    answer += str(system[N%B])
    N //= B

print(answer[::-1])