import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n,m = map(int, input().split())
graph = []
for i in range(n):
    s= input().strip()
    nums = [int(ch) for ch in s]
    graph.append(nums)

maxNum = min(n,m)

def find(n,m,num):
    dx = [1, 0, 1]
    dy = [0, 1, 1]
    for i in range(n):
        for j in range(m):
            x, y = j, i
            cnt = 0

            for k in range(3):
                nx = x + (num - 1)*dx[k]
                ny = y + (num - 1)*dy[k]

                if 0<= nx <m and 0<=ny < n:
                    if graph[y][x] == graph[ny][nx]:
                        cnt +=1
            if cnt == 3:
                return True
    return False



for i in range(maxNum, 0, -1):
    if find(n,m,i):
        print(i**2)
        break
