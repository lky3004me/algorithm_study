import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [0 for _ in range(n)]
sum = 0
for i in range(n):
    arr[i] = int(input())

arr.sort(reverse= True)
for ele in arr:
    money = k // ele
    if money > 0:
        sum +=money
        k -= money*ele

print(sum)

