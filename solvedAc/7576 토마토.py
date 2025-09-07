import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 일단 방식은 bfs인데, 첫번째 시도 중 익은 토마토가 동시에 주변에 영향을 끼침.
# 첫 번째 시도에서, 어느 부분이 익었는지 검사
# 검사 결과, 처음부터 다 익었으면 1, 익을 수가 없는 상황이면 0 출력
# (검사하면서 이게 주변을 익게 할 수 있는지 확인할 수 있도록 검사)
# 그 이후부터, bfs 돌려서 몇 일 걸린는지 찾기 (이때 동시적으로 bfs를 돌릴 방법 찾기)
# 애초에 처음에 어디 들어있는지 검사하니, 싸그리 큐에 추가하고 visited 방문 안 한데만 하면 되지

# 첫 시도, 어느 부분이 익었는지 검사
def checkRiped():
    queue = deque()
    canRipe = False

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                queue.append((i,j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and board[nx][ny] != -1:
                    board[nx][ny] = board[x][y] +1
                    visited[nx][ny] = True
                    canRipe =True

    rst = max(map(max, board))

    if canRipe:
        return rst
    elif not canRipe and rst > 1:
        return -1
    elif not canRipe and rst == 0:
        return 0

print(checkRiped())

