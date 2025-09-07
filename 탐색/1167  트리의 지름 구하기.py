from collections import deque
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n+1)]

for _ in range(n):
    data = list(map(int, input().split()))
    index = 0
    s = data[index]
    index +=1
    while True:
        e = data[index]
        if e == -1:
            break
        v = data[index +1]
        arr[s].append((e, v))
        index +=2

distance = [0] *(n+1)
visited = [False] *(n+1)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now = queue.popleft()
        for i in arr[now]:
            if not visited[i[0]]:
                visited[i[0]]= True
                queue.append(i[0])
                distance[i[0]] = distance[now] + i[1]

bfs(1)
max = 1
for i in range(2, n+1):
    if distance[max] < distance[i]:
        max = i

distance = [0] *(n+1)
visited = [False] * (n+1)
bfs(max)
distance.sort()
print(distance[n])