import sys
input = sys.stdin.readline

n = int(input())
pos = []
neg = []
ones = 0
zeros = 0
rst = 0

for _ in range(n):
    x = int(input())
    if x > 1:
        pos.append(x)
    elif x == 1:
        ones += 1
    elif x == 0:
        zeros += 1
    else:
        neg.append(x)

# 양수는 큰 수끼리 곱하기
pos.sort(reverse=True)
for i in range(0, len(pos)-1, 2):
    rst += pos[i] * pos[i+1]
if len(pos) % 2 == 1:
    rst += pos[-1]

# 음수는 작은 수끼리 곱하기
neg.sort()
for i in range(0, len(neg)-1, 2):
    rst += neg[i] * neg[i+1]
if len(neg) % 2 == 1:
    if zeros > 0:
        # 음수 하나를 0과 곱해서 없앰
        zeros -= 1
    else:
        rst += neg[-1]

# 1은 모두 더하기
rst += ones

print(rst)
