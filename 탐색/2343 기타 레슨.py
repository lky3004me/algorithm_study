import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
lectures = list(map(int, input().split()))

def is_possible(size):
    count = 1
    total = 0
    for length in lectures:
        if total + length > size:
            total = 0
            count +=1
        total += length
    return count <= m


left = max(lectures)
right = sum(lectures)
answer = right

while left <= right:
    mid = (left + right) //2
    if is_possible(mid):
        answer = mid
        right = mid -1
    else:
        left = mid + 1

print(answer)