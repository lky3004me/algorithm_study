from collections import Counter
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

# 1. 산술 평균
print(round(sum(arr) / n))

# 2. 중앙값
print(arr[n // 2])

# 3. 최빈값
counter = Counter(arr)
most_common = counter.most_common()
max_freq = most_common[0][1]

candidates = [num for num, freq in most_common if freq == max_freq]
candidates.sort()
print(candidates[1] if len(candidates) > 1 else candidates[0])

# 4. 범위
print(arr[-1] - arr[0])
