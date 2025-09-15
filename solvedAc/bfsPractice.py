# from collections import deque
#
# n,m = map(int, input().split())
#
# graph = [[] for _ in range(n+1)]
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# visited=[False] * (n+1)
#
# def bfs(start):
#     queue = deque()
#     queue.append(start)
#     visited[start] = True
#
#     while queue:
#         now = queue.popleft()
#         for next_node in graph[now]:
#             if not visited[next_node]:
#                 visited[next_node] = True
#                 queue.append(next_node)
#
# start_node = int(input())
# bfs(start_node)
# from collections import deque
#
# n, m = map(int, input().split())
#
# graph = [[] for _ in range(n+1)]
#
# for _ in range(n):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(b)
#
# visited = [False] * (n+1)
#
# def bfs(start):
#     queue = deque()
#     queue.append(start)
#     visited[start] = True
#
#     while queue:
#         now = queue.popleft()
#
#         for next_node in graph[now]:
#             if not visited[next_node]:
#                 visited[next_node] = True
#                 queue.append(next_node)
#
#
# start_node = int(input())
# bfs(start_node)
# from collections import deque
#
# n, m = map(int, input().split())
#
# graph = [[] for _ in range(n+1)]
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# visited = [False] *(n+1)
#
# def bfs(start):
#     queue = deque()
#     queue.append(start)
#     visited[start] = True
#
#     while queue:
#         now = queue.popleft()
#
#         for next_node in graph[now]:
#             if not visited[next_node]:
#                 visited[next_node] = True
#                 queue.append(next_node)
#
# start_node = int(input())
# bfs(start_node)
# from collections import deque
#
# n,m = map(int, input().split())
#
# graph = [[] for _ in range(n+1)]
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# visited = [False] *(n+1)
#
# def bfs(start):
#     queue = deque()
#     queue.append(start)
#     visited[start] = True
#
#     while queue:
#         now = queue.popleft()
#
#         for next_node in graph[now]:
#             if not visited[next_node]:
#                 visited[next_node] = True
#                 queue.append(next_node)
#
# start_node = int(input())
# bfs(start_node)
# from collections import deque
#
# n,m = map(int, input().split())
#
# board = [list(map(int, input().split())) for _ in range(n)]
#
# visited = [[False] * m for _ in range(n)]
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def bfs(start_x, start_y):
#     queue = deque()
#     queue.append((start_x, start_y))
#     visited[start_x][start_y] = True
#
#     while queue:
#         x, y = queue.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if 0<= nx <n and 0 <= ny <m:
#                 if not visited[nx][ny] and board[nx][ny] == 1:
#                     visited[nx][ny] = True
#                     queue.append((nx, ny))
#
# sx, sy = map(int, input().split())
# bfs(sx, sy)
# from collections import deque
# n, m = map(int, input().split())
#
# graph = [[] for _ in range(n+1)]
#
# for _ in range(n):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# visited = [False] *(n+1)
#
# def bfs(start):
#     queue = deque()
#     queue.append(start)
#     visited[start] = True
#
#     while queue:
#         now = queue.popleft()
#
#         for next_node in graph[now]:
#             if not visited[next_node]:
#                 visited[next_node] = True
#                 queue.append(next_node)
#
# start_node = int(input())
# bfs(start_node)
# from collections import deque
#
# n, m = map(int, input().split())
#
# graph = [[] for _ in range(n+1)]
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# visited = [False] *(n+1)
#
# def bfs(start):
#     queue = deque()
#     queue.append(start)
#     visited[start] = True
#
#     while queue:
#         now = queue.popleft()
#
#         for next_node in graph[now]:
#             if not visited[next_node]:
#                 visited[next_node] = True
#                 queue.append(next_node)
#
# start = int(input())
# bfs(start)
# from collections import deque
#
# # N: 세로, M: 가로
# n, m = map(int, input().split())
#
# board = [list(map(int, input().split())) for _ in range(n)]
#
# visited = [[False] * m for _ in range(n)]
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def bfs(start_x, start_y):
#     queue = deque()
#     queue.append((start_x, start_y))
#
#     while queue:
#         x, y = queue.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if 0 <= nx < n and 0 <= ny <m:
#                 if not visited[nx][ny] and board[nx][ny] ==1 :
#                     visited[nx][ny] = True
#                     queue.append((nx, ny))
#
# sx, sy = map(int, input().split())
# bfs(sx, sy)

