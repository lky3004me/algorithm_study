from collections import deque
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [[0] *m for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0 ,-1 ,0]
for i in range(n):
    numbers = list(input())
    for j in range(m):
        arr[i][j] = int(numbers[j])

visited = [[False] * m for _ in range(n)]

def bfs(i, j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True

    while queue:
        now = queue.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if x >=0 and y >= 0 and x<n and y <m:
                if arr[x][y] != 0 and not visited[x][y]:
                    visited[x][y] = True
                    arr[x][y] = arr[now[0]][now[1]] + 1
                    queue.append((x, y))

bfs(0,0)
print(arr[n-1][m-1])