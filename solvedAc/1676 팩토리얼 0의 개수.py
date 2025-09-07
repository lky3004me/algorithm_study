import sys
from math import factorial

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())

rst = factorial(n)
rstList = []
while True:
    tmp = rst % 10
    rst = rst // 10
    rstList.append(tmp)

    if rst == 0:
        break
rstBool = False
cnt = 0

for i in range(len(rstList)):
    if rstList[i] == 0 and i == 0:
        rstBool = True

    if rstBool:
        if rstList[i] == 0:
            cnt +=1
        else:
            break

print(cnt)