import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

arr.sort()

def binary(arr, target):
    start, end = 0, len(arr)-1

    while start <= end:
        mid = (start+end)//2

        if target == arr[mid]:
            return 1
        elif target > arr[mid]:
            start = mid +1
        else:
            end = mid - 1

    return 0

for ele in targets:
    print(binary(arr, ele))