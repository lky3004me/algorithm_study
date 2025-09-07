import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp1 = [0 for _ in range(n)]
dp2 = [0 for _ in range(n)]

dp1[0] = arr[0]
dp2[0] = 0
for i in range(1, n):
    dp1[i] = max(arr[i], dp1[i-1]+arr[i])
    dp2[i] = max(dp2[i-1] + arr[i], dp1[i-1])

print(max(max(dp1), max(dp2)))

