import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(start_x, start_y, ):
    x, y = start_x, start_y
    size = 1
    visited[x][y] = True
    global graph

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and graph[nx][ny] ==1:
                size += dfs(nx, ny)
    return size

rst = 0
rstList = []
for i in range(n):
    for j in range(n):
       if graph[i][j] == 1 and not visited[i][j]:
           rstList.append(dfs(i,j))

rstList.sort()
print(len(rstList))
for ele in rstList:
    print(ele)