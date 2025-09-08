import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
cnt = 0
n = int(input())
visited = [[False for _ in range(101)] for _ in range(101)]
dx = [1, 0, 1]
dy = [0, 1, 1]
for _ in range(n):
    x, y = map(int, input().split())

    for i in range(y+1, y+11):
        for j in range(x+1, x+11):
            visited[i][j] = True


for i in range(101):
    for j in range(101):
        if visited[i][j]:
            cnt +=1
print(cnt)
