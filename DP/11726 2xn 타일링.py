# import sys
# sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline
#
# n = int(input())
# dp = [0] * (n+2)
# dp[1] = 1
# dp[2] = 2
# for i in range(3, n+1):
#     dp[i] = dp[i-1] + dp[i-2]
#
# print(dp[n]%10007)
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n+1)]
# |
# ||, =
# |||,
# 2번째 인자가 0이면 |로 끝나는 갯수, 1이면 =로 끝나는 개수
dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)