import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
board = [[0]*100 for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())
    # (x, y)를 왼쪽 아래 꼭짓점으로 하는 10x10 영역을 1로 채움
    for i in range(y, y+10):
        for j in range(x, x+10):
            board[i][j] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

perimeter = 0
for r in range(100):
    for c in range(100):
        if board[r][c] == 1:
            for k in range(4):
                nr, nc = r + dy[k], c + dx[k]
                if not (0 <= nr < 100 and 0 <= nc < 100) or board[nr][nc] == 0:
                    perimeter += 1

print(perimeter)
