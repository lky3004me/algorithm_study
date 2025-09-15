import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

arr.sort()

def lower_bound(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:      # x보다 작은 건 왼쪽 구간 확정 → 오른쪽으로 이동
            lo = mid + 1
        else:               # a[mid] >= x면 x의 첫 위치가 mid 이하
            hi = mid
    return lo

def upper_bound(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] <= x:     # x 이하면 더 오른쪽으로
            lo = mid + 1
        else:               # a[mid] > x면 x의 마지막 위치가 mid 미만
            hi = mid
    return lo

def count_x(a, x):
    return upper_bound(a, x) - lower_bound(a, x)

ans = [str(count_x(arr, t)) for t in targets]
print(" ".join(ans))
