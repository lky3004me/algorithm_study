import sys
sys.stdin= open("input.txt", "r")
input = sys.stdin.readline

t = int(input())
for i in range(t):
    tmpr, s = input().split()
    r = int(tmpr)

    for ch in s:
        for j in range(r):
            print(ch, end="")
    print()