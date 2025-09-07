import sys
input = sys.stdin.readline

def custom_round(x):
    # 문제 조건에 따라 0.5 이상이면 무조건 올림
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)

n = int(input())
if n == 0:
    print(0)
    exit()

data = [int(input()) for _ in range(n)]
data.sort()

cut = int(n * 0.15 + 0.5)  # 반올림해서 정수로 자름

trimmed = data[cut:n - cut]
avg = sum(trimmed) / len(trimmed)
print(custom_round(avg))
