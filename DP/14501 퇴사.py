# import sys
# sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline
#
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# dp = [0] * (n+2)  # n+2로 하면 인덱스 오류 방지 가능
#
# for i in range(1, n+1):
#     time, money = arr[i-1][0], arr[i-1][1]
#
#     dp[i] = max(dp[i], dp[i-1])  # 오늘까지의 최대 수익
#
#     if i + time - 1 <= n:  # 상담이 퇴사일 이전에 끝나야 함
#         dp[i + time] = max(dp[i + time], dp[i] + money)
#
# print(max(dp))
import sys
sys.stdin= open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
tArr = [0] * (n+1)
pArr = [0] * (n+1)
dp = [0] * (n+2)
for i in range(1, n+1):
    a,b = map(int, input().split())
    tArr[i] = a
    pArr[i] = b

for i in range(1, n+1):
    date = tArr[i]

    dp[i] = max(dp[i], dp[i-1])
    if i+date-1 <= n:
        dp[i+date] = max(dp[i+date], dp[i] + pArr[i])

print(max(dp))