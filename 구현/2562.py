import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

max = -1
cnt = -1
for i in range(1,10):
    tmp = int(input())
    if tmp > max:
        max = tmp
        cnt = i

print(max)
print(cnt)