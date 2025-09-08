import sys
sys.stdin = open("input.txt", "r")

graph = []
question = []
visited = [[False for _ in range(5)] for _ in range(5)]
cnt = 0
for i in range(5):
    graph.append(list(map(int, input().split(" "))))
for i in range(5):
    question.append(list(map(int, input().split(" "))))

def find(ans):
    global graph, cnt, visited
    for a in range(5):
        for b in range(5):
            if graph[a][b] == ans:
                visited[a][b] = True
                cnt +=1
                return
def check():
    count = 0
    # 가로 검사
    for i in range(5):
        if visited[i][0] and visited[i][1] and visited[i][2] and visited[i][3] and visited[i][4]:
            count += 1
    # 세로 검사
    for i in range(5):
        if visited[0][i] and visited[1][i] and visited[2][i] and visited[3][i] and visited[4][i]:
            count += 1

    # 대각선 검사
    if visited[0][0] and visited[1][1] and visited[2][2] and visited[3][3] and visited[4][4]:
        count += 1
    if visited[4][0] and visited[3][1] and visited[2][2] and visited[1][3] and visited[0][4]:
        count += 1

    if count >= 3:
        return True
    else:
        return False
for i in range(5):
    for j in range(5):
        ans = question[i][j]
        find(ans)
        if check():
            print(cnt)
            sys.exit(0)
