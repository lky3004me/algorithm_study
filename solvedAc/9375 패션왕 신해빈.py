from collections import defaultdict
from functools import reduce

T = int(input())
for _ in range(T):
    n = int(input())
    clothes = defaultdict(int)

    for _ in range(n):
        item, category = input().split()
        clothes[category] += 1

    answer = reduce(lambda x, y: x * (y + 1), clothes.values(), 1) - 1
    print(answer)
