import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))
    cnt = 0

    while True:
        if q[0] == max(q):          # 지금이 최고 우선순위면 출력
            q.popleft()
            cnt += 1
            if m == 0:              # 내가 찾는 문서면 끝
                print(cnt)
                break
            else:
                m -= 1              # 왼쪽으로 한 칸 당겨졌으니 타깃 인덱스 감소
        else:                       # 최고가 아니면 뒤로 보냄
            q.append(q.popleft())
            if m == 0:              # 타깃이 맨 앞이었으면 뒤로 이동
                m = len(q) - 1
            else:
                m -= 1
