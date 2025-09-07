import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n,k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
print(arr[k-1])