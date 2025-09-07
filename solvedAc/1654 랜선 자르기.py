import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

start = 1
end = max(arr)
result = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for ele in arr:
        cnt += ele // mid

    if cnt >= n:
        result = mid      # 현재 길이(mid)도 조건 만족하니 저장
        start = mid + 1   # 더 긴 길이로 도전
    else:
        end = mid - 1     # 너무 길게 잘라서 n개 못 만듦 → 길이 줄이자

print(result)
