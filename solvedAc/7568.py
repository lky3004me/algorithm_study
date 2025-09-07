import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
kgList = [0 for _ in range(n)]
cmList = [0 for _ in range(n)]
rstList = [0 for _ in range(n)]
for i in range(n):
    a,b = map(int, input().split())

    kgList[i] = a
    cmList[i] = b

for i in range(n):
    cnt = 0
    a, b = kgList[i], cmList[i]

    for j in range(n):
        if  kgList[j] > a and cmList[j] > b:
            cnt +=1
    rstList[i] = cnt +1

for ele in rstList:
    print(ele, end=" ")

