# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
#
# str1 = list(input().strip())
# str2 = list(input().strip())
#
# dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
# result = []
#
# # DP 테이블 채우기
# for i in range(1, len(str1) + 1):
#     for j in range(1, len(str2) + 1):
#         if str1[i - 1] == str2[j - 1]:
#             dp[i][j] = dp[i - 1][j - 1] + 1
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
#
# # LCS 길이 출력
# print(dp[len(str1)][len(str2)])
#
# # LCS 문자열 추적 함수
# def getText(r, c):
#     if r == 0 or c == 0:
#         return
#     if str1[r - 1] == str2[c - 1]:
#         result.append(str1[r - 1])
#         getText(r - 1, c - 1)
#     else:
#         if dp[r - 1][c] > dp[r][c - 1]:
#             getText(r - 1, c)
#         else:
#             getText(r, c - 1)
#
# getText(len(str1), len(str2))
#
# # 문자열 역순 출력
# if result:
#     print(''.join(reversed(result)))
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

str1 = list(input().split())
str2 = list(input().split())

