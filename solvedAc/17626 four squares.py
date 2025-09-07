import sys, math
input = sys.stdin.readline

n = int(input())
# ① 1개: 제곱수?
if int(math.isqrt(n))**2 == n:
    print(1)
    sys.exit()

# 제곱수 집합 precompute
squares = {i*i for i in range(1, math.isqrt(n)+1)}

# ② 2개 합
for a in squares:
    if (n - a) in squares:
        print(2)
        sys.exit()

# ③ 3개 합
for a in squares:
    for b in squares:
        if a + b >= n:
            continue
        if (n - a - b) in squares:
            print(3)
            sys.exit()

# ④ 그 외 4
print(4)