# N: 세로, M: 가로
# 방향: 상, 하, 좌, 우
# 시작 좌표 입력 후 BFS 실행
#
# from collections import deque
#
# n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
#
# visited = [[False] * m for _ in range(n)]
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# sx, sy = map(int, input().split())
#
# def bfs(start_x, start_y):
#     queue = deque()
#     queue.append((start_x, start_y))
#
#     while queue:
#         x, y = queue.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if 0 <= nx < n and 0 <= ny < m:
#                 if not visited[nx][ny] and graph[nx][ny] == 1:
#                     visited[nx][ny] = True
#                     queue.append((nx, ny))
#
# bfs(sx, sy)
# from collections import deque
#
# n,m = map(int, input().split())
#
# board = [list(map(int, input().split())) for _ in range(n)]
#
# visited = [[False] * m for _ in range(n)]
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def bfs(start_x, start_y):
#     queue = deque()
#     queue.append((start_x, start_y))
#     visited[start_x][start_y] = True
#
#     while queue:
#         x, y = map(int, input().split())
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if 0 <= nx < n and 0<= ny <m:
#                 if not visited[nx][ny] and board[nx][ny] ==1 :
#                     queue.append((nx, ny))
#                     visited[nx][ny] = True
#
# sx, sy = map(int, input().split())
# bfs(sx, sy)
# import sys
# sys.setrecursionlimit(10**6)
#
# n,m = map(int, input().split())
#
# board = [list(map(int, input().split())) for _ in range(n)]
#
# visited =[[False] * m for _ in range(n)]
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def dfs(x, y):
#     visited[x][y] = True
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if 0 <= nx < n and 0 <= ny < m:
#             if not visited[nx][ny] and board[nx][ny] == 1:
#                 dfs(nx, ny)
#
# sx, sy = map(int, input().split())
# dfs(sx, sy)
# from collections import deque
#
# n,m = map(int, input().split())
#
# graph = [[] for _ in range(n+1)]
#
# visited = [False] *(n+1)
#
# for _ in range(n):
#     a, b = map(int, input().split())
#
#     graph[a].append(b)
#     graph[b].append(a)
#
# def bfs(start):
#     queue = deque()
#     queue.append(start)
#     visited[start] = True
#
#     while queue:
#         now = queue.popleft()
#
#         for next_node in graph[now]:
#             if not visited[next_node]:
#                 visited[next_node] = True
#                 queue.append(next_node)
#
# start_node = int(input())
# bfs(start_node)
# from collections import deque
#
# n,m = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
#
# visited = [[False for _ in range(m)] for _ in range(n)]
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def bfs(start_x, start_y):
#     queue = deque()
#     queue.append((start_x, start_y))
#     visited[start_x][start_y] = True
#
#     while queue:
#         x, y = queue.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if 0 <= nx < n and 0 <= ny < m:
#                 if not visited[nx][ny] and board[nx][ny] == 1:
#                     queue.append((nx,ny))
#                     visited[nx][ny]= True
#
# sx, sy = map(int, input().split())
# bfs(sx, sy)
# import sys
# sys.setrecursionlimit(10**6)
# n,m = map(int, input().split())
#
# graph = [[] for _ in range(n+1)]
#
# for _ in range(n):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# visited = [False] *(n+1)
#
# def dfs(now):
#     visited[now] = True
#
#     for next_node in graph[now]:
#         if not visited[next_node]:
#             dfs(next_node)
#
# start_node = int(input())
# dfs(start_node)
# import sys
# sys.setrecursionlimit(10**6)
#
# n,m = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# visited = [False for _ in range(n+1)]
#
# for _ in range(n):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# def dfs(now):
#     visited[now] = True
#
#     for next_node in graph[now]:
#         if not visited[next_node]:
#             dfs(next_node)
#
# start_node = int(input())
# dfs(start_node)
# import sys
# sys.setrecursionlimit(10**6)
#
# n,m = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
# visited = [[False for _ in range(m)] for _ in range(n)]
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def dfs(x, y):
#     visited[x][y] = True
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if 0<= nx <n and 0<=ny <m:
#             if not visited[nx][ny] and board[nx][ny] ==1:
#                 dfs(nx, ny)
#
# sx, sy = map(int, input().split())
# dfs(sx, sy)
# import sys
# sys.setrecursionlimit(10**6)
#
# n,m = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
# visited = [[False for _ in range(m)] for _ in range(n)]
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def dfs(x, y):
#     visited[x][y] = True
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if 0 <= nx < n and 0< ny <= m:
#             if not visited[nx][ny] and board[nx][ny] == 1:
#                 dfs(nx, ny)
#
# sx, sy = map(int, input().split())
# dfs(sx, sy)
# import sys
# sys.setrecursionlimit(10**6)
#
# n,m = map(int, input().split())
# board = [list(map(int, input().split()))]
# visited = [[False for _ in range(m)] for _ in range(n)]
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def dfs(x, y):
#     visited[x][y] = True
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if 0<= nx <n and 0 <= ny <m :
#             if not visited[nx][ny] and board[nx][ny] == 1:
#                 dfs(nx, ny)
#
# sx, sy = map(int ,input().split())
# dfs(sx, sy)
# from collections import deque
#
# n,m = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
# visited = [[False for _ in range(m)] for _ in range(n)]
#
# def bfs(start_x,start_y):
#     queue = deque()
#     visited[start_x][start_y] = True
#     queue.append((start_x,start_y))
#
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#
#     while queue:
#         x, y =queue.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if 0 <= nx < n and 0 <= ny < m:
#                 if not visited[nx][ny] and board[nx][ny] == 1:
#                     queue.append((nx, ny))
#                     visited[nx][ny] = True
#
# sx, sy = map(int, input().split())
# bfs(sx, sy)
# from collections import deque
#
# n, m = map(int, input().split())
#
# graph = [[] for _ in range(n+1)]
#
# for _ in range(n):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# visited = [False] * (n+1)
#
# def bfs(start):
#     queue = deque()
#     queue.append(start)
#     visited[start] = True
#
#     while queue:
#         now = queue.popleft()
#
#         for next_node in graph[now]:
#             if not visited[next_node]:
#                 visited[next_node] = True
#                 queue.append(next_node)
# start_node = int(input())
# bfs(start_node)
# from collections import deque
#
# n,m = map(int, input().split())
#
# board = [list(map(int, input().split())) for _ in range(n)]
#
# visited = [[False for _ in range(m)] for _ in range(n)]
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def bfs(start_x, start_y):
#     queue = deque()
#     queue.append((start_x, start_y))
#     visited[start_x][start_y] = True
#
#     while queue:
#         x, y = queue.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if 0 <= nx < n and 0 <= ny < m:
#                 if not visited[nx][ny] and board[nx][ny] == 1 :
#                     queue.append((nx, ny))
# sx, sy = map(int, input().split())
# bfs(sx, sy)
# from collections import deque
#
# n,m = map(int, input().split())
#
# board = [list(map(int, input().split())) for _ in range(n)]
#
# visited = [[False for _ in range(m)] for _ in range(n)]
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def bfs(start_x, start_y):
#     queue = deque()
#     queue.append((start_x, start_y))
#     visited[start_x][start_y] = True
#
#     while queue:
#         x, y = queue.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if 0<= nx < n and 0 <= ny < m:
#                 if not visited[nx][ny] and board[nx][ny] == 1:
#                     queue.append((nx, ny))
#
# sx, sy = map(int, input().split())
# bfs(sx, sy)
# import sys
# sys.setrecursionlimit(10**6)
#
# n,m = map(int, input().split())
#
# board = [list(map(int, input().split())) for _ in range(n)]
#
# visited = [[False for _ in range(m)] for _ in range(n)]
#
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#
# def dfs(x, y):
#     visited[x][y] = True
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if 0 <= nx < n and 0<= ny <m:
#             if not visited[nx][ny] and board[nx][ny] == 1:
#                 dfs(nx, ny)
#
# sx, sy = map(int, input().split())
# dfs(sx, sy)
# from collections import deque
#
# n,m = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
#
# visited = [[False for _ in range(m)] for _ in range(n)]
#
# dx = [-1,1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def bfs(startX, startY):
#     queue = deque()
#     visited[startY][startX] = True
#     queue.append((startX, startY))
#
#     while queue:
#         x, y = queue.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if 0 <= nx < m and 0 <= ny <n:
#                 if not visited[ny][nx]:
#                     queue.append((nx,ny))
#                     visited[ny][nx] = True
# sx, sy = map(int, input().split())
# bfs(sx, sy)
# n, m = map(int, input().split())
# board = [list(map, input().split()) for _ in range(n)]
# visited = [[False for _ in range(m)] for _ in range(n)]
#
# dx = [-1,1,0,0]
# dy = [0,0, -1, 1]
#
# def dfs(x, y):
#     visited[y][x] = True
#
#     for i in range(4):
#         nx = x +dx[i]
#         ny = y + dy[i]
#
#         if 0<= nx < m and 0<=ny <n:
#             if not visited[ny][nx]:
#                 dfs(nx, ny)
#
# sx, sy = map(int, input().split())
# dfs(sx, sy)

def bubble(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j + 1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]

    return arr

data = [5,3,87,4,2]
print(bubble(data))