# import sys
# sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline
#
# c, r = map(int, input().split())
# k = int(input())
#
# visited = [[False for _ in range(c+1)] for _ in range(r+1)]
#
# if k > c*r:
#     print(0)
#     sys.exit(0)
#
# x, y = 0,0
# dx = [0,1,0,-1]
# dy = [1,0,-1,0]
# # 0 : 상승, 1 : 우현, 2 : 하강, 3: 좌현
# i = 0
# cnt = 1
# visited[y][x] = True
#
# while True:
#     if cnt == k:
#         print(x+1, y+1)
#         break
#
#     nx = x + dx[i]
#     ny = y + dy[i]
#
#     if 0<= nx < c and 0<= ny < r:
#         if not visited[ny][nx]:
#             x, y = nx, ny
#             visited[y][x] = True
#             cnt +=1
#         else:
#             i = (i+1)%4
#     else:
#         i = (i+1)%4
#
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

c, r = map(int, input().split())
k = int(input())

visited = [[False for _ in range(c+1)] for _ in range(r+1)]

x, y = 0, 0
# 0번 : 상승, 1번 : 우현, 2번 하강, 3번 : 좌현
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cnt = 1
i = 0
visited[y][x] = True
if k > c*r:
    print(0)
    sys.exit(0)

while True:
    if cnt == k:
        break
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < c and 0 <= ny <r:
        if not visited[ny][nx]:
            x, y = nx, ny
            visited[ny][nx] = True
            cnt+=1
        else:
            i = (i+1)%4
    else:
        i = (i+1)%4

print(x+1, y+1)