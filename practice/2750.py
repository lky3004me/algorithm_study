import sys
sys.stdin = open("input.txt", "r")

target = []
N = int(sys.stdin.readline())
for i in range(N):
    target.append(int(sys.stdin.readline()))

def bubble(arr):
    length = len(arr)
    #0부터 n-1까지
    for i in range(0, len(arr) -1):
        #i+1부터 n까지
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]



bubble(target)
for num in target:
    print(num)        


