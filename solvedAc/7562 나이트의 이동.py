from collections import deque
import sys

input = sys.stdin.readline

dxy = [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]

t = int(input())
for _ in range(t):
    L = int(input())  # 체스판 한 변
    sx, sy = map(int, input().split())
    tx, ty = map(int, input().split())

    if (sx, sy) == (tx, ty):
        print(0)
        continue

    dist = [[-1]*L for _ in range(L)]
    q = deque()
    q.append((sx, sy))
    dist[sx][sy] = 0  # 시작점 거리 0

    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < L and 0 <= ny < L and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1  # 이동 횟수 갱신
                if (nx, ny) == (tx, ty):
                    print(dist[nx][ny])
                    q.clear()  # 루프 탈출
                    break
                q.append((nx, ny))
