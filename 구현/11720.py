import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = list(input().strip())
sum = 0

for i in arr:
    sum += int(i)

print(sum)