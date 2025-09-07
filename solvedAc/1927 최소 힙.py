import sys
import heapq

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    x = int(input())

    if x != 0:
        heapq.heappush(arr, x)
    elif x == 0 and len(arr) == 0:
        print(0)
    else:
        print(heapq.heappop(arr))

