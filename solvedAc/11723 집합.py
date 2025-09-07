import sys

input = sys.stdin.readline

M = int(input())
S = 0  # 비트 마스크로 집합 표현 (1부터 20까지)

for _ in range(M):
    cmd = input().split()
    op = cmd[0]

    if op == "add":
        x = int(cmd[1])
        S |= (1 << x)
    elif op == "remove":
        x = int(cmd[1])
        S &= ~(1 << x)
    elif op == "check":
        x = int(cmd[1])
        # x번 비트가 켜져 있으면 1, 아니면 0
        print(1 if S & (1 << x) else 0)
    elif op == "toggle":
        x = int(cmd[1])
        S ^= (1 << x)
    elif op == "all":
        # 1~20번 전체 비트 켜기
        S = (1 << 21) - (1 << 1)  # 또는 (1 << 21)-2
    elif op == "empty":
        S = 0
