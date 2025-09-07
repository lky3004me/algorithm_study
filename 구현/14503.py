import sys
input = sys.stdin.readline
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0

while True:
    # 1. 현재 칸 청소
    if room[r][c] == 0:
        room[r][c] = 2  # 청소함 표시
        cnt += 1

    # 2. 4방향 탐색
    cleaned = False
    for _ in range(4):
        d = (d + 3) % 4  # 반시계 회전
        nx = r + dx[d]
        ny = c + dy[d]

        if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0:
            r, c = nx, ny
            cleaned = True
            break

    if cleaned:
        continue

    # 3. 후진
    back = (d + 2) % 4
    r -= dx[back]
    c -= dy[back]

    if room[r][c] == 1:  # 벽이면 정지
        break

print(cnt)
