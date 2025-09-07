import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n,m,start = map(int, input().split())
arr = [[]  for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(n+1):
    arr[i].sort()


def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for i in arr[v]:
        if not visited[i]:
            dfs(i)

visited = [False] *(n+1)
dfs(start)


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        print(now_Node, end=' ')
        for i in arr[now_Node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

print()
visited = [False] *(n+1)
bfs(start)