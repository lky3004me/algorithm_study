import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
nArr = list(map(int, input().split()))
nArr.sort()
m = int(input())
mArr = list(map(int, input().split()))

for i in range(m):
    find = False
    target = mArr[i]

    #이진 탐색
    start = 0
    end = len(nArr) - 1

    while start <= end:
        midi = int((start + end) // 2)
        midv = nArr[midi]
        if midv > target:
            end = midi - 1
        elif midv < target:
            start = midi + 1
        else:
            find = True
            break

    if find:
        print(1)
    else:
        print(0)
