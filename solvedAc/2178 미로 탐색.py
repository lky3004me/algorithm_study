from collections import deque

n, m= map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0<=ny <m:
                if not visited[nx][ny] and board[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    board[nx][ny] = board[x][y] + 1

    return board[n-1][m-1]

print(bfs(0, 0))

