import sys
input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

# 끝나는 시간 기준 오름차순 정렬, 끝나는 시간이 같으면 시작 시간 기준 정렬
arr.sort(key=lambda x: (x[1], x[0]))

end_time = 0
count = 0

for start, end in arr:
    if start >= end_time:
        end_time = end
        count += 1

print(count)
