import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = [list(input()) for _ in range(n)]

def check(board, n):
    max_count = 1
    for i in range(n):
        # 행 검사
        count = 1
        for j in range(1, n):
            if board[i][j] == board[i][j - 1]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
        # 열 검사
        count = 1
        for j in range(1, n):
            if board[j][i] == board[j - 1][i]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
    return max_count


rst = 0
for i in range(n):
    for j in range(n):
        if j + 1 < n:
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            temp = check(arr, n)
            result = max(rst, temp)
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            # 아래쪽 교환
        if i + 1 < n:
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
            temp = check(arr, n)
            result = max(rst, temp)
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]

print(rst)
